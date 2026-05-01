import numpy as np
from constante import *

def Jacobian(F, X, eps=1e-6):
    n = len(X)
    J = np.zeros((n, n))
    
    for i in range(n):
        X1 = X.copy()
        X1[i] += eps
        
        J[:, i] = (F(X1, Xn, h, params) - F(X, Xn, h, params)) / eps
    
    return J


def newton(F,X0,v, eps=1e-6, Nmax=50):
    X = X0.copy()
    G = F(X,v[-1])
    J = Jacobian(F, X)
    delta = np.linalg.solve(J, G)
    Xn=X - delta
    for k in range(Nmax):

        G = F(X, Xn, h, params)
        
        if np.linalg.norm(G) < eps:
            return X
        
        J = Jacobian(F, X)
        
        delta = np.linalg.solve(J, G)
        X = X - delta
    
    return X
    ++++++++++++++++++++++++++++++++++++++++++++++++++++=====
    def NewtonNd(f,df,x0,eps,Nmax):
    x=x0
    k=0
    erreur=1.0
    Erreur=[]  
    while(erreur>eps and k<Nmax):
          xold=copy.deepcopy(x)
          x=x-np.dot(np.linalg.inv(df(x)),f(x))
          k=k+1
          erreur=np.linalg.norm(x-xold)/np.linalg.norm(x)
          print('Erreur=',erreur)
          print('f(x)',np.linalg.norm(f(x)))
          Erreur.append(erreur)
    return (x,Erreur)

        
       
