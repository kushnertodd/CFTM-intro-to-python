import array2d_defs
#from array import *
rows, cols = (5, 5)
arr = []
array2d_defs.init(arr, rows, cols)
array2d_defs.parray(arr, "before assignment")
arr[2][3] = 4
arr[4][2] = 14
array2d_defs.parray(arr, "after assignment")

