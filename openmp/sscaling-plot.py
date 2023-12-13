# Plot for strong scaling
from matplotlib import pyplot as plt
import numpy as np

case = "output/nx64_ny64_nz64"

nx = ny = nz = 64

data = np.loadtxt(case + ".txt", usecols=(2,5,9)) # Get data for time, speed and thread number

nthr  = np.unique(data[:,2])

s0 = []
s1 = []
s2 = []
s3 = []
s4 = []

for i in range(data.shape[0]):
    if   data[i,2] == nthr[0]:
        s0.append(data[i,1])
        
    elif data[i,2] == nthr[1]:
        s1.append(data[i,1])
        
    elif data[i,2] == nthr[2]:
        s2.append(data[i,1])
        
    elif data[i,2] == nthr[3]:
        s3.append(data[i,1])
        
    elif data[i,2] == nthr[4]:
        s4.append(data[i,1])

speed    = np.array([
    np.average(s0[1:]),
    np.average(s1[1:]),
    np.average(s2[1:]),
    np.average(s3[1:]),
    np.average(s4[1:])
])

speed_err = np.array([
    np.std(s0[1:])/np.sqrt(len(s0[1:])-1),
    np.std(s1[1:])/np.sqrt(len(s1[1:])-1),
    np.std(s2[1:])/np.sqrt(len(s2[1:])-1),
    np.std(s3[1:])/np.sqrt(len(s3[1:])-1),
    np.std(s4[1:])/np.sqrt(len(s4[1:])-1)
])

# LaTeX font selection
plt.rcParams.update({
    "font.family": "STIXGeneral",
})

# Common plot params
figsize = (10,10)
labelsize  = 18 + 7
titlesize  = 20 + 7
legendsize = 16 + 7
ticksize   = 16 + 7

xticks = [1,2,4,8,16]

plotname = case + ".pdf"

fig, ax = plt.subplots(figsize=figsize)

# ax.plot(nthr, speed, "s", c="tab:purple")
ax.errorbar(nthr, speed, speed_err, elinewidth=3, fmt=".-", label=r"64x64x64 Grid", c="tab:purple", linewidth=3,capsize=4,markersize=4 )
# ax.errorbar(nthr, speed, speed_err, elinewidth=7, fmt=".", label=r"64x64x64 Grid", c="tab:purple", linewidth=7,capsize=8,markersize=4 )

ax.set_xticks(xticks)
ax.tick_params(axis = "both", labelsize = ticksize, length=5)
ax.set_ylabel(r"Speed [MLUP/s]", fontsize = labelsize)
ax.set_xlabel(r"$N_{\mathrm{threads}}$", fontsize = labelsize)
# ax.set_title("Strong scaling", fontsize = titlesize)

ax.legend(fontsize = legendsize, frameon=False)

plt.show()
fig.savefig(plotname, bbox_inches='tight', facecolor=fig.get_facecolor())
