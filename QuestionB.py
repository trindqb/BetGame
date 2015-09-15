__author__ = 'TriNguyenDang'
from Homework import *


list_N,list_p = BetGame.p_ReachingHome(2,1000,10,100,0.55)
BetGame.Plot_p_ReachingHome(list_p,list_N)