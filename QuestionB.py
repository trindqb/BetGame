__author__ = 'TriNguyenDang'
from Homework import *

N = np.arange(2,2001,1,int)
W_init = 10
T = 100
p = 0.55

BetGame.plot_p_RH_N(BetGame.get_p_RH_N(N,W_init,T,p),N)