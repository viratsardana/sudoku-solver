def buildgraph(puzzle):
	graph={}
	
	for i in range(1,82):
		graph[i]=[]
	
	same_row=[1,2,3,4,5,6,7,8,9]
	same_col=[1,10,19,28,37,46,55,64,73]
	same_block=[1,2,3,10,11,12,19,20,21]
	
	diff_block=[]
	diff_block.append(same_block)
	
	starting=[4,7,28,31,34,55,58,61]
	
	for num in starting:
		te=same_block[:]
		diff=num-1
		te=[x+diff for x in same_block]
		diff_block.append(te)

	row=0
	
	for i in range(1,82):
		te=[]
		te=[9*row+x for x in same_row]
		#print te
		graph=add_edge(graph,i,te)
		graph=add_edge(graph,i,same_col)
		
		for block in diff_block:
			if i in block:
					graph=add_edge(graph,i,block)
		if i%9==0:
			row=row+1
	
	
	
	#for key in graph:
		#print key,len(graph[key])
	
	graph=add_edges_color(graph,puzzle)
	
	return graph
	


def add_edge(graph,vertex,same_something):
	temp=same_something[:]
	if vertex in temp:
		for num in temp:
			if num!=vertex:
				if num not in graph[vertex]:
					graph[vertex].append(num)
					if vertex not in graph[num]:
						graph[num].append(vertex)
	else:
		
		diff=vertex-1
		
		index=0
		
		for j in range(0,len(temp)):
			if temp[j]+diff<=81:
				temp[j]=temp[j]+diff
			else:
				break
			index=index+1
		
		li=temp[:index]
		
		if vertex in li:
			for num in li:
				if num!=vertex:
					if num not in graph[vertex]:
						graph[vertex].append(num)
						if vertex not in graph[num]:
							graph[num].append(vertex) 			 
				
	
	
	return graph

def add_edges_color(graph,puzzle):
	
	colored_vertices={}
	
	for i in range(1,10):
		for j in range(1,10):
			if puzzle[i][j]!=0:
				colored_vertices[9*(i-1)+j]=puzzle[i][j]
	
	#print colored_vertices
	
	#for vertices not having same color join them by edges
	
	for key in colored_vertices:
		for k in colored_vertices:
			if key!=k and colored_vertices[key]!=colored_vertices[k]:
				if k not in graph[key]:
					graph[key].append(k)
					if key not in graph[k]:
						graph[k].append(key)
	
	#for vertices having same color
	
	for key in colored_vertices:
		for k in colored_vertices:
			if key!=k and colored_vertices[key]==colored_vertices[k]:
				for ver in graph[k]:
					if ver not in graph[key] and ver!=key:
						graph[key].append(ver)	
	
	
											
				
				
	return graph
	
"""buildgraph(1)"""				
	
