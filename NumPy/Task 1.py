import numpy as np

a = np.empty(11, dtype=int)
a.mean()  # середнє значення
np.median(a)  # медіана масиву
a.std()  # середнє відхилення
a.max()
a.min()

b = np.empty((2, 5), dtype=int)
b.mean()
b.std()
np.median(b, axis=0)
np.median(b, axis=1)
b.max(axis=0)  # пошук максимуму за стовпцями
b.min(axis=0)
b.max(axis=1)
b.min(axis=1)  # пошук мінімуму за рядками

a2 = a[np.newaxis, :]  # перетворення в двовимірний
np.transpose(a2)  # транспонування
