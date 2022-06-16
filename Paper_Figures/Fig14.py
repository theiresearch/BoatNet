import numpy as np
import matplotlib.pyplot as plt

size = 8
x = np.arange(size)
print(x)
Santa = [27,26,13.25,3.67,16.25,11.11,26,25]
Loreto = [40,26,24.8,9.17,12.4,8.86,9.6,10.75]
Guaymas = [99,35.5,98.5,49,64.6,70.5,35.83,46.75]

total_width, n = 0.8, 3
width = total_width / n
x = x - (total_width - width) / 2
x1 = x + width
x2 = x + 2 * width
print(x)

string_x = ["Mar-19", "Jun-19", "Sep-19", "Dec-19", "Mar-20", "Jun-20", "Sep-20","Dec-20"]

plt.bar(x, Santa,  width=width, label='Santa Rosalia')
plt.bar(x1, Loreto, width=width, label='Loreto')
plt.bar(x2, Guaymas, width=width, label='Guaymas')
plt.xticks(x1, string_x)
for a, b in zip(x, Santa):
	plt.text(a, b + 0.1, '%.0f' % b, ha='center', va='bottom', fontsize=7)
for a, b in zip(x1, Loreto):
	plt.text(a, b + 0.1, '%.0f' % b, ha='center', va='bottom', fontsize=7)
for a, b in zip(x2, Guaymas):
	plt.text(a, b + 0.1, '%.0f' % b, ha='center', va='bottom', fontsize=7)
plt.ylabel("Seasonal daily average count of small boats")
plt.legend()
plt.savefig("avg_small.pdf", format="pdf")
plt.show()
