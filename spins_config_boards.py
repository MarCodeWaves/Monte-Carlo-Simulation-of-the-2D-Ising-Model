import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

color1 = '#033328'
color2 = '#FCEBC2'
cmap_colors = [color1, color2]
cmap = LinearSegmentedColormap.from_list('custom_cmap', cmap_colors, N=2)


def ising_spins(L, T, MCS, period, folder, subfolder, random=False):
    kB = 1
    J = 1
    N = L * L
    if random:
        board = np.random.choice([-1, 1], size=(L, L))
    else:
        board = np.ones((L,L))

    data = pd.DataFrame(board)
    data.to_csv(f"data/board_10x10/siec_L={L}_T={T}_MCS=0.csv", index=False)

    #data.to_csv(f"data/gifs_{L}X{L}/siec_L={L}_T={T}_MCS=0.csv", index=False)
    plt.figure(figsize=(6,6))
    plt.imshow(board, cmap=cmap, extent=[0, L, 0, L], origin="lower")

    # plt.title(f'Symulacja konfiguracji spinów dla sieci {L}x{L}, T={T} ', y=1.05)
    plt.title(f'MCS=0 ', y=1.05, fontsize=20, fontweight="bold")

    #plt.savefig(f"plots/spins_config_for_gifs/{folder}/{subfolder}/sym_MC=0_T={T}.png", dpi=500)
    plt.savefig(f"plots/spins_config/{folder}/{subfolder}/sym_0_T_{T}.png", dpi=500)
    plt.show()

    for step in range(1, MCS + 1):
        for spin in range(N):
            i = np.random.randint(0, L)
            j = np.random.randint(0, L)
            deltaE = 2 * J * board[j, i] * (
                    board[j, (i - 1) % L] + board[j, (i + 1) % L] + board[(j - 1) % L, i] + board[(j + 1) % L, i])
            if deltaE <= 0:
                board[j, i] = -board[j, i]

            else:
                if np.random.uniform(0, 1) < np.exp(-deltaE / (kB * T)):
                    board[j, i] = -board[j, i]

        if step % period == 0:
            data = pd.DataFrame(board)
            data.to_csv(f"data/{folder}/siec_L={L}_T={T}_MCS={step}.csv", index=False)
           # data.to_csv(f"data/gifs_{L}X{L}/siec_L={L}_T={T}_MCS={step}.csv", index=False)
            plt.figure(figsize=(6, 6))
            plt.imshow(board, cmap=cmap, extent=[0, L, 0, L], origin="lower")

            plt.title(f'MCS={step} ', y =1.05, fontsize=20, fontweight="bold")
            # plt.title(f'Symulacja konfiguracji spinów dla sieci {L}x{L}, T={T} ', y=1.05)

            plt.savefig(f'plots/spins_config/{folder}/{subfolder}/sym_{step}_T_{T}.png', dpi=500)
            #plt.savefig(f'plots/spins_config_for_gifs/{folder}/{subfolder}/sym_MC={step}_T={T}.png', dpi=500)
            plt.show()


#ising_spins(10, 1, 300, 10, "board_10x10", "T1", True)
#ising_spins(10, 2.27, 100, 10, "board_10x10", "T2", True)
#ising_spins(10, 4, 100, 10, "board_10x10", "T3", True)

#ising_spins(80, 1, 100, 25, "board_80x80", "T1")
#ising_spins(80, 2.27, 100, 25, "board_80x80", "T2")
#ising_spins(80, 4, 100, 25, "board_80x80", "T3")

# pod gify
#ising_spins(10, 1, 100, 10, "10x10", "T1")
#ising_spins(10, 2.27, 100, 10, "10x10", "T2")
#ising_spins(10, 4, 100, 10, "10x10", "T3")

#ising_spins(80, 1, 150, 10, "80x80", "T1")
#ising_spins(80, 2.27, 150, 10, "80x80", "T2")
#ising_spins(80, 4, 100, 10, "80x80", "T3")
