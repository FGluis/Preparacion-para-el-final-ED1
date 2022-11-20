from Listas import LinkedList, additionLinkedList
import numpy as np

Mat1 =np.loadtxt('Mat1.txt')
#print(Mat1)
Mat2 =np.loadtxt('Mat2 copy.txt')
#print(Mat2)

#Suma
Res = Mat1 + Mat2
#Resta
# Res = Mat1 - Mat2
# #Multiplicacion
# Res = Mat1.dot(Mat2)
print(Res)

#==================================================================
Matrix1 = LinkedList()
Matrix1.Mat_to_list(Mat1)
Matrix2 = LinkedList()
Matrix2.Mat_to_list(Mat2)
MatrixR = LinkedList()
MatrixR.Mat_to_list(Res)

print("Matrix one (Mat to list)")
print(Matrix1)
print("Matrix two (Mat to list)")
print(Matrix2)
print("Result with mat")
print(MatrixR)



#==================================================
Res = additionLinkedList(Matrix1,Matrix2)
print("Resultado with list")
print(Res)
print("List to Mat")
uwu = Res.List_to_Mat() 
print(uwu)
#========================================================
