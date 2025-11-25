import numpy as np
import time
import matplotlib.pyplot as plt
from multiprocessing import Pool
from PIL import Image

# -------------------------
# Mandelbrot (pixel)
# -------------------------
def mandelbrot(c, max_iter=1000):
    z = 0
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return i
    return max_iter

# -------------------------
# Calcul d'une ligne
# -------------------------
def compute_row(args):
    y, width, height, max_iter = args
    row = np.zeros(width, dtype=np.uint16)
    for x in range(width):
        re = (x - width/2) * 4.0 / width
        im = (y - height/2) * 4.0 / width
        c = complex(re, im)
        row[x] = mandelbrot(c, max_iter)
    return y, row

# -------------------------
# Version parallèle
# -------------------------
def generate_parallel(width, height, n_processes=4, max_iter=1000):
    args = [(y, width, height, max_iter) for y in range(height)]

    with Pool(n_processes) as p:
        results = p.map(compute_row, args)

    image = np.zeros((height, width), dtype=np.uint16)
    for y, row in results:
        image[y] = row
    return image

# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    width = 600
    height = 600

    # --- Temps séquentiel ---
    print("Calcul séquentiel...")
    t0 = time.time()
    img_seq = generate_parallel(width, height, 1)
    t_seq = time.time() - t0
    print(f"Tseq = {t_seq:.3f}s")

    Ns = [1, 2, 4, 8]
    times = []

    for n in Ns:
        print(f"{n} process...")
        t0 = time.time()
        img = generate_parallel(width, height, n)
        t = time.time() - t0
        times.append(t)
        Image.fromarray(img).save(f"mandelbrot_{n}.png")

    # --- Speedup & efficacité ---
    speedup = [t_seq / t for t in times]
    efficiency = [speedup[i] / Ns[i] for i in range(len(Ns))]

    # --- Courbe théorique Amdahl ---
    p = 0.815  # trouvé expérimentalement
    amdahl = [1 / ((1-p) + p/n) for n in Ns]

    # --- Graphique Speedup ---
    plt.figure()
    plt.plot(Ns, speedup, marker='o', label="Speedup mesuré")
    plt.plot(Ns, amdahl, linestyle="--", label="Amdahl théorique")
    plt.xlabel("Nombre de processus")
    plt.ylabel("Speedup")
    plt.grid(True)
    plt.legend()
    plt.savefig("speedup.png")

    # --- Graphique efficacité ---
    plt.figure()
    plt.plot(Ns, efficiency, marker='o')
    plt.xlabel("Nombre de processus")
    plt.ylabel("Efficacité")
    plt.grid(True)
    plt.savefig("efficiency.png")

    print("Graphiques générés : speedup.png & efficiency.png")
