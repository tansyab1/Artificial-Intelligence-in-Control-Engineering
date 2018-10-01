#------------------------------------------------------------------------------
#	Libraries
#------------------------------------------------------------------------------
import numpy as np 

#------------------------------------------------------------------------------
#	Function represents the process model
#------------------------------------------------------------------------------
def random_index(W):
	"""
	[Arguments]
		W : (list) List of important factors.

	[Return]
		idx : (int) Random index based on the given distribution of W.
	"""
	total = np.sum(W) 
	size = len(W)  
	p = W/total 
	return np.random.choice(size, 1, p=p)[0] 

#------------------------------------------------------------------------------
#	Test bench to verify the written function
#------------------------------------------------------------------------------
x = [10,1,3,4,5,5,5,5,5,6,6,7,7,7,3,9] 
total = np.sum(x) 
p = x/total
print(p) 
y = [] 
for i in range(100):
	y.append(random_index(x)) 
_, count = np.unique(y, return_counts=True)
total = np.sum(count) 
p = count/total
print(p) 