from constante import *
from newton import *

def fonction_pour_newton(x):
  """
  définis la fonction où l'on cherche implicitement v(t+dt)
  """
  return x-v[-1]-dt*f(x,t+pas)

def euler_implicite(v):
  """
  Résous un problème de Cauchy via la méthode d'euler implicite
  v : vecteur d'état au temps initial
  """
  nb_points=int(temps/pas)
  for i in range(nb_points-1):
    t=i*pas
    v.append(newton(v[-1],fonction_pour_newton))
  return v
  
  #newton(X0, Xn, h,F, eps=1e-6, Nmax=50)
