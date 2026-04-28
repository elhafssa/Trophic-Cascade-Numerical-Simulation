from Code.py import dt,f
from newton.py import newton 

def fonction_pour_newton(v,t):
  """
  définis la fonction où l'on cherche implicitement v(t+dt)
  """
  return x-v[-1]-dt*f(x,t+dt)

def euler_implicite(v):
  """
  Résous un problème de Cauchy via la méthode d'euler implicite
  """
  
  
  
