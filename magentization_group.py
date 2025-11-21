import numpy as np
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


# usrednianie po czasie bez ucinania/z ucinaniem
@jit
def magnetiz_group(L, Ts, MCS, markers, colors):
    for l in range(len(L)):
        index = L[l]
        M1 = np.zeros(len(Ts))

        for t1 in range(len(Ts)):
            index_T1 = Ts[t1]
            trajectory1 = np.zeros(100)
            for k1 in range(100):
                _, data1 = ising_m(index, index_T1, MCS)
                trajectory1[k1] = data1[-1]
            M1[t1] = np.mean(np.abs(trajectory1))
        plt.plot(Ts, M1, marker=markers[l], color=colors[l], label=f'L={L[l]}')

    plt.title(" Magnetyzacja jako funkcja temperatury")
    plt.xlabel('T* - zredukowana temperatura')
    plt.ylabel('<m> - magnetyzacja')
    plt.legend(loc="best")
    plt.savefig(f"plots/magnet_group/magnet_po_zespole_dla_MCS={MCS}.png", dpi=500)
    plt.show()


L = [10, 20, 40, 80]

Ts = np.arange(0.5, 3.6, 0.1)
Ts1 = np.arange(0.5, 2.25, 0.25)
Ts2 = np.arange(2, 3.15, 0.05)
Ts3 = np.arange(3.1, 3.75, 0.25)
MCS = 25000
markers = ["o", "d", "v", "X"]
colors = ["#011B01", "#09552F", "#00994C", "#74C69D"]
magnetiz_group(L, Ts, MCS, markers, colors)
