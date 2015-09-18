__author__ = 'TriNguyenDang'
from Homework import *

Run_times = 10000
N = 100
W_init = 10
T = 100
p = 0.55



title = 'Probability of reaching home'
p_bankrupt = BetGame.get_p_ReachingHome_N_Times(Run_times,N,W_init,T,p)

avg = [round(sum(p_bankrupt)/len(p_bankrupt),4)]*Run_times

plt.plot(avg,'ro--',label = 'avg p = '+str(avg[0]))
plt.plot(p_bankrupt,'bo--',label='p bankruptcy')
plt.xlabel('Number of simulations ran')
plt.ylabel('Probability reaching home')
plt.title(title)
plt.grid(True)
plt.legend(loc = 0)
plt.show()
'''
BetGame.multi_Plot(x,p_bankrupt,'blue','o','p bankruptcy','Number of simulations ran','Probability reaching home',title)
BetGame.show_plot()
'''


