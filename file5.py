from file3 import *
from file4 import *


'''
Evaluate Game Board File

1)Instantiate a MisterX and two Detectives
2)Reveal each of them to the others, and start guessing
3)Iterate through each player in turn and increment turns after that
4)Test the game over condition every turn

'''

class Game_Board:
	def __init__(self,players=2):
            self.players=players
	    self.turn=0
	    self.MrX=MisterX(0)
	    self.Det1=detective(0)
	    self.Det2=detective(0)
	    self.GameOver=0


	def Play(self):
	    while self.GameOver==0:
	       self.turn=self.turn+1
               print "On turn number: %d" %self.turn
	       self.MrX.det1=self.Det1.present_square
	       self.MrX.det2=self.Det2.present_square
               print "Mr.X is on %d" %self.MrX.cur_square
               
	       #print self.MrX.det1, self.MrX.det2
	       if self.turn in [3,8,13,18]:
	           self.Det1.last_known_X=self.MrX.cur_square
	           self.Det2.last_known_X=self.MrX.cur_square
	       self.MrX.check_dists()
               print "Mr.X moves to %d" %self.MrX.cur_square
#Insert function for detective one
               chk1=self.Det1.choose_action()
               if self.MrX.cur_square==self.Det1.present_square:
                   print "Detective 1 got him"
                   print "Detective 1 is on %d, Detective 2 is on %d, and they think Mr.X is on %d\n" %(self.Det1.present_square,self.Det2.present_square, self.Det1.last_known_X)
                   break
                   self.GameOver=2
#Insert function for detective two	      
               chk2=self.Det2.choose_action()
               if self.MrX.cur_square==self.Det2.present_square:
                   print "Detective 1 is on %d, Detective 2 is on %d, and they think Mr.X is on %d\n" %(self.Det1.present_square,self.Det2.present_square, self.Det1.last_known_X)
                   print "Detective 2 got him"
                   break  
                   self.GameOver=2	
               if (chk1+chk2)==0 or self.turn==23:
                   print "Detective 1 is on %d, Detective 2 is on %d, and they think Mr.X is on %d\n" %(self.Det1.present_square,self.Det2.present_square, self.Det1.last_known_X)
                   print "Mr.X slipped away"
                   break
                   self.GameOver=1
               print "Detective 1 is on %d, Detective 2 is on %d, and they think Mr.X is on %d\n" %(self.Det1.present_square,self.Det2.present_square, self.Det1.last_known_X)    
            self.print_result(self.GameOver)
        

        def print_result(self,GameOver):
    	    if GameOver==1:
    		print "Mr.X wins!"
    	    elif GameOver==2:
    	        print "Detectives Win!"
    	    return    	

   
Board=Game_Board()
Board.Play()

