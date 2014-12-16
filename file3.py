'''
Detective AI

Still to do - reaction to turns-----at 10:30AM, sort of done



'''

from testoffile2 import *



class detective():
       
	def __init__(self,turns=0):
	    self.present_square=random_start_square()
	    self.last_known_X=1
	    self.turns=0
	    self.taxi_tickets=10
	    self.bus_tickets=8
	    self.under_tickets=4
       
	def if_valid_move(self):
		if self.taxi_tickets+self.bus_tickets+self.under_tickets==0:
			return 0

	def info(self):
		print self.present_square, self.turns, self.last_known_X


	def process_action(self,mode):
		if mode==0:
		   self.taxi_tickets-=1
		elif mode==1:
		   self.bus_tickets-=1
		else:
		   self.under_tickets-=1   
    
        def choose_action(self):
     
            (ans, target)=shortest_path(self.present_square,self.last_known_X)    
            method=self.move(target[0])
            if method==150:
        	return 0
            else:
        	self.process_action(method)
        	return 1
            #target.pop(0) Don't think this is necessary, since the value of target is recalculated for each turn
            #print target


        def move(self,target):
            play=self.if_valid_move()
            if play!=0:

        	for x,mode in enumerate(modes):
            	    if [self.present_square, target] in mode or [target, self.present_square] in mode:
                	self.present_square=target                 
		    		#How do I find which method of transport was used? ---UPDATE, done
                	self.turns+=1
                	#Insert call to process_action here somewhere-------UPDATE, done
			#print "Done"
			return x

            else:
		return 150

                      
       
    

#first=detective()
#first.info()
#(ans,target)=shortest_path(first.present_square,first.guess_X)
#print ans, target

#first.choose_action()
