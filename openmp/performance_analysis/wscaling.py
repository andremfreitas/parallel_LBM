import numpy as np
import matplotlib.pyplot as plt


path1 = 'weak_scaling/ws1'
table1 = np.genfromtxt(path1)

path2 = 'weak_scaling/ws2'
table2 = np.genfromtxt(path2)

path3 = 'weak_scaling/ws3'
table3 = np.genfromtxt(path3)

mlups1 = table1[:,5]
mlups2 = table2[:,5]
mlups3 = table3[:,5]

mlup1_avg = np.average(mlups1[1:])
mlup2_avg = np.average(mlups2[1:])
mlup3_avg = np.average(mlups3[1:])

mlup1_std = np.std(mlups1[1:])
mlup2_std = np.std(mlups2[1:])
mlup3_std = np.std(mlups3[1:])

error1 = mlup1_std/np.sqrt(len(mlups1[1:])-1)
error2 = mlup2_std/np.sqrt(len(mlups2[1:])-1)
error3 = mlup3_std/np.sqrt(len(mlups3[1:])-1)

nthreads = [2,8,32]
mlup = [mlup1_avg, mlup2_avg, mlup3_avg]
error = [error1, error2, error3]
xticks = [2,8,32]


labelsize  = 18 
ticksize   = 16 

plt.figure()
plt.plot(nthreads, mlup, color = 'k', linewidth=3)
plt.tick_params(axis = "both", labelsize = ticksize, length=5)
#plt.scatter(nthreads, mlup, color = 'k')
plt.errorbar(nthreads, mlup, yerr=error, fmt='o', color = 'k',capsize=5,markersize=8)
plt.xlabel(r'$N_{threads}$', fontsize = labelsize)
plt.ylabel(r'Speed $[MLUP/s]$', fontsize = labelsize)
plt.xticks(xticks)
#plt.title('Weak Scaling')
#plt.show()
plt.tight_layout()
plt.savefig('weak_scaling.png')

