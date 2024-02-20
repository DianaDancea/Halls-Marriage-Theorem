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
   doubly = False
   return doubly 

#This function checks if Marriage Condition is satisified
def isMarriageCondition(): 
   marriage = False
   return marriage 


















#Testing Area
rows, columns = getMatrixInfo()

matrix = inputMatrix(rows, columns)
rowsum = rowSum(matrix)
columnsum = columnSum(matrix, rows, columns)

print("The matrix is:", matrix)
print("Row Sums: ", rowsum)
print("Column Sums: ", columnsum)















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
