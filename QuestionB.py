__author__ = 'TriNguyenDang'
from Homework import *

Run_times = 100
N = 1000
W_init = 10
T = 100
p = 0.55
x = np.arange(1,Run_times+1)
title = 'Probability of reaching home, num_Player = '+str(N)+', T = '+str(T)+', p = '+str(p)+', W_init = '+str(W_init)
p_bankrupt = BetGame.get_p_ReachingHome_N_Times(Run_times,N,W_init,T,p)

avg = [round(sum(p_bankrupt)/len(p_bankrupt),4)]*Run_times
plt.plot(x,avg,'ro-',label = 'avg p = '+str(avg[0]))

BetGame.multi_Plot(x,p_bankrupt,'blue','o','p bankrupt','Number of simulations ran','Probability reaching home',title)
BetGame.show_plot()



