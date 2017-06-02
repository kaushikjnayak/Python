import matplotlib.patches as patches
import matplotlib.pyplot as plt

#draw circle

# Circle
shape = patches.Circle((0, 1), radius = 1., color = '.75')
plt.gca().add_patch(shape)

# Rectangle
shape = patches.Rectangle((1, 2), 2,3, color = 'b')
plt.gca().add_patch(shape)
plt.grid(True)
plt.axis('scaled')
plt.show()

# we can also get the shape from plt directly

shape = plt.Circle((1, 2), radius=2, color = 'b')
plt.gca().add_patch(shape)
plt.grid(True)
plt.axis('scaled')
plt.show()