import numpy as np
from constante import *

def Jacobian(F,X, Xn, eps=1e-6):
    n = len(X)
    J = np.zeros((n, n))
    
    for i in range(n):
        X1 = X.copy()
        X1[i] += eps
        
        J[:, i] = (F(X1, Xn, h, params) - F(X, Xn, h, params)) / eps
    
    return J

def newton(X0, F, eps=1e-6, Nmax=50):
    X = X0.copy()
    
    for k in range(Nmax):
        Xn,X = F(X),Xn

        if np.linalg.norm(Xn) < eps:
            return Xn
        
        J = Jacobian(F, X, Xn)
        
        delta = np.linalg.solve(J, GX)
        Xn,X = X - delta,Xn
    
    return Xn
