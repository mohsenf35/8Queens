
# coding: utf-8

# In[48]:


import matplotlib.pyplot as plt
import numpy as np
import random

#NQueenFunctions

def InitFirstPopulation(Queens, Solutions):
    Population = np.zeros([Solutions, Queens + 1])
    
    for j in range(0, Solutions):        
        for i in range(0, Queens):            
            value = random.randint(1, Queens)
            while(1 == 1):
                if value in Population[j] :
                    value = random.randint(1, Queens)
                else:
                    Population[j, i] = value
                    break

    return Population    

def CostFunctionAll(A):   
    for i in range(0 , len(A)):       
        A[i, 8] = CostFunction(A[i])
        
    B = np.array(A)
    return np.array(sorted(B, key=lambda x :x[-1]))

def CostFunction(A):
    Threats = 0
    Queens = len(A) - 1
    #print('Queens: ' + str(Queens))
    
    for i in range(0 , Queens):                
        value = A[i]
        #print('========================')
        for j in range(i + 1, Queens):
            #print('i = ' + str(i) + '; j = ' + str(j))            
            
            #line Threats
            if(value == A[j] and j != i):
                Threats = Threats + 1               
            
            #Cross Threats
            if(abs(j - i) + value == A[j]):
                #print('x1')
                Threats = Threats + 1               
            
            if(abs(abs(j - i) - value) == A[j]):
                #print('x2')
                Threats = Threats + 1               
    
    #print(str(A) + ' => ' + str(Threats))
    #print('--------------------------------------------')
    return Threats

def CrossOver(Population, NewPopulation):
    p1 = Population[random.randint(0, 99),:8]
    p2 = Population[random.randint(0, 99),:8]    
    
    ch1 = np.zeros(8)
    ch2 = np.zeros(8)
    #print(ch1)       
    
    ch1[0] = p1[0]
    ch1[1] = p1[1]
    ch1[2] = p1[2]
    ch1[3] = p1[3]
    for i in range(4, 8):
        #print('index = ' + str(i))
        for j in range(0, 8):
            val = p2[j]
            if val not in ch1:
                ch1[i] = val        
       
    ch1 = np.append(ch1, [0])
    ch1[8] = CostFunction(ch1)
    
    #print('ch1 : ' + str(ch1))
    
    ch2[7] = p1[7]
    ch2[6] = p1[6]
    ch2[5] = p1[5]
    ch2[4] = p1[4]
    for i in range(0, 4):
        #print('index = ' + str(i))
        for j in range(0 , 8):
            val = p1[j]
            if val not in ch2:
                ch2[i] = val
    
    
    ch2 = np.append(ch2, [0])
    ch2[8] = CostFunction(ch2)
    
    #print('ch2 : ' + str(ch2))    
    #print('--------------------------')    
    
    for i in range(0, len(NewPopulation)):            
        if(NewPopulation[i] is None):
            NewPopulation[i] = ch1
            break
        
    for j in range(0, len(NewPopulation)):    
        if(NewPopulation[j] is None):
            NewPopulation[j] = ch2
            break
    
    return NewPopulation

def Mutation(Population, NewPopulation):
    
    p1 = Population[random.randint(0, 99)]
    
    point1 = random.randint(0, 3)
    point2 = random.randint(4, 7)
    
    #print('p1 : ' + str(p1))
    
    ch1 = p1
    v1 = ch1[point1] 
    v2 = ch1[point2] 
    ch1[point1] = v2
    ch1[point2] = v1
    
    #print('val1 : ' + str(ch1[point1]))
    #print('val2 : ' + str(ch1[point2]))
    #print('point1 : ' + str(point1))
    #print('point2 : ' + str(point2))
    #print('ch1 : ' + str(ch1))
    #print('--------------------------------')
    
    ch1[8] = CostFunction(ch1)
    
   
    
    
    for i in range(0, len(NewPopulation)):    
        if(NewPopulation[i] is None):
            NewPopulation[i] = ch1
            break
    
    return NewPopulation 
    
Queens = 8
NumberOfSolutions = 100
Solutions = InitFirstPopulation(Queens, NumberOfSolutions)
Solutions = CostFunctionAll(Solutions)    
#print(len(Solutions))
#print(len(Solutions[0]))
#print(type(Solutions))
print(Solutions)

CrossOverNumber = 40
MutationNumber = 30
NewPopulationNumber = 110

Epochs = 100
BestSolutions = [None] * Epochs
AVGSolutions = [None] * Epochs
AllSolutions = [None] * Epochs

AllSolutions[0] = Solutions
BestSolutions[0] = Solutions[0,8]
AVGSolutions[0] = np.average(Solutions[:,8])
#print(BestSolutions)
#print(AVGSolutions)
#print(Solutions[0:10])


# In[50]:


for i in range(1, Epochs):    
    LatestPopulation = AllSolutions[i-1]
    NewPopulation = [None] * NewPopulationNumber

    #CrossOver
    for j in range(0 , CrossOverNumber):        
        NewPopulation = CrossOver(LatestPopulation, NewPopulation)             
        
    #Mutation
    for j in range(0 , MutationNumber):        
        NewPopulation = Mutation(LatestPopulation, NewPopulation)
        
    #print(NewPopulation)
    Temp = np.array(sorted(NewPopulation, key=lambda x :x[-1]))
    #print(Temp)
    NewGeneration = Temp[:100,:]
    #print(NewGeneration)
    #Calculate
    AllSolutions[i] = NewGeneration
    BestSolutions[i] = NewGeneration[0,8]
    AVGSolutions[i] = np.average(NewGeneration[:,8])
    if(BestSolutions[i] == 0):
        print(NewGeneration[0])
        print(i)
        break
    
#print(BestSolutions)
#print(AVGSolutions)


plt.plot(BestSolutions)
plt.show()

plt.plot(AVGSolutions)
plt.show()

