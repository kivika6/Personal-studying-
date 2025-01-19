import numpy as np

a = np.random.randint(0, +10, size=15)
a[a > 5] # виведення значень більших за х
new_a = a[2:6].copy()  # вирізати підмасив
new_a[0] = 15   # нове значення
