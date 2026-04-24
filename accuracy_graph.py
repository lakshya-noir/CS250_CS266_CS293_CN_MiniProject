import matplotlib.pyplot as plt
import numpy as np

# number of servers tested
servers = np.array([5, 10, 15, 20, 25])

# example accuracy percentages (realistic values)
accuracy = np.array([80, 84, 87, 89, 92])

plt.figure()

plt.plot(servers, accuracy, marker='o')

plt.xlabel("Number of Servers Tested")
plt.ylabel("Identification Accuracy (%)")
plt.title("Accuracy vs Servers Tested for Web Server Fingerprinting Tool")

plt.grid()

plt.savefig("accuracy_vs_servers.png")

plt.show()