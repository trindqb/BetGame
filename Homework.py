__author__ = 'TriNguyenDang'
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli



class Player(object):

    W_init = None # w(0)
    W = None #Wealth history
    E = None #Expected value
    T = None #Maximum turn(times) play_
    p = None #probability win
    T_0 = None #first point broke

    #constructor
    def __init__(self, W_init, T, p):
        self.W_init = W_init
        self.T = T
        self.p = p
        self.W = []

    #history wealth of player
    def Play(self):
        t = 1
        self.W.append(self.W_init)
        while(t <= self.T )and(self.W[t-1]>0):
            self.W.append(self.W[t-1] + 2*bernoulli.rvs(self.p) - 1)
            t+=1
        if(t <= self.T):
            self.T_0 = t-1
        else:
            self.T_0 = 0

    #calculate expected value
    def ExpectedValue(self):
        self.E = np.zeros(self.T + 1)
        self.E = self.W_init
        t = 1
        while(t < self.T):
            self.E[t] = self.E[t-1] + 2*self.p - 1
            t+=1
    #plot
    def Draw_Wealth(self,Color):
        plt.plot(self.W,lw = 2,color = Color, label = 'p='+str(self.p))


    #indexer
    def __getitem__(self, item):
        return self.W[item]


    #definition of operator +
    def __add__(self, other):
        tmp = Player(self.W_init,self.T,self.p)
        M = len(self.W)
        N = len(other.W)
        i = j = 0
        while(i < M)and(j < N):
            tmp.W.append(self[i] + other[j])
            i+=1
            j+=1
        while(j < N):
            tmp.W.append(other[j])
            j+=1
        while(i < M):
            tmp.W.append(self[i])
            i+=1
        return tmp

class BetGame:
    num_Player = None
    list_Player = None
    p_bankrupt = None

    def __init__(self,num_Player,W_init,T,p):
        self.num_Player = num_Player
        self.list_Player = []
        for i in range(num_Player):
            self.list_Player.append(Player(W_init,T,p))

    def Start(self):
        for player in self.list_Player:
            player.Play()

    #get probability bankrupt of  game
    def get_Probability_Bankrupt(self):
        Count = 0.0
        for player in self.list_Player:
            if(player.T_0 != 0):
                Count+=1
        self.p_bankrupt =  Count/self.num_Player
        return self.p_bankrupt


    # get average wealth of all player
    def get_Average(self):
        _sum = Player(self.list_Player[0].W_init,self.list_Player[0].T,self.list_Player[0].p)
        for player in self.list_Player:
            _sum = _sum + player
        for i in range(len(_sum.W)):
            _sum.W[i] = 1.0*_sum.W[i]/self.num_Player
        return _sum

    #plot each player in list_player
    def _Plot(self,Color):
        for player in self.info_Player:
            player.Draw(Color)


    def get_T_0(self):
        T_0 = []
        for player in self.list_Player:
            T_0.append(player.T_0)
        return T_0

    @staticmethod
    #calculate probability reaching home with multiple N = [(N given)..MaxN] exp:N = [50..1000]
    def get_p_ReachingHome_N_Times(Run_times,num_Player,W_init,T,p):
        p_bankrupt = []
        for i in range(Run_times):
            A = BetGame(num_Player,W_init,T,p)
            A.Start()
            p_bankrupt.append(A.get_Probability_Bankrupt())
            num_Player+=10
        return p_bankrupt


    #calculate probability reaching home with multiple initial wealth
    @staticmethod
    def get_p_ReachingHome_multi_initial_W(N, list_W_init, T, p):
        p_bankrupt = []
        for W_init in list_W_init:
            A = BetGame(N,W_init,T,p)
            A.Start()
            p_bankrupt.append(A.get_Probability_Bankrupt())
        return p_bankrupt

    #calculate probability reaching home with multiple probability win
    @staticmethod
    def get_p_ReachingHome_multi_p(N,W_init,T,list_p):
        p_bankrupt = []
        for p in list_p:
            A = BetGame(N,W_init,T,p)
            A.Start()
            p_bankrupt.append(A.get_Probability_Bankrupt())
        return p_bankrupt

    #plot
    @staticmethod
    def multi_Plot(xValue, yValue, Color, Marker, Label, Xlabel, Ylabel, Title):
        plt.plot(xValue, yValue, color = Color, marker = Marker, linewidth = 2, label = Label)
        plt.title(Title)
        plt.xlabel(Xlabel)
        plt.ylabel(Ylabel)


    @staticmethod
    def show_plot():
        plt.grid(True)
        plt.legend(loc = 0)
        plt.show()


















