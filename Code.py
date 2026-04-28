V=[440,4.5,2.5,0.04,0.25] # Vecteur d'état au temps initial
V_t=[] #Evolution du vecteur d'état
V_t.append(V)



#Végétation Eq.(F1)
rV=1.20 #an−1 Taux de croissance intrinsèque de la végétation
KV=500 #kg.km−2 Capacité de charge de la végétation
αN=15.0 #kg.an−1.animal−1 Intensité de pâturage des wapitis/orignaux
νN=200 #kg.km−2 Demi-saturation, pâturage des wapitis/orignaux sur V
αD=8.0 #kg.an−1.animal−1 Intensité de pâturage des cerfs
νD=100 #kg.km−2 Demi-saturation, pâturage des cerfs sur V
αB=3.0 #kg an−1 animal−1Intensité de pâturage des ours sur V
νB=120 #kg km−2 Demi-saturation, pâturage des ours sur V



#Ongulé principal (wapiti/orignal) Eq.(F2)
rN=0.30 #an−1 Taux de croissance intrinsèque
KN=7.0 #animaux.km−2 Capacité de charge maximale
V⋆=70 #kg.km−2 Demi-saturation pour κ(V )
θN=4.0 #Exposant theta-logistique
cWN=7.5 #km2.animal−1.an−1 Coefficient de mise à mort loup–wapiti/orignaux
β=0.5 #Paramètre de dépendance au ratio
cBN=0.5 #km2.animal−1.an−1 Coefficient de mise à mort ours–wapiti/orignaux
hBN=3.0 #animaux.km−2 Demi-saturation ours–wapiti/orignaux
δN=0.05 #an−1 Mortalité de fond des wapiti/orignaux



#Ongulé secondaire (cerf) Eq.(F3)
rD=0.50 #an−1 Taux de croissance intrinsèque
KD=4.0 #animaux.km−2 Capacité de charge des cerfs
V⋆⋆=50 #kg.km−2 Demi-saturation pour κD(V )
θD=2.0 #Exposant theta-logistique
cW=D 2.0 #km2.animal−1 .an−1 Coefficient de mise à mort loups-cerfs
hWD=2.0 #animaux.km−2 Demi-saturation loups-cerfs
cBD=0.3 #km2.animal−1.an−1 Coefficient de mise à mort ours-cerfs
hBD=1.5 #animaux.km−2 Demi-saturation ours-cerfs
δD=0.08 #an−1 Mortalité de fond des cerfs



#Loups Eq.(F4)
ε1=0.25 #Coefficient de pente logarithmique de la réponse numérique
ε2=0.5 #Décalage de base de la réponse numérique
η=0.01 #an−1 Décalage de régularisation logarithmique
mW=0.15 #an−1 Mortalité naturelle des loups
µW=0.10 #an−1 Amplitude maximale du prélèvement saisonnier par l’homme


#Ours Eq.(F5)
eB=0.12 #Gain énergétique des ours à partir des proies
eV=0.02 #an−1 Gain énergétique des ours à partir de la végétation
mB=0.08 #an−1 Mortalité naturelle des ours
