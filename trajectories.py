import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def ising_m(L, T, MCS):
    N = L * L
    m = []

    board = np.random.choice([-1, 1], size=(L, L))

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
        m.append(np.sum(board) / N)
    return m


L = 40
T = 1.7
MCS = 1000
data = pd.DataFrame()

for i in range(1, 11):
    m = ising_m(L, T, MCS)
    data[f"m{i}"] = m

data.to_csv(f"data/trajectory_40x40/traj_L={L}_T={T}_MCS={MCS}.csv", index=False)

plt.figure()
data = pd.read_csv(f"data/trajectory_40x40/traj_L={L}_T={T}_MCS={MCS}.csv")

for i in range(1, 11):
    m = data[f"m{i}"]
    plt.plot(m)

plt.legend([], [], frameon=False)
plt.xlabel("t [MCS]")
plt.ylabel("m")
plt.title(f"Trajektorie dla T={T}, sieć {L}x{L}")
plt.savefig(f"plots/trajectories/board_40x40/traj_L={L}_T={T}_MCS={MCS}.png", dpi=500)
plt.show()
