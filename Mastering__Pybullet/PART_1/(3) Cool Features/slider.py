import pybullet as p
import pybullet_data

p.connect(p.GUI)  # or p.SHARED_MEMORY or p.DIRECT
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")
p.setGravity(0, 0, -10)

sliderID = p.addUserDebugParameter("Position_x", 0, 15, 1)
new_pos_x = 0
while(1):
    old_pos_x = new_pos_x
    new_pos_x = p.readUserDebugParameter(sliderID)
    if(old_pos_x!=new_pos_x):
        p.loadURDF("sphere.urdf", [new_pos_x, 0, 10])
    p.stepSimulation()
p.disconnect()
