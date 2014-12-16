
'''
AI for Mr. X
Assuming 2 detectives

Key points:
1. How to reveal the current location to other detectives
2. Different alpha, beta, (gamma) values for weighting the detectives importance
3. Including double moves (eventually)


'''

from testoffile2 import *
from random import random
from bisect import bisect



class MisterX():
	def __init__(self,turns=0,det1=0,det2=0):
		self.cur_square=random_start_square()
		self.black_tickets=2
		self.turns=0
		self.det1=0
		self.det2=0

	def move(self,target):
            for mode in modes:
                if [self.cur_square, target] in mode or [target, self.cur_square] in mode:
                    self.cur_square=target                 
                    self.turns+=1
	    #print "Done"



#avoid these paths with probability alpha and beta respectively
	def evaluate_best_move(self,alpha,beta,lpath1,lpath2):
	    choice_list=[]
	    prob_list=[]
	    neighburr=neighbors(self.cur_square)
	    x=len(neighburr)
        #    print x
         #   print alpha,beta
	    factor=1/(x-2+alpha+beta)
	    for i,item in enumerate(neighburr):
                #print i,item
                ##print alpha, beta
                #print factor
	    	if item in lpath1:
	    		choice_list.append(alpha*factor)
	    	elif item in lpath2:
	    		choice_list.append(beta*factor)
	    	else:
	    		choice_list.append(factor)
	    choosing_list=[(x,y) for x,y in zip(neighburr,choice_list)]
            
	    self.choose_move(choosing_list)


	def choose_move(self,choice_list):    		
			values, weights=zip(*choice_list)
			total=0
			cumul_weights=[]
			for w in weights:
				total+=w
				cumul_weights.append(total)
			x=random()*total
			i=bisect(cumul_weights, x)
                        #print values[i], type(values[i])			
			self.move(values[i])
    
        def setvalues(self, dist):
		if dist>=1 and dist<=3:
	            return 0.9
		elif dist>3 and dist<=6:
		    return 0.6
		elif dist>6 and dist<=9:	
                    return 0.3
                elif dist>9:
        	    return 0.1

	def check_dists(self,alpha=0,beta=0):
	    (dist_det1, likely_path1)=shortest_path(self.cur_square,self.det1)
	    (dist_det2, likely_path2)=shortest_path(self.cur_square,self.det2)
	    #print "DD1=", dist_det1, type(dist_det1)
	    alpha=self.setvalues(dist_det1)
	    beta=self.setvalues(dist_det2)
	    self.evaluate_best_move(alpha,beta,likely_path1,likely_path2)

	
