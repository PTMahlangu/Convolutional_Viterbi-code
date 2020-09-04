import numpy as np

def Viterbi(output0):    
    Join_Data ="".join(map(str,output0))
    temp0     = list(Join_Data)
    in_data   = np.zeros((len(temp0)))
    
    for j in range (0,len(temp0)):
        if(temp0[j])  =='1':
            in_data[j]=-1
        else:
            in_data[j]=1  
        
    lenght = int(len(in_data)/4)+1
    Metric          = np.zeros((16,lenght))
    Branch_Metric   = np.zeros((16,lenght))
    Path_Metric     = np.zeros((16,lenght))
    output          = np.zeros((lenght))
    
    temp1 = np.zeros((4))
    
    for i in range (0,int(len(in_data)/4)): # FOR INPPUT COUNT
        for k in range (0,16):
            temp2 = list('{0:04b}'.format(k))
            for j in range (0,4):
                if(temp2[j])=='1':
                    temp1[j]=-1
                else:
                    temp1[j]=1
           # print(temp1)
            Branch_Metric[k][i]= int(temp1[0])*in_data[4*i]+int(temp1[1])*in_data[4*i+1]+ int(temp1[2])*in_data[4*i+2]+int(temp1[3])*in_data[4*i+3]
        
        # stage 1
        Metric[0][1] = Branch_Metric[0][0]  
        Metric[8][1] = Branch_Metric[15][0]
        
        # stage 2
        Metric[0][2] = Branch_Metric[0][1]  + Metric[0][1] 
        Metric[8][2] = Branch_Metric[15][1] + Metric[0][1]
        
        Metric[4][2]  = Branch_Metric[12][1] +  Metric[8][1] 
        Metric[12][2] = Branch_Metric[3][1] +  Metric[8][1]
        Path_Metric[4][2] = 8 
        Path_Metric[12][2]= 8
        
        # stage 3
        Metric[0][3] = Branch_Metric[0][2]  + Metric[0][2] 
        Metric[8][3] = Branch_Metric[15][2] + Metric[0][2]
        
        Metric[4][3]  = Branch_Metric[12][2] +  Metric[8][2] 
        Metric[12][3] = Branch_Metric[3][2] +  Metric[8][2]
        Path_Metric[4][3] = 8  
        Path_Metric[12][3]= 8
        
        Metric[2][3]  = Branch_Metric[10][2] +  Metric[4][2] 
        Metric[10][3] = Branch_Metric[5][2] +  Metric[4][2]
        Path_Metric[2][3] = 4  
        Path_Metric[10][3]= 4
        
        Metric[6][3]  = Branch_Metric[6][2] +  Metric[12][2] 
        Metric[14][3] = Branch_Metric[1][2] +  Metric[12][2]
        Path_Metric[6][3] = 12  
        Path_Metric[14][3]= 12
        #stage 4
        Metric[0][4]  = Branch_Metric[0][3]  +  Metric[0][3]
        Metric[1][4]  = Branch_Metric[13][3] +  Metric[2][3]
        Path_Metric[1][4]= 2
        Metric[2][4]  = Branch_Metric[10][3] +  Metric[4][3] 
        Path_Metric[2][4]= 4
        Metric[3][4]  = Branch_Metric[7][3]  +  Metric[6][3]
        Path_Metric[3][4]= 6
        Metric[4][4]  = Branch_Metric[12][3] +  Metric[8][3] 
        Path_Metric[4][4]= 8
        Metric[5][4]  = Branch_Metric[1][3]  +  Metric[10][3]
        Path_Metric[5][4]= 10
        Metric[6][4]  = Branch_Metric[6][3]  +  Metric[12][3]
        Path_Metric[6][4]= 12
        Metric[7][4]  = Branch_Metric[11][3] +  Metric[14][3]
        Path_Metric[7][4]= 14
        Metric[8][4]  = Branch_Metric[15][3] +  Metric[0][3]
        Metric[9][4]  = Branch_Metric[2][3]  +  Metric[2][3] 
        Path_Metric[9][4]= 2
        Metric[10][4] = Branch_Metric[5][3]  +  Metric[4][3]
        Path_Metric[10][4]= 4
        Metric[11][4] = Branch_Metric[14][3]  +  Metric[6][3] 
        Path_Metric[11][4]= 6
        Metric[12][4] = Branch_Metric[3][3]  +  Metric[8][3] 
        Path_Metric[12][4]= 8
        Metric[13][4] = Branch_Metric[14][3] +  Metric[10][3]
        Path_Metric[13][4]= 10
        Metric[14][4] = Branch_Metric[1][3]  +  Metric[12][3] 
        Path_Metric[14][4]= 12
        Metric[15][4] = Branch_Metric[4][3]  +  Metric[14][3]
        Path_Metric[15][4]= 14
        
        
    # STAGE 4 TO N   s
    i = 4   
    while(i < int(len(in_data)/4)): # FOR INPPUT COUNT
        for k in range (0,16):
            temp2 = list('{0:04b}'.format(k))
            for j in range (0,4):
                if(temp2[j])=='1':
                    temp1[j]=-1
                else:
                    temp1[j]=1
           # print(temp1)
            Branch_Metric[k][i]= int(temp1[0])*in_data[4*i]+int(temp1[1])*in_data[4*i+1]+ int(temp1[2])*in_data[4*i+2]+int(temp1[3])*in_data[4*i+3]
        
        
        Metric[0][i+1] =max(Metric[0][i] + Branch_Metric[0][i],Metric[1][i] + Branch_Metric[15][i])
        if ((Metric[0][i] + Branch_Metric[0][i]) > (Metric[1][i] + Branch_Metric[15][i])):
            Path_Metric[0][i+1]= 0
        else:
            Path_Metric[0][i+1]= 1
        
        Metric[1][i+1] =max(Metric[2][i] + Branch_Metric[13][i],Metric[3][i] + Branch_Metric[2][i]) 
        if ((Metric[2][i] + Branch_Metric[13][i]) > (Metric[3][i] + Branch_Metric[2][i])):
            Path_Metric[1][i+1]= 2
        else:
            Path_Metric[1][i+1]= 3 
            
        Metric[2][i+1] =max(Metric[4][i] + Branch_Metric[10][i],Metric[5][i] + Branch_Metric[5][i]) 
        if (Metric[4][i] + Branch_Metric[10][i] > Metric[5][i] + Branch_Metric[5][i]):
            Path_Metric[2][i+1]= 4
        else:
            Path_Metric[2][i+1]= 5
            
        Metric[3][i+1] =max(Metric[6][i] + Branch_Metric[7][i],Metric[7][i] + Branch_Metric[8][i])
        if (Metric[6][i] + Branch_Metric[7][i] > Metric[7][i] + Branch_Metric[8][i]):
            Path_Metric[3][i+1]= 6
        else:
            Path_Metric[3][i+1]= 7 
            
        Metric[4][i+1] =max(Metric[8][i] + Branch_Metric[12][i],Metric[9][i] + Branch_Metric[3][i])
        if (Metric[8][i] + Branch_Metric[12][i] > Metric[9][i] + Branch_Metric[3][i]):
            Path_Metric[4][i+1]= 8
        else:
            Path_Metric[4][i+1]= 9
        
        Metric[5][i+1] =max(Metric[10][i]+ Branch_Metric[1][i],Metric[11][i]+ Branch_Metric[14][i])
        if (Metric[10][i]+ Branch_Metric[1][i] > Metric[11][i]+ Branch_Metric[14][i]):
            Path_Metric[5][i+1]= 10
        else:
            Path_Metric[5][i+1]= 11
            
        Metric[6][i+1] =max(Metric[12][i]+ Branch_Metric[6][i],Metric[13][i]+ Branch_Metric[9][i])
        if (Metric[12][i]+ Branch_Metric[6][i] > Metric[13][i]+ Branch_Metric[9][i]):
            Path_Metric[6][i+1]= 12
        else:
            Path_Metric[6][i+1]= 13
            
        Metric[7][i+1] =max(Metric[14][i]+ Branch_Metric[11][i],Metric[15][i]+ Branch_Metric[4][i])
        if (Metric[14][i]+ Branch_Metric[11][i] > Metric[15][i]+ Branch_Metric[4][i]):
            Path_Metric[7][i+1]= 14
        else:
            Path_Metric[7][i+1]= 15
        
        Metric[8][i+1] =max(Metric[0][i] + Branch_Metric[15][i],Metric[1][i] + Branch_Metric[0][i])
        if (Metric[0][i] + Branch_Metric[15][i] > Metric[1][i] + Branch_Metric[0][i]):
            Path_Metric[8][i+1]= 0
        else:
            Path_Metric[8][i+1]= 1
            
        Metric[9][i+1] =max(Metric[2][i] + Branch_Metric[2][i],Metric[3][i] + Branch_Metric[13][i])
        if (Metric[2][i] + Branch_Metric[2][i] > Metric[3][i] + Branch_Metric[13][i]):
            Path_Metric[9][i+1]= 2
        else:
            Path_Metric[9][i+1]= 3
            
        Metric[10][i+1]=max(Metric[4][i] + Branch_Metric[5][i],Metric[5][i] + Branch_Metric[10][i])
        if (Metric[4][i] + Branch_Metric[5][i] > Metric[5][i] + Branch_Metric[10][i]):
            Path_Metric[10][i+1]= 4
        else:
            Path_Metric[10][i+1]= 5
            
        Metric[11][i+1]=max(Metric[6][i] + Branch_Metric[8][i],Metric[7][i] + Branch_Metric[7][i])
        if (Metric[6][i] + Branch_Metric[8][i] > Metric[7][i] + Branch_Metric[7][i]):
            Path_Metric[11][i+1]= 6
        else:
            Path_Metric[11][i+1]= 7
            
        Metric[12][i+1]=max(Metric[8][i] + Branch_Metric[3][i],Metric[9][i] + Branch_Metric[12][i])
        if (Metric[8][i] + Branch_Metric[3][i]>Metric[9][i] + Branch_Metric[12][i]):
            Path_Metric[12][i+1]= 8
        else:
            Path_Metric[12][i+1]= 9
            
        Metric[13][i+1]=max(Metric[10][i]+ Branch_Metric[14][i],Metric[11][i]+ Branch_Metric[1][i])
        if (Metric[10][i]+ Branch_Metric[14][i] > Metric[11][i]+ Branch_Metric[1][i]):
            Path_Metric[13][i+1]= 10
        else:
            Path_Metric[13][i+1]= 11
            
        Metric[14][i+1]=max(Metric[12][i]+ Branch_Metric[9][i],Metric[13][i]+ Branch_Metric[6][i])
        if (Metric[12][i]+ Branch_Metric[9][i] > Metric[13][i]+ Branch_Metric[6][i]):
            Path_Metric[14][i+1]= 12
        else:
            Path_Metric[14][i+1]= 13
            
        Metric[15][i+1]=max(Metric[14][i]+ Branch_Metric[4][i],Metric[15][i]+ Branch_Metric[11][i])
        if (Metric[14][i]+ Branch_Metric[4][i]>Metric[15][i]+ Branch_Metric[11][i]):
            Path_Metric[15][i+1]= 14
        else:
            Path_Metric[15][i+1]= 15
        
        i=i+1
        
        
    E = np.zeros((16, 1))
    index = i
    for z in range (0,15):
        E[z] = Metric[z][index]
        
    resul  =  np.where(E == np.amax(E))
    #result = np.where(Metric == np.amax(Metric))
    
    x = index
    y = int(resul[0][0]) 
    
    while(x!=0):
        if ((y ==0) or (y ==1) or (y ==2) or (y ==3) or (y ==4) or (y ==5) or (y ==6) or (y ==7)):
            
            y = int(Path_Metric[y][x])
            output[x]=0
            x=x-1
                         
        else:
            y = int(Path_Metric[y][x])
            output[x]=1 
            x=x-1
        
    inputData2 = []
    inputData2[0:len(output)-1] = output[1:len(output)-1]
    inputData2 = np.int32(inputData2)
    return inputData2

