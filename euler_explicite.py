from f import f
from constante import pas, temps
import numpy as np

def euler_explicite(f_init):
  """
  Résous le problème de Cauchy par la méthode d'euler_explicite
  """
  nb_points=int(temps/pas)
  res=[f_init.copy()]
  for i in range(nb_points-1):
    res.append(np.add(res[i],np.multiply(pas,f(pas*i,res[i]))))
  return res
