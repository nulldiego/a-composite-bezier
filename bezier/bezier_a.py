import matplotlib.pyplot as plt
import numpy as np

def B(coorArr, i, j, t):
    if j == 0:
        return coorArr[i]
    return (B(coorArr, i, j - 1, t)*(1 - t) 
        + B(coorArr, i + 1, j - 1, t)*t)

P = np.array([
    [[2.5, 10.], [4., 12.], [6., 12.]], 
    [[6., 12.], [8., 12.], [9., 10.]], 
    [[9., 10.], [10., 8.], [10., 6.]],
    [[10., 6.], [8., 7.], [6., 7.]], 
    [[6., 7.], [4., 7.], [2., 6.]], 
    [[2., 6.], [0.5, 5.], [0.5, 4.]],
    [[0.5, 4.], [0.5, 3.], [1.25, 1.25], [2., 1.]], 
    [[2., 1.], [3., 0.5], [5., 0.5], [6., 0.65]],
    [[6., 0.65], [7., 0.8], [9., 2.], [10., 3.]],
    [[10., 3.], [10., 4.5], [10., 6.]],
    [[10., 6.], [10., 4.5], [10., 3.]],
    [[10., 3.], [10., 1.], [11., 1.], [13., 1.]]])

fig = plt.figure(1)
for k in range(0, P.size):
    x = [item[0] for item in P[k]]
    y = [item[1] for item in P[k]]
    n = len(x)
    xb = []; yb = []
    for t in np.linspace (0., 1., 25):
        a = B(x, 0, n - 1, t)
        b = B(y, 0, n - 1, t)
        xb.append(a)
        yb.append(b)
    plt.plot(xb, yb)

xs = [item[0] for item in P for item in item]
ys = [item[1] for item in P for item in item]
plt.plot(xs, ys, 'c--', xs, ys, 'ko', ms = 8)
plt.show()