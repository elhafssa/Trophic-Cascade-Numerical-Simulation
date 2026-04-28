from constante.py import *
from newton.py import *

def fonction_pour_newton(x):
  """
  définis la fonction où l'on cherche implicitement v(t+dt)
  """
  return x-v[-1]-dt*f(x,t+dt)

def euler_implicite(v,t_final):
  """
  Résous un problème de Cauchy via la méthode d'euler implicite
  v : vecteur d'état au temps initial
  """
  t=0
  while t<t_final:
    v.append(newton(fonction_pour_newton))
    t=t+dt
  return v
  
  
