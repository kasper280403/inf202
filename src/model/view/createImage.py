import matplotlib.pyplot as plt
import numpy as np


umax = 1
umin = 0

u = 0.0 # used for different colors

Triangles = Mesh.get_triangles()
# Plot the mesh by adding all triangles with their value
plt.figure()

# Create the colormap
sm = plt.cm.ScalarMappable(cmap='viridis')
sm.set_array([umin,umax])



# Add colorbar using a separate axis
cbar_ax = plt.gca().inset_axes([1, 0, 0.05, 1])  # adjust position and size as needed
plt.colorbar(sm, cax=cbar_ax, label='c')
for i in Triangles:
    plt.gca().add_patch(plt.Polygon(i.get_coordinates(), color=plt.cm.viridis((u - umin)/(umax - umin)), alpha=0.9))



# Add labels to axes
plt.xlabel('a')
plt.ylabel('b')

plt.xlim(0, 1)  # set the x-axis limits
plt.ylim(0, 1)  # set the y-axis limits
plt.gca().set_aspect('equal')

# Show plot
plt.savefig(f"img_test.png")

plt.close()