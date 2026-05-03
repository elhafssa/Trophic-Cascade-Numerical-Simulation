# Cascade Trophique — Simulation Numérique

Simulation numérique d'une cascade trophique à 5 compartiments
(végétation, wapitis/orignaux, cerfs, loups, ours) modélisée par
un système d'équations différentielles ordinaires non linéaires
et non autonomes.

## Structure du projet

- `constante.py` — Paramètres du modèle
- `f.py` — Le système d'équations différentielles
- `euler_explicite/euler_implicite/runge_kutta.py` — Différentes méthodes de résolutions des équations différentielles
- `main.py` — Simulation et affichage des résultats

## Méthodes numériques implémentées

- **Euler explicite** — ordre 1, simple mais conditionnellement stable
- **Euler implicite** — Stable, résolu à chaque pas via la méthode de Newton
- **Runge-Kutta 4** — ordre 4

## Auteurs

Thaddée · Rémi · Hafssa · Malek
