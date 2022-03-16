import numpy
import matplotlib.pyplot as plt

def matrix_factorization(R, P, Q, K, steps=5000, alpha=0.0002, beta=0.02):
    Q = Q.T
    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    # calculate error
                    eij = R[i][j] - numpy.dot(P[i,:],Q[:,j])
                    for k in range(K):
                        # calculate gradient with a and beta parameter
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])

        eR = numpy.dot(P,Q)
        e = 0
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - numpy.dot(P[i,:],Q[:,j]), 2)
                    for k in range(K):
                        e = e + (beta/2) * (pow(P[i][k],2) + pow(Q[k][j],2))

        # 0.001: local minimum
        if e < 0.001:
            break

    return P, Q.T

def takeinput():
    I = []
    print(Movies)
    print("Enter ratings in range 1-5, 0 if NA")
    for i in range(5):
        I.append((int(input())))
    print(I)
    return I

Movies = ["A. The Godfather", "B. The Dark Knight", "C. Interstellar", "D. The Matrix", "E. Parasite"]
R = numpy.array([])
while(True):
    print("Enter i to input, c to compute, q to exit")
    s = input()
    if(s=="i"):
        R = numpy.append(R, (takeinput()))
        R = numpy.reshape(R, (-1,5))
        print(R)

    elif(s=="c"):
        R = numpy.reshape(R, (-1,5))
        R = numpy.array(R)
        # N: num of User
        N = len(R)
        # M: num of Movie
        M = len(R[0])
        # Num of Features
        K = 3
        P = numpy.random.rand(N,K)
        Q = numpy.random.rand(M,K)
        nP, nQ = matrix_factorization(R, P, Q, K)
        nR = numpy.dot(nP, nQ.T)
        nR = numpy.round(nR)
        print(nR)
    
    else:
        break



