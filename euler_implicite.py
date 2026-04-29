from constante import *
from newton import *

def fonction_pour_newton(x):
  """
  définis la fonction où l'on cherche implicitement v(t+dt)
  """
  return x-v[-1]-dt*f(x,t+dt)

def euler_implicite(v):
  """
  Résous un problème de Cauchy via la méthode d'euler implicite
  v : vecteur d'état au temps initial
  """
  t=0
  while t<temps:
    v.append(newton(v[-2],fonction_pour_newton))
    t=t+dt
  return v
  
  #newton(X0, Xn, h,F, eps=1e-6, Nmax=50)
