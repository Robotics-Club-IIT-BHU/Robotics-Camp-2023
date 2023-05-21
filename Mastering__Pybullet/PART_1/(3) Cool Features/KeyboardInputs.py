import pybullet as p
import pybullet_data

p.connect(p.GUI)  # or p.SHARED_MEMORY or p.DIRECT
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")
p.setGravity(0, 0, -10)

pos = [[1, 0, 1], [0, 1, 1], [-1, 0, 1], [0, -1, 1]]

# Spheres will be spawned at various positions depending on the pressed key
while (1):
    keys = p.getKeyboardEvents()
    for k, v in keys.items():
        if (k == p.B3G_UP_ARROW and (v & p.KEY_IS_DOWN)):
            ID = p.loadURDF("sphere.urdf", pos[0])

        if (k == p.B3G_LEFT_ARROW and (v & p.KEY_IS_DOWN)):
            ID = p.loadURDF("sphere.urdf", pos[1])

        if (k == p.B3G_DOWN_ARROW and (v & p.KEY_IS_DOWN)):
            ID = p.loadURDF("sphere.urdf", pos[2])

        if (k == p.B3G_RIGHT_ARROW and (v & p.KEY_IS_DOWN)):
            ID = p.loadURDF("sphere.urdf", pos[3])
            
    p.stepSimulation()

p.disconnect()
