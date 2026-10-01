import numpy as np

w = np.array([-2, 1, 0])
x = np.array([2, 3, 1])
y = 1

z = np.dot(w, x)

print("wTx truoc cap nhat =", z)

if y * z <= 0:
    print("Mau bi phan lop sai")

    w = w + y * x

    print("w sau cap nhat =", w)

    z = np.dot(w, x)
    print("wTx sau cap nhat =", z)
else:
    print("Mau duoc phan lop dung")