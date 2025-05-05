import matplotlib.pyplot as plt
import numpy as np

# Определяем каждую часть графика
x1 = np.linspace(0, 9, 100)
y1 = (2/27)*x1**2 - 3

x2 = np.linspace(-10, 0, 100)
y2 = 0.04*x2**2 - 3

x3 = np.linspace(-9, -3, 100)
y3 = (2/9)*(x3 + 6)**2 + 1

x4 = np.linspace(-3, 9, 100)
y4 = -(1/12)*(x4 - 3)**2 + 6

x5 = np.linspace(5, 8, 100)
y5 = (1/9)*(x5 - 5)**2 + 2

x6 = np.linspace(8, 5, 100)
y6 = (1/8)*(x6 - 7)**2 + 1.5

x7 = np.linspace(-13, -9, 100)
y7 = -0.75*(x7 + 11)**2 + 6

x8 = np.linspace(-15, -13, 100)
y8 = -0.5*(x8 + 13)**2 + 3

x9 = np.linspace(-15, -10, 100)
y9 = np.ones_like(x9)

x10 = np.linspace(3, 4, 100)
y10 = np.full_like(x10, 3)

# Настройка графика
plt.figure(figsize=(10, 6))
plt.title("Kит")

plt.plot(x1, y1, color='red')
plt.plot(x2, y2, color='green')
plt.plot(x3, y3, color='blue')
plt.plot(x4, y4, color='purple')
plt.plot(x5, y5, color='orange')
plt.plot(x6, y6, color='cyan')
plt.plot(x7, y7, color='brown')
plt.plot(x8, y8, color='magenta')
plt.plot(x9, y9, color='black')
plt.plot(x10, y10, color='gray')

plt.grid(True)
plt.show()
