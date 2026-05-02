import numpy as np
from constante import *
from f import f
import warnings


def jacobian(F, X, v_prev, h=1e-8):
    """Jacobien par différences finies centrées."""
    n = len(X)
    J = np.zeros((n, n))

    for i in range(n):
        X_plus  = X.copy(); X_plus[i]  += h
        X_minus = X.copy(); X_minus[i] -= h
        J[:, i] = (F(X_plus, v_prev) - F(X_minus, v_prev)) / (2 * h)

    return J


def newton(F, X0, v_prev, tol=1e-4, h=1e-6, Nmax=20):
    X = np.atleast_1d(np.array(X0, dtype=float))

    for k in range(Nmax):
        G = np.atleast_1d(F(X, v_prev))

        if np.linalg.norm(G) < tol:
            return X

        J = jacobian(F, X, v_prev, h)

        if abs(np.linalg.det(J)) < 1e-14:
            raise ValueError(f"Jacobien singulier à l'itération {k}.")

        delta = np.linalg.solve(J, G)
        X = X - delta

    warnings.warn(f"Newton : non convergé après {Nmax} itérations (||F|| = {np.linalg.norm(G):.2e}).")
    return X


def euler_implicite(V: np.ndarray) -> np.ndarray:
    nb_points = int(round(temps / pas))
    resultats = np.empty((nb_points, len(V)))
    resultats[0] = V

    for i in range(nb_points - 1):
        t      = i * pas
        v_prev = resultats[i]

        def equation(x, v_prev=v_prev, t=t):
            return x - v_prev - pas * np.array(f(t + pas, x))

        resultats[i + 1] = newton(equation, v_prev, v_prev)

    return resultats
