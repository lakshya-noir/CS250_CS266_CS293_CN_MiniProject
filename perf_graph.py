import matplotlib.pyplot as plt
import numpy as np

servers = np.array([1, 3, 5, 10, 15])
time_taken = np.array([40, 120, 210, 420, 630])  # milliseconds

plt.figure()

plt.plot(servers, time_taken, marker='o')

plt.xlabel("Number of Servers")
plt.ylabel("Total Scan Time (ms)")
plt.title("Multi-Server Testing Performance")

plt.grid()

plt.savefig("servers_vs_time.png")

plt.show()