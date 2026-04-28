from Code.py import f
import numpy as np

def euler_explicite(f_init,pas,nb_points):
  res=[f_init]
  for i in range(nb_points-1):
    res.append(res[i]+pas*f(pas*i,res[i]))
  return res

