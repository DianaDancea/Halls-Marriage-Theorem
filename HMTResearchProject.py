# Establishing Connections Between Hall's Marriage Theorem and Birkhoff's Theorem 
# Author: Diana E. Dancea 
# Date: 2/19/2024
# Version: 1.1

'''
Logic: 
1) Take in a matrix from user 
2) Check that each row and column has at least one 1 entry (doubly stochastic)
3) Check that Marriage condition is satisfied by summing columns and checking if k >= n rows 
    *There needs to be at least the same number of rows and columns for a possible match, cannot be less 
4) Check each subrow to be marriage condition sufficient 
'''
#Using Numpy 
import numpy as np

#This functions gets the rows and columns from the user input 
def getMatrixInfo(): 
  rows = int(input("Enter the number of rows:"))
  columns = int(input("Enter the number of columns:"))
  return rows, columns

#This function takes in the matrix entries and displays the matrix
def inputMatrix(rows, columns): 
  
  print("Please enter the entries in a single line (separated by a space): ")
  
  #This allows the numbers to by taken in and split by their space
  #Map allows input() to be applied to the list of numbers 
  entries = list(map(int, input().split()))
  
  #This prints the matrix 
  matrix = np.array(entries).reshape(rows, columns)

  #Check if input is 0 and 1, if not don't continue 
  #if not a 0-1 matrix, transform it
  
  return matrix 

#This function calculates the row sum 
def rowSum(matrix): 
  rowSumArray = []
  for row in matrix:
        rowsum = sum(row)
        rowSumArray.append(rowsum)
  return rowSumArray

#This function calculates the column sum 
def columnSum(matrix, rows, columns): 
  columnSumArray = [0] * columns 
  for i in range(rows):
    for j in range(columns):
      columnSumArray[j] += matrix[i][j]
  return columnSumArray 

#This function checks if it is Doubly Stochastic 
def isDoublyStochastic(): 
   rowSumArray = rowSum(matrix)
   columnSumArray = columnSum(matrix, rows, columns)
   doubly = False
   
   #Checks the row and column sums of the indiviual rows 
   for i in rowSumArray:
      if rowSumArray[i] == 1 and columnSumArray[i] == 1: 
         doubly = True
      else: 
         continue 
   return doubly 

def countEntries(matrix): 
    countArray = []

    for row in matrix:
        count = 0
        for i in range(len(row)):
            if row[i] == 1:
                count += 1
        countArray.append(count)

    return countArray
  
'''count = 0
   countArray = []
  
   for j in range(len(matrix[rows, :])):
      if matrix[rows,j] == 1:
          count += 1
      countArray.append(count) 
           
   return countArray   '''
   
      

#This function checks if Marriage Condition is satisified
def isMarriageCondition(matrix, rows, columns): 
   marriage = False 
   countArray = countEntries(matrix)
   newMatrix = []
   newRow = [] 

   #Adding two rows 
   while True:
   #i = 1
    for i in range(len(matrix)-1):
        #j = i+1
        print("This is i: ", i)
        for j in range(i+1,len(matrix)): 
            #Check if each row has a distinct 1 entry 
          print("This is j: ", j)
          #if matrix[i][j] == 1:
          newRow =[x + y for x, y in zip(matrix[i], matrix[j])]
          newMatrix.append(newRow)
          print(newRow)
    return newMatrix
            
'''print(newMatrix)
 
   return marriage'''



















#Testing Area
rows, columns = getMatrixInfo()

matrix = inputMatrix(rows, columns)
rowsum = rowSum(matrix)
columnsum = columnSum(matrix, rows, columns)
marriageCondition = isMarriageCondition(matrix, rows, columns)
#doublyStochastic = isDoublyStochastic() 
entriesCount = countEntries(matrix)

print("The matrix is: \n ", matrix)
print("Row Sums: ", rowsum)
print("Column Sums: ", columnsum)
print("Marriage Condition: ", marriageCondition)
#print("Doubly Stochastic: ", doublyStochastic)
print("Non zero entries count in each row:", entriesCount)















''' 
#This function takes in the matrix from the user 
def inputMatrix():
  
  #These are the variables for row and columns values 
  rows = int(input("Please input the number of rows:"))
  columns = int(input("Please input the number of columns:"))

  #Initializing the matrix variable 
  matrix = []

  print("Hello! Please input the values in a single line, rowwise.")
  
  #Using a loop to take in the values from the user
  for i in range(rows):
    #this tempArray takes in the row entries 
    tempArray = [] 
    #this nested loop iterates over the column entries 
    for j in range(columns): 
      tempArray.append(int(input()))
    matrix.append(tempArray)

    #This for loop prints the matrix
    for i in range(rows):
      for j in range(columns): 
        print(matrix[i][j], end = " ")
      print()  


inputMatrix()

'''
