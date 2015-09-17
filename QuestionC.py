__author__ = 'TriNguyenDang'
from Homework import *


N = 1000
T = 100
p = 0.55
W_init = np.arange(1,21, 1, int)
title = 'Probability of reaching home as a function of initial wealth'
p_bankrupt = BetGame.get_p_ReachingHome_multi_initial_W(N,W_init,T,p)
BetGame.multi_Plot(W_init, p_bankrupt, 'blue', 'o', 'p bankruptcy', 'Initial wealth', 'Probability reaching home',title)
BetGame.show_plot()




