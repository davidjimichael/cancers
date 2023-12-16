import numpy as np

a = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.matrix([[1, 2, 3], [5, 6, 7], [9, 10, 11], [21, 22, 23]])
a1 = np.matrix([[4, 5, 6], [7, 8, 9], [10, 11, 12]])
b1 = np.matrix([[5, 6, 7], [9, 10, 11], [21, 22, 23]])
print(a)
print(b)
c = np.dot(a, b.transpose())
d = np.cross(b1,  a1.transpose())


def function_name():
    print(c)
    print(d)
