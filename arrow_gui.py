import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

# Initial arrow parameters
init_pos = [0, 0, 0]
init_angles = [0, 0, 0]  # yaw, pitch, roll in degrees
arrow_length = 1

# Function to compute arrow direction from angles
def get_arrow_vector(yaw, pitch, roll, length=1):
    # Convert degrees to radians
    yaw = np.deg2rad(yaw)
    pitch = np.deg2rad(pitch)
    roll = np.deg2rad(roll)
    # Rotation matrices
    Rz = np.array([
        [np.cos(yaw), -np.sin(yaw), 0],
        [np.sin(yaw), np.cos(yaw), 0],
        [0, 0, 1]
    ])
    Ry = np.array([
        [np.cos(pitch), 0, np.sin(pitch)],
        [0, 1, 0],
        [-np.sin(pitch), 0, np.cos(pitch)]
    ])
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(roll), -np.sin(roll)],
        [0, np.sin(roll), np.cos(roll)]
    ])
    # Apply rotations: Rz * Ry * Rx
    R = Rz @ Ry @ Rx
    # Arrow points along x-axis by default
    v = np.array([length, 0, 0])
    return R @ v

def plot_arrow(ax, pos, angles):
    ax.cla()
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Arrow with Adjustable Angles')
    arrow_vec = get_arrow_vector(*angles, length=arrow_length)
    ax.quiver(pos[0], pos[1], pos[2], arrow_vec[0], arrow_vec[1], arrow_vec[2], 
              length=arrow_length, normalize=True, color='r')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.25)

# Initial plot
drawn = plot_arrow(ax, init_pos, init_angles)

# Sliders for yaw, pitch, roll
axcolor = 'lightgoldenrodyellow'
ax_yaw = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_pitch = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)
ax_roll = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)

s_yaw = Slider(ax_yaw, 'Yaw (deg)', -180, 180, valinit=init_angles[0])
s_pitch = Slider(ax_pitch, 'Pitch (deg)', -90, 90, valinit=init_angles[1])
s_roll = Slider(ax_roll, 'Roll (deg)', -180, 180, valinit=init_angles[2])

def update(val):
    angles = [s_yaw.val, s_pitch.val, s_roll.val]
    plot_arrow(ax, init_pos, angles)
    plt.draw()

s_yaw.on_changed(update)
s_pitch.on_changed(update)
s_roll.on_changed(update)

plt.show()
