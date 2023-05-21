import pybullet as p
import pybullet_data

p.connect(p.GUI)  #or p.SHARED_MEMORY or p.DIRECT
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")
p.setGravity(0, 0, -10)

carpos = [0, 0, 0.1]
car = p.loadURDF("husky/husky.urdf", carpos[0], carpos[1], carpos[2])

numJoints = p.getNumJoints(car)
for joint in range(numJoints):
  print(p.getJointInfo(car, joint))

targetVel = 1  #rad/s
maxForce = 100 #Newton

while (1):
    for joint in range(2, 6):
        p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL,targetVelocity = targetVel,force = maxForce)
    
    p.stepSimulation()

p.disconnect()
