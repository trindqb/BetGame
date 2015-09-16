__author__ = 'TriNguyenDang'
from Homework import *

N = 100
T = 1000
W_init = 10
p = np.arange(0.3,0.72,0.02)

BetGame.plot_p_RH_p(p,BetGame.get_p_RH_p(N,W_init,T,p))

