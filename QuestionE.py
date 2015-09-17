__author__ = 'TriNguyenDang'
from Homework import *

N = 10000
W_init = 10
T = 1000
p = 0.44
A = BetGame(N,W_init,T,p)
A.Start()
T_0 = A.get_T_0()
avgT = sum(T_0)/len(T_0)
results, edges = np.histogram(T_0,bins=50, normed=True)
binWidth = edges[1] - edges[0]
plt.bar(edges[:-1], results*binWidth, binWidth)
plt.xlabel('T_0,(avg T_0 ='+str(avgT)+')')
plt.ylabel('pdf')
plt.title('Time to reach home')

plt.show()

