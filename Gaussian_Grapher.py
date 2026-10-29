import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
import math

# The Probability density function
def Probability_Density(X, DEVIATION, MEAN, M_DENOM):
    return (np.exp(-0.5 * ((X - MEAN) / DEVIATION) ** 2) * M_DENOM)

MEAN = float(input("Enter the mean of your distribution: "))
INEQ = input("Enter 'LEFT' if you want to evaluate the <= probability or 'RIGHT' for evaluating the >= probability: ")
DEVIATION = float(input("Enter the standard deviation of your distribution: "))
SOME_CONST = 1 / (np.sqrt(2) * DEVIATION); PI2_INVERSE = 1 / np.sqrt(np.pi)
UP_LIM = float(input("Enter the upper limit of your probability evaluation: "))

RANGE = 50.0
START = MEAN - RANGE

U = (UP_LIM - MEAN) * SOME_CONST
n, term, sum = 0, U, 0
while abs(term) >= 1e-6:
    sum += term
    n += 1
    TEMP_CONST = 2 * n + 1
    term = (-1 if n & 1 == 1 else 1) * (U ** TEMP_CONST) / (math.factorial(n) * TEMP_CONST)

sum = sum * PI2_INVERSE + 0.5
if (INEQ == "RIGHT"):
    sum = 1 - sum
if (INEQ == "LEFT" or INEQ == "RIGHT"):
    print(f"There is a {sum * 100}% chance that your desired event will happen")

X = np.linspace(START, MEAN + RANGE, int(RANGE) * 5)
Y = Probability_Density(X, DEVIATION, MEAN, SOME_CONST * PI2_INVERSE)

plt.plot(X, Y, label=r'$\frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{1}{2} (\frac{x - \mu}{\sigma})^2}$', color='blue', linewidth=2)
plt.fill_between(X, Y, where=(X >= START) & (X <= UP_LIM), color='darkblue', alpha=0.5, label="Probability")

plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.title("Gaussian Distribution", fontsize=14)
plt.xlabel("X", fontsize=12)
plt.ylabel("Probability Density", fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)

plt.show()