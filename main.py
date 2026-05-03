import matplotlib.pyplot as plt
from euler_explicite import euler_explicite
from euler_implicite import euler_implicite
from runge_kutta import runge_kutta_4
from constante import *
import numpy as np

titres = ["Végétation (kg/km²)", "Wapitis (ind/km²)", "Cerfs (ind/km²)",
          "Loups (ind/km²)", "Ours (ind/km²)"]

# ── FIGURE 1 : comparaison des méthodes ──────────────────────
sol_exp = np.array(euler_explicite(V))
sol_imp = np.array(euler_implicite(V))
sol_rk4 = np.array(runge_kutta_4(V))

fig1, axes1 = plt.subplots(3, 2, figsize=(12, 10))
axes1 = axes1.flatten()

for idx in range(5):
    axes1[idx].set_xlabel("Temps (années)")
    axes1[idx].set_ylabel(titres[idx])
    axes1[idx].plot(intervalle, sol_exp[:, idx], label="Euler explicite", linewidth=2)
    axes1[idx].plot(intervalle, sol_imp[:, idx], label="Euler implicite", linewidth=1.5, linestyle="--")
    axes1[idx].plot(intervalle, sol_rk4[:, idx], label="Runge-Kutta 4",  linewidth=1,   linestyle=":")
    axes1[idx].legend(fontsize=7)

axes1[5].axis("off")
plt.suptitle("Comparaison des méthodes numériques", fontsize=13)
plt.tight_layout()
plt.savefig("resultats.png", dpi=150)
print("Sauvegardé : resultats.png")

# ── FIGURE 2 : scénario Yellowstone ──────────────────────────
sol_normal = np.array(runge_kutta_4(V))
sol_yel    = np.array(runge_kutta_4(V_yellowstone))

fig2, axes2 = plt.subplots(3, 2, figsize=(12, 10))
axes2 = axes2.flatten()

for idx in range(5):
    axes2[idx].set_xlabel("Temps (années)")
    axes2[idx].set_ylabel(titres[idx])
    axes2[idx].plot(intervalle, sol_normal[:, idx], label="Avec loups",  linewidth=2)
    axes2[idx].plot(intervalle, sol_yel[:, idx],    label="Sans loups",  linewidth=2, linestyle="--")
    axes2[idx].legend(fontsize=7)

axes2[5].axis("off")
plt.suptitle("Scénario Yellowstone : réintroduction du loup", fontsize=13)
plt.tight_layout()
plt.savefig("yellowstone.png", dpi=150)
print("Sauvegardé : yellowstone.png")
