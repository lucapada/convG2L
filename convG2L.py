import math
import numpy as np

if __name__ == "__main__":
    while True:
        # X, Y, Z, Xe, Ye, Ze, K, L
        X = float(input("Inserire valore di X: "))
        Y = float(input("Inserire valore di Y: "))
        Z = float(input("Inserire valore di Z: "))
        Xe = float(input("Inserire valore di Xe: "))
        Ye = float(input("Inserire valore di Ye: "))
        Ze = float(input("Inserire valore di Ze: "))
        K = float(input("Inserire valore di K: "))
        L = float(input("Inserire valore di L: "))

        # B = [X;Y;Z]
        B = np.array([X, Y, Z]);
        # O = [Xe;Ye;Ze]
        O = np.array([Xe, Ye, Ze]);

        # Rz = [cos(k)  sin(k) 0]
        #      [-sin(k) cos(k) 0]
        #      [0       0      1]
        Rz = np.array([
            [math.cos(K), -math.sin(K), 0],
            [math.sin(K), math.cos(K), 0],
            [0,0,1]
        ])

        # Ry = [sin(l)  0     -cos(l)]
        #      [0       1     0      ]
        #      [cos(l)  0     sin(l) ]
        Ry = np.array([
            [math.sin(L), 0, math.cos(L)],
            [0, 1, 0],
            [-math.cos(L), 0, math.sin(L)]
        ])

        # C = Rz^ * (Ry^ * B) + O
        # non serve fare la trasposta perché dot lavora per accostamento di righe e non di colonne, quindi è come se avessi trasposto "automaticamente"
        # https://www.andreaminini.com/python/numpy/funzione-dot-numpy-python
        # https://www.andreaminini.com/python/numpy/funzione-transpose-numpy-python
        RzT = Rz #np.transpose(Rz)
        RyT = Ry #np.transpose(Ry)
        C = np.dot(np.dot((B - O), Rz), Ry)

        # stampo matrice C
        print(C)

        if(input("Altro set di dati (S/N)?") == "N"):
            exit()
