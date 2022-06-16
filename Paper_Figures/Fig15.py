import numpy as np
import matplotlib.pyplot as plt

size = 8
x = np.arange(size)
print(x)
Santa = [0,0,0.38,0.33,0.38,0.22,0.71,0.5]
Loreto = [0,0.33,0.2,0.17,0,0,0.1,0.25]
Guaymas = [25.33,7.67,21.5,9.5,9.2,9.5,8.33,10.75]

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
	plt.text(a, b + 0.1, '%.1f' % b, ha='center', va='bottom', fontsize=7)
for a, b in zip(x1, Loreto):
	plt.text(a, b + 0.1, '%.1f' % b, ha='center', va='bottom', fontsize=7)
for a, b in zip(x2, Guaymas):
	plt.text(a, b + 0.1, '%.1f' % b, ha='center', va='bottom', fontsize=7)
plt.ylabel("Seasonal daily average count of large ships")
plt.legend()
plt.savefig("avg_big.pdf", format="pdf")
plt.show()
