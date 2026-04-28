from Code.py import f, pas, temps
import numpy as np

def euler_explicite(f_init,pas):
  nb_points=temps/pas
  res=[f_init]
  for i in range(nb_points-1):
    res.append(res[i]+pas*f(pas*i,res[i]))
  return res
