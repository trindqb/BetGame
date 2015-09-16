__author__ = 'TriNguyenDang'
from Homework import *


A = BetGame(10000,10,1000,0.44)
A.Start()
plt.plot(A.get_Probability_Bankrupt_T(),'ro-')
plt.show()
