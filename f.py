from constante import *
import numpy as np

def kappa_N(V):
    return K_N*V/(V_et+V)
def kappa_D(V):
    return K_D*V/(V_etet+V)

def f(t, u):
    V, N, D, W, B = u
    Phi_W=(c_WN*N)/(W+beta*N)+(c_WN*D)/(h_WD+D)
    dV = (r_V * V * (1 - V / K_V)
          - (alpha_N * V * N) / (nu_N + V)
          - (alpha_D * V * D) / (nu_D + V)
          - (alpha_B * V * B) / (nu_B + V))
  
    dN = (r_N * N * (1 - (N / kappa_N(V)) ** theta_N)
          - (c_WN * N * W) / (W + beta*N)
          - (c_BN * N * B) / (h_BN + N)
          - delta_N * N)
  
    dD = (r_D * D * (1 - (D / kappa_D(V)) ** theta_D)
          - (c_WD * D * W) / (h_WD + D)
          - (c_BD * D * B) / (h_BD + D)
          - delta_D * D)

    dW = ((epsilon_1 * np.log(Phi_W + eta) - epsilon_2) * W
          - m_W * W
          - mu_W * np.sin(np.pi * t) ** 2 * W)
 
    dB = ((e_B * (c_BN * N / (h_BN + N) + c_BD * D / (h_BD + D))
           + e_V * alpha_B * V / (nu_B + V)
           - m_B) * B)
 
    return [dV, dN, dD, dW, dB]
