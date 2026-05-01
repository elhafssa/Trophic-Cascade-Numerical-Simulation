from constante import *
from newton import *
from f import f

def fonction_pour_newton(x,v):
  """
  définis la fonction où l'on cherche implicitement v(t+dt)
  """
  return x-v[-1]-pas*f(t+pas,x)

def euler_implicite(V):
  """
  Résous un problème de Cauchy via la méthode d'euler implicite
  v : vecteur d'état au temps initial
  """
  v=[V.copy()]
  nb_points=int(temps/pas)
  for i in range(nb_points-1):
    t=i*pas
    v.append(newton(fonction_pour_newton,v[-1],v))
  return v
  
  #newton(X0, Xn, h,F, eps=1e-6, Nmax=50)
