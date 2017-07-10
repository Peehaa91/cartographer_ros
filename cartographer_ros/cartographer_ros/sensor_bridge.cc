/*
 * Copyright 2016 The Cartographer Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "cartographer_ros/sensor_bridge.h"

#include "cartographer/kalman_filter/pose_tracker.h"
#include "cartographer_ros/msg_conversion.h"
#include "cartographer_ros/time_conversion.h"
#include <tf/transform_datatypes.h>

namespace cartographer_ros {

namespace carto = ::cartographer;

using carto::transform::Rigid3d;

namespace {

const string& CheckNoLeadingSlash(const string& frame_id) {
  if (frame_id.size() > 0) {
    CHECK_NE(frame_id[0], '/');
  }
  return frame_id;
}

}  // namespace

SensorBridge::SensorBridge(
    const string& tracking_frame, const double lookup_transform_timeout_sec,
    tf2_ros::Buffer* const tf_buffer,
    carto::mapping::TrajectoryBuilder* const trajectory_builder)
    : tf_bridge_(tracking_frame, lookup_transform_timeout_sec, tf_buffer),
      trajectory_builder_(trajectory_builder) {
	last_yaw_ = 0;
	last_roll_ = 0;
	last_pitch_ = 0;
	last_plane_msg_time_ = ros::Time(0);
}

void SensorBridge::HandleOdometryMessage(
    const string& sensor_id, const nav_msgs::Odometry::ConstPtr& msg) {
  const carto::common::Time time = FromRos(msg->header.stamp);
  const auto sensor_to_tracking = tf_bridge_.LookupToTracking(
      time, CheckNoLeadingSlash(msg->child_frame_id));
  if (sensor_to_tracking != nullptr) {
    trajectory_builder_->AddOdometerData(
        sensor_id, time,
        ToRigid3d(msg->pose.pose) * sensor_to_tracking->inverse());
  }
}

void SensorBridge::HandleImuMessage(const string& sensor_id,
                                    const sensor_msgs::Imu::ConstPtr& msg) {
  CHECK_NE(msg->linear_acceleration_covariance[0], -1)
      << "Your IMU data claims to not contain linear acceleration measurements "
         "by setting linear_acceleration_covariance[0] to -1. Cartographer "
         "requires this data to work. See "
         "http://docs.ros.org/api/sensor_msgs/html/msg/Imu.html.";
  CHECK_NE(msg->angular_velocity_covariance[0], -1)
      << "Your IMU data claims to not contain angular velocity measurements "
         "by setting angular_velocity_covariance[0] to -1. Cartographer "
         "requires this data to work. See "
         "http://docs.ros.org/api/sensor_msgs/html/msg/Imu.html.";

  const carto::common::Time time = FromRos(msg->header.stamp);
  const auto sensor_to_tracking = tf_bridge_.LookupToTracking(
      time, CheckNoLeadingSlash(msg->header.frame_id));
  if (sensor_to_tracking != nullptr) {
    CHECK(sensor_to_tracking->translation().norm() < 1e-5)
        << "The IMU frame must be colocated with the tracking frame. "
           "Transforming linear acceleration into the tracking frame will "
           "otherwise be imprecise.";
    trajectory_builder_->AddImuData(
        sensor_id, time,
        sensor_to_tracking->rotation() * ToEigen(msg->linear_acceleration),
        sensor_to_tracking->rotation() * ToEigen(msg->angular_velocity));
  }
}

void SensorBridge::HandleLaserScanMessage(
    const string& sensor_id, const sensor_msgs::LaserScan::ConstPtr& msg) {
  HandleRangefinder(sensor_id, FromRos(msg->header.stamp), msg->header.frame_id,
                    ToPointCloudWithIntensities(*msg).points);
}

void SensorBridge::HandleMultiEchoLaserScanMessage(
    const string& sensor_id,
    const sensor_msgs::MultiEchoLaserScan::ConstPtr& msg) {
  HandleRangefinder(sensor_id, FromRos(msg->header.stamp), msg->header.frame_id,
                    ToPointCloudWithIntensities(*msg).points);
}

void SensorBridge::HandlePointCloud2Message(
    const string& sensor_id, const sensor_msgs::PointCloud2::ConstPtr& msg) {
  pcl::PointCloud<pcl::PointXYZ> pcl_point_cloud;
  pcl::fromROSMsg(*msg, pcl_point_cloud);
  carto::sensor::PointCloud point_cloud;
  for (const auto& point : pcl_point_cloud) {
    point_cloud.emplace_back(point.x, point.y, point.z);
  }
  HandleRangefinder(sensor_id, FromRos(msg->header.stamp), msg->header.frame_id,
                    point_cloud);
}

const TfBridge& SensorBridge::tf_bridge() const { return tf_bridge_; }

void SensorBridge::HandleRangefinder(const string& sensor_id,
                                     const carto::common::Time time,
                                     const string& frame_id,
                                     const carto::sensor::PointCloud& ranges) {
  const auto sensor_to_tracking =
      tf_bridge_.LookupToTracking(time, CheckNoLeadingSlash(frame_id));
  if (sensor_to_tracking != nullptr) {
    trajectory_builder_->AddRangefinderData(
        sensor_id, time, sensor_to_tracking->translation().cast<float>(),
        carto::sensor::TransformPointCloud(ranges,
                                           sensor_to_tracking->cast<float>()));
  }
}

void SensorBridge::HandlePlaneMessage(
	const string& sensor_id, const cartographer_ros_msgs::PlaneStamped::ConstPtr& msg)
{
	const carto::common::Time time = FromRos(msg->header.stamp);
    const auto sensor_to_tracking = tf_bridge_.LookupToTracking(
	    time, CheckNoLeadingSlash(msg->header.frame_id));
    if (sensor_to_tracking != nullptr) {
      Eigen::Vector4d coefficients = Eigen::Vector4d(msg->plane.coef[0], msg->plane.coef[1],
    		  msg->plane.coef[2], msg->plane.coef[3]);
	  trajectory_builder_->AddPlaneData(
		  sensor_id, time,
		  coefficients);
    }
////	ROS_WARN_STREAM("Plane Received: "<<"a: "<<msg->plane.coef[0]<<" b: "<<msg->plane.coef[1]<<" c: "<<msg->plane.coef[2]
////								      <<" d: "<<msg->plane.coef[3]);
//	shape_msgs::Plane plane = msg->plane;
//	Eigen::Vector3f norm_vec_plane = Eigen::Vector3f(plane.coef[0], plane.coef[1], plane.coef[3]);
//	norm_vec_plane.normalize();
//	Eigen::Vector3f rot_axis = norm_vec_plane + Eigen::Vector3f(0,0,1);
//	rot_axis.normalize();
//	Eigen::Vector3f axis = rot_axis.cross(norm_vec_plane);
//	double angle = rot_axis.dot(norm_vec_plane);
//    /*double angle = std::acos(fabs(norm_vec_plane(0)*0 + norm_vec_plane(1)* 0+ norm_vec_plane(2)*1)
//    		/std::sqrt(norm_vec_plane(0)* norm_vec_plane(0) + norm_vec_plane(1)* norm_vec_plane(1) + norm_vec_plane(2)* norm_vec_plane(2)));*/
//    //angle_xy_plane = angle_xy_plane*(180/M_PI);
//    tf::Quaternion q = tf::Quaternion(axis(0), axis(1), axis(2), angle);
//    q.normalize();
//	//ROS_WARN_STREAM("angle: "<<q.getAngle()*180/M_PI);
//	geometry_msgs::Quaternion q_msg;
////	q_msg.x = q.;
////	q_msg.y = q.y;
////	q_msg.z = q.z;
////	q_msg.w = q.w;
////	Eigen::Vector3d lin_acc = ToEigen(msg->linear_acceleration);
//	tf::Matrix3x3 m(q);
//	double roll, pitch, yaw;
//	m.getRPY(roll, pitch, yaw);
//	//ROS_WARN_STREAM("roll: "<<roll*180/M_PI<<" pitch: "<<pitch*180/M_PI<<" yaw: "<<yaw*180/M_PI);
//
//	if (last_plane_msg_time_ == ros::Time(0))
//	{
//		last_plane_msg_time_ = msg->header.stamp;
//		last_yaw_ = yaw;
//		last_roll_ = roll;
//		last_pitch_ = pitch;
//		return;
//	}
//	Eigen::Vector3d lin_acc = Eigen::Vector3d(0,0,-9.81);
//	ros::Duration delta = msg->header.stamp - last_plane_msg_time_;
//	double delta_t = double(delta.sec) + double(delta.nsec)*1e-9;
//	//Eigen::Vector3d ang_vel = Eigen::Vector3d((roll - last_roll_)/delta_t,(pitch - last_pitch_)/delta_t,(yaw - last_yaw_)/delta_t);
//	Eigen::Vector3d ang_vel = Eigen::Vector3d(0,0,0);
//	last_plane_msg_time_ = msg->header.stamp;
//	last_yaw_ = yaw;
//	last_roll_ = roll;
//	last_pitch_ = pitch;
//
//	const carto::common::Time time = FromRos(msg->header.stamp);
//	const auto sensor_to_tracking = tf_bridge_.LookupToTracking(
//			time, CheckNoLeadingSlash("imu_link"));
//	if (sensor_to_tracking != nullptr) {
//	CHECK(sensor_to_tracking->translation().norm() < 1e-5)
//		<< "The plane frame must be colocated with the tracking frame. "
//		   "Transforming linear acceleration into the tracking frame will "
//		   "otherwise be imprecise.";
//	//ROS_INFO_STREAM("PLANE:"<<time);
//	trajectory_builder_->AddImuData(
//		"imu", time,
//		sensor_to_tracking->rotation() * lin_acc,
//		sensor_to_tracking->rotation() * ang_vel);}
//	else
//	  ROS_ERROR_STREAM("not found");
//
//    //tf::createQuaternionFromRPY(0,-angle_xy_plane,0);

}

}  // namespace cartographer_ros
