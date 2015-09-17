__author__ = 'TriNguyenDang'
from Homework import *


A = BetGame(10000,10,1000,0.44)
A.Start()
T_0 = A.get_T_0()
plt.hist(T_0,25,label = 'T_0 = '+str(round(1.0*sum(T_0)/len(T_0),0)))
plt.legend()
plt.show()
