from constante import *
from f import f
import numpy as np
from copy import copy

def runge_kutta_4(V):
  """
  Résous le problème de Cauchy par RK4
  v : vecteur composé du vecteur d'état initial
  """
  t=0
  v=[V.copy()]
  while t<temps:
    k1=f(t,v[-1])
    k2=f(t+(pas/2),np.add(v[-1],np.multiply((pas/2),k1)))
    k3=f(t+(pas/2),np.add(v[-1],np.multiply((pas/2),k2)))
    k4=f(t+pas,np.add(v[-1],np.multiply(pas,k3)))
    v.append(np.add(v[-1],np.multiply((pas/6),(np.add(k1,np.add(np.multiply(2,k2),np.add(np.multiply(2,k3),k4)))))))
    t=t+pas
  return v[:-1]
