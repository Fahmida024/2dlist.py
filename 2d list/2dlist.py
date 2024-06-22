matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(len(matrix))
print (len(matrix [1]))
print (matrix[2][1])
print (matrix[0][2])

for i in range (3):
    for g in range (3):
        print (matrix[i][g])

row=int(input('enter the number of list you want'))
column=int(input('enter the number of items you want'))

matrix2=[]
for i in range (row):
    temp=[]
    for a in range(column):
        x=int(input('enter your value'))
        temp.append(x)
    matrix2.append(temp)
print (matrix2)

for i in range (row):
    for a in range (column):
        print (matrix2[i][a])

matrixA=[[1,2],[3,4]]
matrixB=[[5,6],[7,8]]
matrixResult=[[0,0],[0,0]]
for i in range (2):
    for a in range (2):
        matrixResult[i][a]=matrixA[i][a]+matrixB[i][a]
print (matrixResult)

matrixC=[[1,2],[3,4]]
matrixD=[[4,5],[6,7]]
matrixCD=[[0,0],[0,0]]
for i in range (2):
    for a in range (2):
        matrixCD[i][a]=matrixC[i][a]-matrixD[i][a]
print (matrixCD)

randomMarks=[10,20,30,40,44,67,58,32,54,78,32,45,67,22,33,48,88,66]
marks30=[]
marks69=[]
marks70=[]
for i  in randomMarks:
    if i<=30:
        marks30.append(i)
    elif 31<= i <= 69:
        marks69.append(i)
    else:
        marks70.append(i)
print (marks30)
print (marks69)
print (marks70)





        

