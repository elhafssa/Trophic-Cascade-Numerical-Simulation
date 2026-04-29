from f import f
from constante import pas, temps
import numpy as np

def euler_explicite(f_init):
  """
  Résous le problème de Cauchy par la méthode d'euler_explicite
  """
  nb_points=int(temps/pas)
  res=[f_init]
  for i in range(nb_points):
    res.append(np.add(res[i],np.multiply(pas,f(pas*i,res[i]))))
  return res[:-1]
