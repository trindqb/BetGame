__author__ = 'TriNguyenDang'
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli



class Player(object):

    W_init = None # w(0)
    W = None #Wealth history
    E = None #Expected value
    T = None #Maximum turn(times) play_
    p = None

    #constructor
    def __init__(self, W_init, T, p):
        self.W_init = W_init
        self.T = T
        self.p = p
        self.W = np.zeros(T+1)

    #history wealth of player
    def Play(self):
        t = 1
        self.W[0] = self.W_init
        while(t <= self.T )and(self.W[t-1]>0):
            self.W[t] = self.W[t-1] + 2*bernoulli.rvs(self.p) - 1
            t+=1

    #calculate expected value
    def ExpectedValue(self):
        self.E = np.zeros(self.T + 1)
        self.E = self.W_init
        t = 1
        while(t < self.T):
            self.E[t] = self.E[t-1] + 2*self.p - 1
            t+=1
    #plot
    def Draw(self,Color):
        #x = np.arange(self.T + 1)
        plt.plot(self.W,lw = 2,color = Color, label = 'p='+str(self.p))

    #indexer
    def __getitem__(self, item):
        return self.W[item]


    #definition of operator +
    def __add__(self, other):
        tmp = Player(self.W_init,self.T,self.p)
        for i in range(self.T + 1):
            tmp[i]= self.W[i] + other.W[i]
        return tmp

class BetGame:
    num_Player = None
    info_Player = None
    def __init__(self,num_Player, W_init, T, p):
        self.num_Player = num_Player
        self.info_Player = [Player(W_init,T,p) for i in range(num_Player)]

    def Start(self):
        for player in self.info_Player:
            player.Play()


    def get_Probability_Bankrupt(self):
        Count = 0.0
        for player in self.info_Player:
            if(player[-1]==0):
                Count+=1
        return Count/self.num_Player


    def get_Average(self):
        avg = np.zeros( self.info_Player[0].T + 1)
        for player in self.info_Player:
            for i in range(player.T+1):
                avg[i]+= player[i]/self.num_Player
        return avg

    def Draw(self,Color):
        for player in self.info_Player:
            player.Draw(Color)


    @staticmethod
    #calculate probability reaching home with multiple N = [(N given)..MaxN] exp:N = [50..1000]
    def get_p_RH_N(list_N,W_init,T,p):
        p_bankrupt = []
        for N in list_N:
            A = BetGame(N,W_init,T,p)
            A.Start()
            p_bankrupt.append(A.get_Probability_Bankrupt())
        return list_N,p_bankrupt

    @staticmethod
    #plot probability reaching home with multiple N
    def plot_p_RH_N(Value, N_ran):
        plt.plot(N_ran,Value,'bo--',label = 'p bankrupt')
        avg = [sum(Value)/len(Value) for x in range(len(Value))]
        plt.plot(N_ran,avg,'ro--',label = 'average p ='+str(avg[0]))
        plt.title('Homework 1, question b')
        plt.grid(True)
        plt.xlabel('The number of simulations ran(N)')
        plt.ylabel('Probability of reaching home(Bankruptcy)')
        plt.legend(loc = 0)
        plt.show()

    #calculate probability reaching home with multiple initial wealth
    @staticmethod
    def get_p_RH_W_init(N, list_W_init, T, p):
        p_bankrupt = []
        for W_init in list_W_init:
            A = BetGame(N,W_init,T,p)
            A.Start()
            p_bankrupt.append(A.get_Probability_Bankrupt())
        return p_bankrupt

    @staticmethod
    def plot_p_RH_W_init(list_W_init, p_bankrupt):

        plt.plot(list_W_init,p_bankrupt,'bo-',lw=2,label = 'p bankrupt')
        plt.title('Homework 1, question c')
        plt.grid(True)
        plt.xlabel('Valuation of initial wealth(W_init=[1..20],T=100,N=100,p=0.55)')
        plt.ylabel('Probability of reaching home(Bankruptcy)')
        plt.legend(loc = 0)
        plt.show()

    #calculate probability reaching home with multiple probability win
    @staticmethod
    def get_p_RH_p(N,W_init,T,list_p):
        p_bankrupt = []
        for p in list_p:
            A = BetGame(N,W_init,T,p)
            A.Start()
            p_bankrupt.append(A.get_Probability_Bankrupt())
        return p_bankrupt

    @staticmethod
    def plot_p_RH_p(list_p, p_bankrupt):
        plt.plot(list_p,p_bankrupt,'bo-',lw = 2,label = 'p bankrupt')
        plt.title('Homework 1, question d')
        plt.grid(True)
        plt.xlabel('Valuation of p win(W_init = 10 ,T = 1000, N=100, p=[0.3:0.7 ,step= 0.02])')
        plt.ylabel('Probability of reaching home(Bankruptcy)')
        plt.legend(loc = 0)
        plt.show()















