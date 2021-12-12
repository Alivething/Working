import matplotlib.pyplot as plt

case = ['Case 1', 'Case 2', 'Case 3']
latency = [729.93, 729.878, 799.767]
unpriolatency = [799.767, 799.767, 799.767]

plt.ylabel("Latency (ms)")

plt.plot(case, latency, label = "Prioritized")
plt.plot(case, unpriolatency, label = "Unprioritized")
plt.legend()
plt.grid()
plt.show()