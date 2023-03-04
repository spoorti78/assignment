import numpy as np
arr = np.array([[0, 8, 0], [7, 0, 0], [-5, 0, 1]])
  
print ("Input  array : \n", arr)
    
out_tpl = np.nonzero(arr)
print ("Indices of non zero elements : ", out_tpl) 