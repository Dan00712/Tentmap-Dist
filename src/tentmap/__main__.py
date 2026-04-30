import argparse
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

import tentmap.dist as d

parser = argparse.ArgumentParser(
        prog="Tentmap Distribution",
        )
parser.add_argument("outfile", type=Path)
args = parser.parse_args()

x0s = np.linspace(0, 1, 120)
As = np.linspace(1, 2, 150)
N = 200

data = d.get_data_anal(
        x0s = x0s,
        As = As,
        N=N
).T # [XCount, AValue]

masked_data = np.ma.masked_where(data == 0, data)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6), constrained_layout=True)

ax1.imshow(masked_data, aspect='auto',
           extent=[As[0], As[-1], x0s[0], x0s[-1]]
)
ax1.set_xlabel("A")
ax1.set_ylabel("x")


for i in [10, -3]:
    A = As[i]
    dist = data[:, i]
    ax2.plot(x0s[3:], dist[3:], label=f"A={round(A, ndigits=2)}")
ax2.set_ylabel("p(x)")
ax2.set_xlabel("x")
ax2.legend()

plt.savefig(args.outfile)
