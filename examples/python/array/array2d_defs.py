def init(arr, rows, cols):
  for r in range(rows):
    arr.append([])
    for c in range(cols):
      arr[r].append(0)

def parray(arr, msg):
  print(msg)
  for r in arr:
     for c in r:
        print(c,end = " ")
     print()
