import matplotlib.pyplot as plt
import numpy as np

class CreateImage():
    def __init__(self,TriangleList):
        self._triangles = TriangleList #get a list of triangles can be done multiple ways
        self._umax = 1
        self._umin = 0
        self._u = 0.0

    def plot_Triangles(self):# Plot the mesh by adding all triangles with their value
        plt.figure()

         # Create the colormap
        sm = plt.cm.ScalarMappable(cmap='viridis')
        sm.set_array([self._umin,self._umin])

        cbar_ax = plt.gca().inset_axes([1, 0, 0.05, 1])  # adjust position and size as needed
        plt.colorbar(sm, cax=cbar_ax, label='c')

        for i in self._triangles:
            plt.gca().add_patch(plt.Polygon(i.get_coordinates(), color=plt.cm.viridis((self._u - self._umin)/(self._umax - self._umin)), alpha=0.9))
        # Add labels to axes
        plt.xlabel('a')
        plt.ylabel('b')

        plt.xlim(0, 1)  # set the x-axis limits
        plt.ylim(0, 1)  # set the y-axis limits
        plt.gca().set_aspect('equal')

    def save_img(self,file_loc):
        # Show plot
        plt.savefig(file_loc)
        
