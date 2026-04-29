from constante import *

def runge_kutta_4(v):
  """
  Résous le problème de Cauchy par RK4
  v : vecteur composé du vecteur d'état initial
  """
  t=0
  while t<temps:
    k1=f(t,v[-1])
    k2=f(t+(dt/2),v[-1]+(dt/2)*k1)
    k3=f(t+(dt/2),v[-1]+(dt/2)*k2)
    k4=f(t+dt,v[-1]+dt*k3)
    v.append(v[-1]+(dt/6)*(k1+2*k2+2*k3+k4))
    t=t+dt
  return v
