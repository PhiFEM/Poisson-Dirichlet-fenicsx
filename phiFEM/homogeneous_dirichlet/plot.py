import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

parent_dir = os.path.dirname(__file__)
output_dir = os.path.join(parent_dir, "output")

def plot(df):
    dofs = df["dofs"].values
    h10  = df["H10 error"].values
    l2   = df["L2 error"].values

    a, b = np.polyfit(np.log(dofs[-4:]), np.log(h10[-4:]), 1)
    c, d = np.polyfit(np.log(dofs[-4:]), np.log(l2[-4:]), 1)

    plt.loglog(dofs, h10, "-^", label=f"H10 error")
    plt.loglog(dofs, l2, "-^", label=f"L2 error")
    plt.loglog(dofs[-4:], 0.9*np.exp(b)*dofs[-4:]**a, "--", color='black', label=f"Slope {np.round(a,2)}")
    plt.loglog(dofs[-4:], 0.9*np.exp(d)*dofs[-4:]**c, "--", color='black', label=f"Slope {np.round(c,2)}")

plt.figure()

df = pd.read_csv(os.path.join(output_dir, "results.csv"))
plot(df)

plt.legend()
plt.savefig(os.path.join(output_dir, "plot.pdf"), bbox_inches="tight")