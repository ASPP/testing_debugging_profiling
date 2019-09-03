def find_maxima(ln):
    maxima = []
    if len(ln)>2:
        for i in range(1,len(ln)-1):
            if ln[i]>ln[i+1] and ln[i]>ln[i-1]:
                maxima.append(ln[i])
        if maxima==[]:
            print('no maxima')
        else:
            return maxima
    else:
        print('list is too short')
