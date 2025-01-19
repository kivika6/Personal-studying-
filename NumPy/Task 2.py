import numpy as np

np.random.normal(size=1000, loc=0, scale=1) # loc - середнє, scale - відхилення
np.random.uniform(size=20, low=0, high=10) # масив у певному діапазоні
a = np.random.randint(0,1 +1, size=30)
count = np.unique(a, return_counts=True) # повернення унікальних значень
print(np.asarray(count).T) # перетворення вхідних даних у масив (.T - транспонування)
