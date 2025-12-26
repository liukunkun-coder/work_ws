# 之于G1机器人在gazebo中扫描模拟钢材的部署
## G1 人形机器人 · 货架缝隙 RGB 检测仿真

## 1 需求
- 机器人：G1 人形
- 传感器：腕部 RGB 相机
- 场景：工厂货架金属板件 
- 输出：ROS topic `/camera/image_raw` 

## 2 启动（3 步）
### 配置
-Ubuntu 20.04 ros-noetic 
###启动 命令
bash 
<pre >
catkin_make 
source devel/setup. bash 
roslaunch g1_description gazebo _display. launch 
</pre >

另开终端 
<pre>
rostopic list
rqt
</pre>
查看相机输出