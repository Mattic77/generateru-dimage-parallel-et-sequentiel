import numpy as np
import time
from multiprocessing import Pool
from PIL import Image

def mandelbrot(c, max_iter=1000):
    z = 0
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return i
    return max_iter

def compute_row(args):
    y, width, height, max_iter = args
    row = np.zeros(width, dtype=np.uint16)
    for x in range(width):
        re = (x - width/2) * 4.0 / width
        im = (y - height/2) * 4.0 / width
        c = complex(re, im)
        row[x] = mandelbrot(c, max_iter)
    return y, row

def generate_parallel(width, height, n_processes=4, max_iter=1000):
    args = [(y, width, height, max_iter) for y in range(height)]

    with Pool(n_processes) as p:
        results = p.map(compute_row, args)

    image = np.zeros((height, width), dtype=np.uint16)
    for y, row in results:
        image[y] = row

    return image

# ======================================
# IMPORTANT : NE PAS OUBLIER CE BLOC
# ======================================
if __name__ == "__main__":
    width = 600
    height = 600

    for n in [1, 2, 4, 8]:
        start = time.time()
        img = generate_parallel(width, height, n)
        end = time.time()
        print(f"{n} processes → temps = {end - start:.3f}s")

        Image.fromarray(img).save(f"mandelbrot_{n}.png")
        print(f"Image enregistrée : mandelbrot_{n}.png")
