import creategraph
from spuzzle import puzzle
def solve():
	graph=creategraph.buildgraph(puzzle)
	#for key in graph:
		#print key,len(graph[key])
	#print graph[1]
	
	#print creategraph.colored_vertices
	
	ans=[]
	
	c_v=creategraph.colored_vertices
	
	n_colored=len(creategraph.colored_vertices)
	
	while n_colored < 81:
		m=-1
		index=-1
		for i in range(1,82):
			#print 'here'
			check=[]
			if i not in c_v:
				#means not colored
				#find max saturation degree vertex
				for v in graph[i]:
					if v in c_v:
						check.append(c_v[v])
				check=list(set(check))
				#print 'check:',i,check
				#len(check) gives the saturation degree
				if len(check)>m:
					m=len(check)
					index=i
				elif len(check)==m:
					#now find degree of vertex
					if len(graph[i])>len(graph[index]):
						index=i
		
		#print 'in:',index
		if assign_color(index,graph,c_v)==True:
			#print 'yes'
			n_colored=n_colored+1
		
		else:
			#print 'no'
			return False
	
	print 'Solution exists'
	print 'c:',c_v
	return True

def assign_color(index,graph,c_v):
	#check for available colors
	#print 'i:',index
	available_colors=[]
	available_colors=[t for t in range(1,10)]
	for v in graph[index]:
		if v in c_v:
			#print 'c:',c_v[v]
			if c_v[v] in available_colors:
				available_colors.remove(c_v[v])
	#print available_colors
	if len(available_colors)==0:
		#print 'there'
		#the vertex cannot be colored using given vertices
		return false
	else:
		#print 'here'
		c_v[index]=available_colors[0]
		#print c_v
		return True
	
	
	

#solve()
	
	
