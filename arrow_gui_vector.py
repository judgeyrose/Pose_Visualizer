import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

# Initial arrow parameters
init_pos = [0, 0, 0]
init_dir = [1, 0, 0]  # initial direction vector
arrow_length = 1

# Function to normalize a vector
def normalize(vec):
    norm = np.linalg.norm(vec)
    if norm == 0:
        return vec
    return vec / norm

def plot_arrow(ax, pos, direction):
    ax.cla()
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Arrow with Adjustable Direction Vector')
    dir_vec = normalize(direction) * arrow_length
    ax.quiver(pos[0], pos[1], pos[2], dir_vec[0], dir_vec[1], dir_vec[2], 
              length=arrow_length, normalize=True, color='b')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.25)

# Sliders for direction vector components
axcolor = 'lightgoldenrodyellow'
ax_dx = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_dy = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)
ax_dz = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)

s_dx = Slider(ax_dx, 'Dir X', -1, 1, valinit=init_dir[0])
s_dy = Slider(ax_dy, 'Dir Y', -1, 1, valinit=init_dir[1])
s_dz = Slider(ax_dz, 'Dir Z', -1, 1, valinit=init_dir[2])

def update(val):
    direction = [s_dx.val, s_dy.val, s_dz.val]
    plot_arrow(ax, init_pos, direction)
    plt.draw()

s_dx.on_changed(update)
s_dy.on_changed(update)
s_dz.on_changed(update)

# Initial plot
plot_arrow(ax, init_pos, init_dir)

plt.show()
