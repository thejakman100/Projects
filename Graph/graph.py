import numpy as np
import matplotlib.pyplot as plt
from sympy.utilities.lambdify import lambdify
from sympy import var
from sympy import sympify


print("What kind of function would you like to graph?")
eq = input()
x = var('x')
expr = sympify(eq)
f = lambdify(x, expr)


def f(x):
    return f


t = np.arange(-10, 10, 0.5)

plt.plot(t, f(t))

plt.show()
