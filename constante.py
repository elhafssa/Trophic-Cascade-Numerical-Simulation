import numpy as np

V=[440,4.5,2.5,0.04,0.25] # Vecteur d'état au temps initial
pas=1/365
temps=71.0
intervalle=np.arange(0.,temps,pas)


#Végétation Eq.(F1)
r_V=1.20 #an−1 Taux de croissance intrinsèque de la végétation
K_V=500 #kg.km−2 Capacité de charge de la végétation
alpha_N=15.0 #kg.an−1.animal−1 Intensité de pâturage des wapitis/orignaux
nu_N=200 #kg.km−2 Demi-saturation, pâturage des wapitis/orignaux sur V
alpha_D=8.0 #kg.an−1.animal−1 Intensité de pâturage des cerfs
nu_D=100 #kg.km−2 Demi-saturation, pâturage des cerfs sur V
alpha_B=3.0 #kg an−1 animal−1Intensité de pâturage des ours sur V
nu_B=120 #kg km−2 Demi-saturation, pâturage des ours sur V



#Ongulé principal (wapiti/orignal) Eq.(F2)
r_N=0.30 #an−1 Taux de croissance intrinsèque
K_N=7.0 #animaux.km−2 Capacité de charge maximale
V_et=70 #kg.km−2 Demi-saturation pour κ(V )
theta_N=4.0 #Exposant theta-logistique
c_WN=7.5 #km2.animal−1.an−1 Coefficient de mise à mort loup–wapiti/orignaux
beta=0.5 #Paramètre de dépendance au ratio
c_BN=0.5 #km2.animal−1.an−1 Coefficient de mise à mort ours–wapiti/orignaux
h_BN=3.0 #animaux.km−2 Demi-saturation ours–wapiti/orignaux
delta_N=0.05 #an−1 Mortalité de fond des wapiti/orignaux



#Ongulé secondaire (cerf) Eq.(F3)
r_D=0.50 #an−1 Taux de croissance intrinsèque
K_D=4.0 #animaux.km−2 Capacité de charge des cerfs
V_etet=50 #kg.km−2 Demi-saturation pour κD(V )
theta_D=2.0 #Exposant theta-logistique
c_WD= 2.0 #km2.animal−1 .an−1 Coefficient de mise à mort loups-cerfs
h_WD=2.0 #animaux.km−2 Demi-saturation loups-cerfs
c_BD=0.3 #km2.animal−1.an−1 Coefficient de mise à mort ours-cerfs
h_BD=1.5 #animaux.km−2 Demi-saturation ours-cerfs
delta_D=0.08 #an−1 Mortalité de fond des cerfs



#Loups Eq.(F4)
epsilon_1=0.25 #Coefficient de pente logarithmique de la réponse numérique
epsilon_2=0.5 #Décalage de base de la réponse numérique
eta=0.01 #an−1 Décalage de régularisation logarithmique
m_W=0.15 #an−1 Mortalité naturelle des loups
mu_W=0.10 #an−1 Amplitude maximale du prélèvement saisonnier par l’homme


#Ours Eq.(F5)
e_B=0.12 #Gain énergétique des ours à partir des proies
e_V=0.02 #an−1 Gain énergétique des ours à partir de la végétation
m_B=0.08 #an−1 Mortalité naturelle des ours

