from file1 import *
from collections import deque
import copy
import itertools
import random
# important functions:
#
# 1.nearest underground,bus,black  ----------------done except black ticket
#    Recycle this square and find shortest path to it
# 
# 2. include distance in node class ------------Done
#
# 3. now for the actual path--------done
#

class Node:
	def __init__(self,locn,dist,transport=None):
		self.locn=locn
		self.adjacentNodes=neighbors(self.locn,transport)
                self.dist=dist
#		print self.dist
		#print(self.adjacentNodes)


def random_start_square():
	return random.randint(1,200)


def findpath(vispath, locnvalue, dist):
   news=[]
   news.append(locnvalue)
   vpath=vispath
  # print "vpath ="
  # print vpath
   index=len(vpath)-1
   pathfunction(vpath, index, locnvalue, news)
   #Make a function such that when you call it on this it checks commonality with modes and returns the value of x for which you coincide and you provide the index, the value and the list itself
#   print locnvalue, news[::-1]
   return news[::-1]



#Currently returns a semi-accurate path but not the whole path. Also does some weird shit with the pathing. It makes sense to travel by underground the best but still
# As of 23:45, 11/14
def pathfunction(vis_path, index, value,path):
    for x,y in itertools.product(range(1,index),modes):
         # print type(vis_path[x])
          if [vis_path[x], value] in y or [value,vis_path[x]] in y :
             if vis_path[x] not in path:
 #               print vis_path[x],"index= ",x
                path.append(vis_path[x])
                token=vis_path[x]
                return  pathfunction(vis_path, x-1, vis_path[x], path)
           


#process needs to remove all square brackets, all occurrences of cur_locn and extra commas
def process(target,cur_locn):
	ans=sum(target,[])
	ret=[item for item in ans if item!=cur_locn]
	return ret

def remove_all(val,item):
	return [value for value in list if value!=val]


def direct(cur_locn,transport):0
	stop=[stops for stops in transport if cur_locn in stops]
	return stop


#Returns list of neighbors
def neighbors(cur_locn, transport=None):
	 nayburr=[]
	 temp=[]
	 if transport==None:
	 	i=0
	 	for mode in modes:
	 		stop=direct(cur_locn,mode)
		 	if stop:
		 		temp=temp+stop
		nayburr=process(temp,cur_locn) 		
	 else:
	 	stop=direct(cur_locn,transport)		
	 	
	 	nayburr=process(stop,cur_locn)
	 	
	 #print nayburr
	 return nayburr 

#Worksfine2:30PM Sunday
def nearest_transport(cur_locn,transport):
  
#uN saves us the visiting and scanning time on seen nodes
   uselessNodes = set()
   cur=Node(cur_locn,0)
   queue = deque([cur])
   trans=sum(transport,[])   
   while len(queue) > 0:
      node = queue.pop()
      #print node.locn
      if node.locn in uselessNodes:
         continue
      #print type(visitedNodes)
      #print node.locn
      if node.locn in trans:
            return node.locn
      uselessNodes.add(node.locn)
      
      
      for n in node.adjacentNodes:
      	 if n not in uselessNodes:
	    newnode=Node(n,0)
            queue.appendleft(newnode)
     

#works fine 2:30PM Sunday
def shortest_path(cur_locn,target_locn,transport=None):
   visitedNodes = []
   cur=Node(cur_locn,0,transport)
   queue = deque([cur])
   count=0
   tag=1
   queue1=copy.deepcopy(queue)
   path_list=[]
   while len(queue) > 0:
      #print len(queue), len(queue1) 
      node = queue.pop()
      queue1.pop()
      if len(queue1)==0:
         count=count+1
         tag=0
         queue1=queue
      #print type(node)
      if node.locn in visitedNodes:
         continue
      #print type(visitedNodes)
      visitedNodes.append(node.locn)
      if node.locn == target_locn:
	 path_list=findpath(visitedNodes,node.locn,count)
         #print path_list
	 
         return count, path_list

      
      for n in node.adjacentNodes:
      	 if n not in visitedNodes:
            
	    newnode=Node(n,count,transport)
	    #print "count=", count
	    #print "newnode.dist=", newnode.dist
            queue.appendleft(newnode)
      if tag==0:
      	queue1=copy.deepcopy(queue)
        tag=1
   return False, []
			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   


#neighbors(100)	 
#ans=shortest_path(37,198)
#print "ans is", ans
