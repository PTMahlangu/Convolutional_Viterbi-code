import numpy as np
from My_Viterbi import Viterbi
# code rate =1/4
def Conv_encoder(inputData): 
    inputData = np.int32(list(inputData))
    hold0   = [0]*(1+len(inputData))  
    for x in range(len(inputData)):
       hold0[x] = inputData[x]
       
    s_reg  = [0b0] * 5     # Shift Registers
    G      = [0b0] * 4     # Output 
    output0 = []
    for i in range (0,len(inputData)):
        s_reg[4]=s_reg[3]
        s_reg[3]=s_reg[2]
        s_reg[2]=s_reg[1]
        s_reg[1]=s_reg[0]
        s_reg[0]=inputData[i]
        
        G[0] = s_reg[0]^s_reg[1]^s_reg[2]^s_reg[3]^s_reg[4]
        G[1] = s_reg[0]^s_reg[1]^s_reg[3]^s_reg[4]
        G[2] = s_reg[0]^s_reg[2]^s_reg[4]
        G[3] = s_reg[0]^s_reg[3]^s_reg[4]
        
        output0.append("".join(map(str,G)))
        
    return output0

#................Code test...................
#inputData = [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]  
#A = Conv_encoder(inputData)
#B=Viterbi(A)
#C = "".join(map(str,A))