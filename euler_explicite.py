from Code.py import f, pas, temps, V
import numpy as np

def euler_explicite(f_init):
  """
  Résous le problème de Cauchy par la méthode d'euler_explicite
  """
  nb_points=temps/pas
  res=[f_init]
  for i in range(nb_points-1):
    res.append(np.add(res[i]+pas*f(pas*i,res[i])))
  return res
