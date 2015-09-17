__author__ = 'TriNguyenDang'
from Homework import *

N = 1000
T = 1000
W_init = 10
p = np.arange(0.3,0.72,0.02)
title = 'Probability of reaching home as a function of p'
p_bankrupt = BetGame.get_p_ReachingHome_multi_p(N,W_init,T,p)

BetGame.multi_Plot(p,p_bankrupt,'blue','o','p bankruptcy','Winning probability', 'Probability reaching home',title)
BetGame.show_plot()

