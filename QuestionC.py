__author__ = 'TriNguyenDang'
from Homework import *


N = 100
T = 100
p = 0.55
W_init = np.arange(1,21, 1, int)


BetGame.plot_p_RH_W_init(W_init, BetGame.get_p_RH_W_init(N,W_init,T,p))
