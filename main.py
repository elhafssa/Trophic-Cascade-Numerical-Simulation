import matplotlib.pyplot as plt
from euler_explicite import euler_explicite
from euler_implicite import euler_implicite
from runge_kutta import runge_kutta_4
from constante import *
import numpy as np

sol_el_expli = np.array(euler_explicite(V))
sol_el_impli = np.array(euler_implicite(V))
sol_RK4      = np.array(runge_kutta_4(V))

titres = ["Végétation (kg/km²)", "Wapitis (ind/km²)", "Cerfs (ind/km²)",
          "Loups (ind/km²)", "Ours (ind/km²)"]

for idx in range(5):
    plt.subplot(3, 2, idx + 1)
    plt.xlabel("Temps (années)")
    plt.ylabel(titres[idx])
    plt.plot(intervalle, sol_el_expli[:, idx], label="Euler explicite", linewidth=2)
    plt.plot(intervalle, sol_el_impli[:, idx], label="Euler implicite", linewidth=1.5, linestyle="--")
    plt.plot(intervalle, sol_RK4[:, idx],      label="Runge-Kutta 4",  linewidth=1,   linestyle=":")
    plt.legend(fontsize=7)

plt.tight_layout()
plt.savefig("resultats.png", dpi=150)
print("Figure sauvegardée dans resultats.png")
