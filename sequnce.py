import numpy as np
import time
from PIL import Image

def mandelbrot(c, max_iter=1000):
    z = 0
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return i
    return max_iter

def generate_image(width, height, max_iter=1000):
    image = np.zeros((height, width), dtype=np.uint16)
    for y in range(height):
        for x in range(width):
            # Convert pixel → complexe
            re = (x - width/2) * 4.0 / width
            im = (y - height/2) * 4.0 / width
            c = complex(re, im)
            image[y, x] = mandelbrot(c, max_iter)
    return image

# Test séquentiel
start = time.time()
img = generate_image(1000, 1000)
end = time.time()

print("Temps séquentiel:", end - start, "s")

# Enregistrer l'image
Image.fromarray(img).save("mandelbrot_seq.png")
