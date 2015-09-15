__author__ = 'TriNguyenDang'
from Homework import *

player1 = Player(W_init=20,T=1000,p=0.25)
player2 = Player(W_init=20,T=1000,p=0.55)
player3 = Player(W_init=20,T=1000,p=0.75)

player1.Play()
player2.Play()
player3.Play()

player1.Draw('red')
player2.Draw('blue')
player3.Draw('purple')

plt.title('Homework 1, question a')
plt.legend(loc = 0)
plt.grid(True)
plt.xlabel('bet time(t)')
plt.ylabel('Wealth(in $)')
plt.show()