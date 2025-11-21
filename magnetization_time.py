import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numba import jit


@jit
def ising_m(L, T, MCS):
    N = L * L
    mag = []

    board = np.ones((L, L))

    for step in range(MCS):
        for spin in range(N):
            x = np.random.randint(0, L)
            y = np.random.randint(0, L)
            deltaE = 2 * board[x, y] * (
                    board[(x - 1) % L, y] + board[(x + 1) % L, y] + board[x, (y - 1) % L] + board[x, (y + 1) % L])
            if deltaE <= 0:
                board[x, y] = - board[x, y]
            else:
                if np.random.uniform(0, 1) < np.exp(-deltaE / T):
                    board[x, y] = -board[x, y]
        mag.append(np.sum(board) / N)

    return board, mag


@jit
def magnetiz2(L, Ts1, Ts2, Ts3, MCS, markers, colors):
    for l in range(len(L)):
        M = []
        for t in range(len(Ts1)):
            _, data = ising_m(L[l], Ts1[t], MCS)
            M.append(np.mean(np.abs(data[60000:99999])))

        M2 = []
        for j in range(len(Ts2)):
            _, data2 = ising_m(L[l], Ts2[j], MCS)
            M2.append(np.mean(np.abs(data2[60000:99999])))
        M3 = []
        for s in range(len(Ts3)):
            _, data3 = ising_m(L[l], Ts3[s], MCS)
            M3.append(np.mean(np.abs(data3[60000:99999])))

        plt.plot(Ts1, M, marker=markers[l], color=colors[l], label=f'L={L[l]}')
        plt.plot(Ts2, M2, marker=markers[l], color=colors[l])
        plt.plot(Ts3, M3, marker=markers[l], color=colors[l])
    plt.title(" Magnetyzacja jako funkcja temperatury")
    plt.xlabel('T* - zredukowana temperatura')
    plt.ylabel('<m> - magnetyzacja')
    plt.legend(loc="best")
    plt.savefig(f"plots/magnet_time/magnet_po_czasie_dla_MCS={MCS}_3zakresy_ucinane.png", dpi=500)
    plt.show()


L = [10, 20, 40, 80]
Ts = np.arange(0.5, 3.5, 4)
Ts1 = np.arange(0.5, 2.25, 0.25)
Ts2 = np.arange(2, 3.15, 0.05)
Ts3 = np.arange(3.1, 3.75, 0.25)
MCS = 100000
markers = ["o", "d", "v", "X"]
colors = ["#011B01", "#09552F", "#00994C", "#74C69D"]

magnetiz2(L, Ts1, Ts2, Ts3, MCS, markers, colors)
