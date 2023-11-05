# Find the number of islands in the matrix
## Example
IP : 
```
4 4 
0 1 0 1
0 1 1 0
0 1 0 0
0 0 1 1
```
OP : 
```
3
```
## code python 
```
def check(ar,i,j):
  if ( i<0 or j<0 or i>=m or j>=n or ar[i][j]==0):
    return
  
  ar[i][j]=0
  check(ar,i,j-1) #left element 
  check(ar,i-1,j) #top element
  check(ar,i+1,j) #bottom element
  check(ar,i,j+1) #right element

#scan row & column
m,n = map(int,input().split())
ar = []
#scan array
for i in range(m):
  ar.append(list(map(int,input().split())))
c = 0
for i in range(m):
  for j in range(n):
    if ar[i][j]==1:
      check(ar,i,j)
      c+=1
print(c)
```
