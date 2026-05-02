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
# euler_implicite.py  — version corrigée et compatible

import copy
import numpy as np
from constante import *

def jacobienne_f(t, u, eps=1e-7):
    n = len(u)
    J = np.zeros((n, n))
    f0 = np.array(f(t, u))
    for j in range(n):
        u_eps = u.copy()
        u_eps[j] += eps
        J[:, j] = (np.array(f(t, u_eps)) - f0) / eps
    return J

def NewtonNd(F, dF, x0, eps, Nmax):
    x = x0.copy()
    k = 0
    erreur = 1.0
    Erreur = []
    while erreur > eps and k < Nmax:
        xold = copy.deepcopy(x)
        x = x - np.dot(np.linalg.inv(dF(x)), F(x))   # ← bug corrigé
        k += 1
        erreur = np.linalg.norm(x - xold) / np.linalg.norm(x)
        Erreur.append(erreur)
    return x, Erreur

def euler_implicite(u0, eps_newton=1e-10, Nmax_newton=50):
    """
    Même signature que euler_explicite(u0) et runge_kutta_4(u0).
    Utilise t0, T, h, f depuis constante.py.
    Retourne une liste de vecteurs d'état (sans les temps).
    """
    u0 = np.array(u0, dtype=float)
    n  = len(u0)
    N  = int(round((T - t0) / h))
    t_vec = np.linspace(t0, T, N + 1)

    U = np.zeros((N + 1, n))
    U[0] = u0

    for k in range(N):
        tn  = t_vec[k]
        tn1 = t_vec[k + 1]
        u_n = U[k]

        def G(u):
            return u - u_n - h * np.array(f(tn1, u))

        def JG(u):
            return np.eye(n) - h * jacobienne_f(tn1, u)

        # Prédicteur Euler explicite comme point de départ
        u_pred = u_n + h * np.array(f(tn, u_n))

        u_new, _ = NewtonNd(G, JG, u_pred, eps_newton, Nmax_newton)
        U[k + 1] = u_new

    return U   # shape (N+1, 5) — même format que les autres

        
       
