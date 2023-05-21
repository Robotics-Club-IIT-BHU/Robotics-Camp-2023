import pybullet as p
import pybullet_data

p.connect(p.GUI)  # or p.SHARED_MEMORY or p.DIRECT
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")
p.setGravity(0, 0, -10)

# Watch the spheres spawning as you move the pointer
while (1):
    output = p.getMouseEvents()
    for t, x, y, i, s in output:
        if(t==1):
            p.loadURDF("sphere.urdf", [x/200, y/200, 1])
            
    p.stepSimulation()

p.disconnect()
