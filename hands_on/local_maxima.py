def find_maxima(vector):
	values=[]
	indices=[]
	for index,item in enumerate(vector):
		if(index==0):
			if(item>vector[index+1]:
				values.append(item)
				indices.append(index)
		elif(index==len(vector)-1):
			if(item>vector[index-1]:
				values.append(item)
				indices.append(index)
		else:
			if(item>vector[index-1] & item>vector[index+1]:
				values.append(item)
				indices.append(index)
	return values, indices 

