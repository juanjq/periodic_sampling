
def resample(x,y,dt):

    #periodically array with x positions
    sample_x = [x[0]+dt*i for i in range(int((x[-1]-x[0])/dt))]
    

    #iterating trough all the sampling
    sample_y = []
    for i in range(len(sample_x)):
        
        #for each point of the sample_x, we locate it in terms of real data
        #first we check if the points are the same
        tEqual = False
        for j in range(len(x)):
            
            if sample_x[i] == x[j]:
                sample_y.append(y[j])
                tEqual = True
                
        #if not,
        if tEqual == False:

            j=0
            while x[j]<sample_x[i]:

                if j == len(x)-1:
                    print('ERROR in data')
                    break

                j = j+1
            
            #interpolating the points as a straight line
            B = (y[j]-y[j-1])/(x[j]-x[j-1])
            A = y[j-1]-B*(x[j-1])

            sample_y.append(A+B*sample_x[i])

    #return the arrays x, y resampled
    return sample_x, sample_y
