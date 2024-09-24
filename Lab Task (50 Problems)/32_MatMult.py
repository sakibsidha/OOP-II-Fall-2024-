A = [[9, 6, 3],    
     [2, 4, 5],    
     [5, 7, 9]]
     
B = [[3, 2, 4],    
     [4, 3, 8],    
     [7, 4, 5]]     
   
multiResult = [[0, 0, 0],      
               [0, 0, 0],      
               [0, 0, 0]]   
   
for m in range(len(A)): 
   for n in range(len(B[0])):   
        for o in range(len(B)):
            multiResult[m][n] += A[m][o] * B[o][n]

print("The multiplication result of matrix A and B is:") 
for res in multiResult:      
   print(res)