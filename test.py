import numpy as np
import plot

'''
SVD of matrix mat
'''
def svd(mat):
    return np.linalg.svd(mat)

def main():
    print("Hello world!")
    
    # Simplest arrays
    m0 = np.zeros((4,2))             #zeros 
    m1 = np.zeros(3)                 #zeros (square)
    m2 = np.eye(3)                   #identity (square)
    m3 = np.random.randn(2,3)        #random vals sampled from normal dist
 
    # Defining arrays using primitive lists
    m4 = np.array([[1,2,3],[4,5,6]]) #takes in Python list
    m5 = np.asarray(m4)              #like 'np.array' except won't make copy
    m4[0,0] = 10
    print("array reference:", m5[0,0], m5[0,0]) #note: both variables updated
    
    # Array types (float, int, etc)
    print("data types:")
    print(m3.dtype)
    print(m4.dtype)
    m6 = np.array([1,2], dtype=np.int64)
    print(m6.dtype)
    m6 = m6.astype(np.float32)       #change array data type
    print(m6.dtype)   
 
    # Manipulating arrays
    a = np.random.randn(3,5)
    b = np.random.randn(1,5)
    c = np.vstack((a,b))             #use np.hstack for horizontal stacking
    print("vstack shape:", c.shape)

    d = np.reshape(a, (5,3))
    print("reshape:", d.shape)
  
    # SVD 
    mat = np.eye(3)
    mat[0,0] = 3
    mat[2,2] = 2
    print("input matrix:\n", mat)
    print("of shape:", mat.shape)
    
    u,s,vh = svd(mat)
    print("singular values:", s)

if __name__ == '__main__':
    main()
    #plot.golden_curve(15)
