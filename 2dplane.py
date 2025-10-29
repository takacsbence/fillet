import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('coo_list.txt')

print(data)

# Plot points
plt.scatter(data[:,0], data[:,1], color='red', label='Points')

# Connect points to show plane (polygon)
# Close the polygon by repeating the first point at the end
polygon = np.vstack([data, data[0]])
plt.plot(polygon[:,0], polygon[:,1], color='blue', alpha=0.5, label='Plane')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Plane from 4 Points')
plt.legend()
plt.grid(True)
plt.show()
