
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_values = []
y_values = []

fig, ax = plt.subplots()
ax.set_xlim(0, 105)
ax.set_ylim(0, 20)
line, = ax.plot(0, 0)

angle, vector = 90, [10, 0]

initial_angle = np.radians(0)
final_angle = np.radians(angle)

initial_vector = np.array(vector)

angle_ranges = np.arange(initial_angle, final_angle, 1)

print(angle_ranges)


# def animation_frame(angle, vector):
    
#     initial_angle = np.radians(0)
#     final_angle = np.radians(angle)

#     initial_vector = np.array(vector)

#     angle_ranges = np.arange(initial_angle, final_angle, 1)
    

    # for angle_range in angle_ranges:
    #     rotation_matrix = np.array([ [round(np.cos(angle_range),4), round(-np.sin(angle_range),4)], [round(np.sin(angle_range),4), round(np.cos(angle_range),4)]])
    #     x_val = np.dot(rotation_matrix, initial_vector)[0]
    #     x_values.append(x_val)

    #     y_val = np.dot(rotation_matrix, initial_vector)[1]
    #     y_values.append(y_val)

    # line.set_xdata(x_values)
    # line.set_ydata(y_values)

#     return line,

# animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0,angle,1), interval=1)
# plt.show()