import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    a=(vector[0]**2+vector[1]**2+vector[2]**2)**.5
    if a==0:
        vector=[0,0,0]
    else:
        tempvector=[vector[0]/a,vector[1]/a,vector[2]/a]
        vector=tempvector
    return vector

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    if i+1>=len(polygons):
        A=[polygons[i],polygons[0]]
        B=[polygons[i],polygons[1]]
    elif i+2>=len(polygons):
        A=[polygons[i],polygons[i+1]]
        B=[polygons[i],polygons[0]]
    else:
        A=[polygons[i],polygons[i+1]]
        B=[polygons[i],polygons[i+2]]
    Ax=A[1][0]-A[0][0]
    Ay=A[1][1]-A[0][1]
    Az=A[1][2]-A[0][2]
    Bx=B[1][0]-B[0][0]
    By=B[1][1]-B[0][1]
    Bz=B[1][2]-B[0][2]
    normal=[Ay*Bz-Az*By,Az*Bx-Ax*Bz,Ax*By-Ay*Bx]
    return normal
