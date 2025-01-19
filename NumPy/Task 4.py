# Математичні операції
import numpy as np

a = np.ones(12, dtype=int)
b = np.random.randint(1, 10, size=12)
addition = a + b
subtraction = a - b
mult = a * b
split = a // b
np.dot(a, b) # скалярний добуток
np.matmul(a, b) # матричний добуток (краще використовувати для декільковимірних масивів)
np.sin(a) # синус

