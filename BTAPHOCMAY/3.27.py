import numpy as np

w = np.array([1, 2, -10])
x = np.array([3, 4, 1])

z = np.dot(w, x)

if z >= 0:
    y_pred = 1
else:
    y_pred = -1

print("wTx =", z)
print("Nhan du doan =", y_pred)

y = -1

if y_pred != y:
    print("Phan lop sai")
else:
    print("Phan lop dung")