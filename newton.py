import numpy as np
from constante import *

def Jacobian(G, X, Xn, h, params, eps=1e-6):
    n = len(X)
    J = np.zeros((n, n))
    
    for i in range(n):
        X1 = X.copy()
        X1[i] += eps
        
        J[:, i] = (G(X1, Xn, h, params) - G(X, Xn, h, params)) / eps
    
    return J


def Newton_system(X0, Xn, h, params, eps=1e-6, Nmax=50):
    X = X0.copy()
    
    for k in range(Nmax):
        GX = G(X, Xn, h, params)
        
        if np.linalg.norm(GX) < eps:
            return X
        
        J = Jacobian(G, X, Xn, h, params)
        
        delta = np.linalg.solve(J, GX)
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

        
       
