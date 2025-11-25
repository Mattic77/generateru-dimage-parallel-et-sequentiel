Génération de l’ensemble de Mandelbrot et analyse de performance avec la loi d’Amdahl

Ce projet consiste à générer une image de la fractale de Mandelbrot en Python et à analyser les performances d’une version séquentielle et d’une version parallèle implémentée avec le module multiprocessing.

L’objectif principal est d’étudier l’impact du parallélisme sur les performances réelles et de comparer les résultats obtenus avec les prédictions de la loi d’Amdahl.

🔥 Contenu du projet

Implémentation séquentielle du calcul de Mandelbrot

Implémentation parallèle basée sur un découpage de l’image en lignes

Mesures de temps d’exécution pour différents nombres de processus (1, 2, 4, 8)

Calcul automatique du speedup et de l’efficacité

Génération de deux graphes :

speedup.png

efficiency.png

Application de la loi d’Amdahl pour estimer la partie non parallélisable du programme

📊 Résultats principaux

Les tests montrent que :

Le speedup réel est limité (≈ 2× maximal)

L’efficacité chute rapidement à mesure que le nombre de processus augmente

La surcharge du module multiprocessing (création des processus, IPC, sérialisation…) représente une grande partie du temps total

Ces résultats confirment les prédictions de la loi d’Amdahl, qui souligne que même un problème théoriquement parallélisable reste limité par les parties séquentielles et par les surcharges du système.

🛠️ Technologies utilisées

Python 3

NumPy

Matplotlib

PIL (Pillow)

Multiprocessing
