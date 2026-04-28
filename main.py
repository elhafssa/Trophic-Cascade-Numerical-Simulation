import matplotlib.pyplot as plt
from euler_explicite import euler_explicite
from euler_implicite import euler_implicite
from runge_kutta import runge_kutta_4
from constante import *

sol_el_expli=np.array(euleur_explicite(V))
sol_el_impli=np.array(euleur_implicite(V))
sol_RK4=np.array(runge_kutta_4(V))

vegetation_el_expli=sol_el_expli[:,0]
vegetation_el_impli=sol_el_impli[:,0]
vegetation_RK4=runge_kutta_4[:,0]
ongules_el_expli=sol_el_expli[:,1]
ongules_el_impli=sol_el_impli[:,1]
ongules_RK4=runge_kutta_4[:,1]
ongules_sec_el_expli=sol_el_expli[:,2]
ongules_sec_el_impli=sol_el_impli[:,2]
ongules_sec_RK4=runge_kutta_4[:,2]
loup_el_expli=sol_el_expli[:,3]
loup_el_impli=sol_el_impli[:,3]
loup_RK4=runge_kutta_4[:,3]
ours_el_expli=sol_el_expli[:,4]
ours_el_impli=sol_el_impli[:,5]
ours_RK4=runge_kutta_4[:,5]

intervalle=np.linspace(0,temps,temps/pas)

plt.subplot(3,2,2)
plt.plot(intervalle,ongules_el_expli)
plt.plot(intervalle,ongules_el_impli)
plt.plot(intervalle,ongules_RK4)

plt.subplot(3,2,1)
plt.plot(intervalle,vegetation_el_expli)
plt.plot(intervalle,vegetation_el_impli)
plt.plot(intervalle,vegetation_RK4)

plt.subplot(3,2,3)
plt.plot(intervalle,ongules_sec_el_expli)
plt.plot(intervalle,ongules_sec_el_impli)
plt.plot(intervalle,loup_RK4)

plt.subplot(3,2,4)
plt.plot(intervalle,loup_el_expli)
plt.plot(intervalle,loup_el_impli)
plt.plot(intervalle,vegetation_RK4)

plt.subplot(3,2,5)
plt.plot(intervalle,ours_el_expli)
plt.plot(intervalle,ours_el_impli)
plt.plot(intervalle,ours_RK4)
