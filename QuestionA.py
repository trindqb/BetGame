__author__ = 'TriNguyenDang'
from Homework import *


A = Player(W_init = 20, T = 1000, p = 0.25)
A.Play()
A.Draw_Wealth('red')

B = Player(W_init = 20, T = 1000, p = 0.55)
B.Play()
B.Draw_Wealth('blue')

C = Player(W_init = 20, T = 1000, p = 0.75)
C.Play()
C.Draw_Wealth('green')

plt.title('Simulation of a process realization')
plt.xlabel('Time(t)')
plt.ylabel('Wealth($)')
plt.grid(True)
plt.legend(loc =0)
plt.show()

A = BetGame(100,20,1000,0.25)
B = BetGame(100,20,1000,0.55)
C = BetGame(100,20,1000,0.75)
A.Start()
B.Start()
C.Start()
a = A.get_Average()
b = B.get_Average()
c = C.get_Average()
a.Draw_Wealth('red')
b.Draw_Wealth('blue')
c.Draw_Wealth('green')

plt.title('Simulation of average process')
plt.xlabel('Time(t)')
plt.ylabel('Wealth($)')
plt.grid(True)
plt.legend(loc =0)
plt.show()