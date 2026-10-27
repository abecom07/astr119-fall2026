# pixels_starter.py -- an image is an array (Pod 5). Copy this file to pixels.py and work on the copy.
# Run from the repository folder:  python module-3/pixels.py
import numpy as np
from matplotlib.pyplot import imread, imsave

I = imread("module-3/clean_io_small.png")     # rows, columns, 3 colour channels; values 0.0 to 1.0
print(I.size)

J = I.copy()
J[20:40, 20:40, :] = 1.0
J[356, :, :] = 0.0

K = I.copy()
K = 1 - K

L = I.copy()
zoom_array = L[145:245, 145:245, :]
L = np.repeat(zoom_array, 4, axis=0)
L = np.repeat(L, 4, axis=1)

M = I.copy()
center = M[356, 349, :]
x_idx, y_idx = np.indices(M.shape)
dist_from_center = np.sqrt((x_idx - 356) ** 2 + (y_idx - 349) ** 2)
if dist_from_center > 100:
    M = np.random.rand()

imsave("module-3/pixels_out.png", J)
imsave("module-3/pixels_out2.png", K)
imsave("module-3/pixels_out3.png", L)
imsave("module-3/pixels_out4.png", M)
if __name__ == "__main__":
    print("shape:", I.shape)
