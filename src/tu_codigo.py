import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#valores fisicos de la red 2D
#los valores se colocaran adiminsionales y de magnitud uno
#simplificando computo y permite dan aproximacion a graficos presentados en el capitulo 4 y 5 del libro de kittel.
K = 1.0    # constante de resorte
m = 1.0    # masa
a = 1.0    # parámetro de red

# Defincion de la Malla en el espacio recíproco (primera zona de Brillouin)
N = 800  # resolución de la malla

k_max = np.pi / a
kx = np.linspace(-k_max, k_max, N)
ky = np.linspace(-k_max, k_max, N)

KX, KY = np.meshgrid(kx, ky)
# Calculo de la Relación de dispersión para la red 2D

# omega = sqrt( (4K/m) * [sin^2(kx*a/2) + sin^2(ky*a/2)] )
omega = np.sqrt( (4 * K / m) * ( np.sin(KX * a / 2)**2 + np.sin(KY * a / 2)**2 ) )

# Valores en puntos de alta simetría (para referencia)
omega_X = np.sqrt(4 * K / m)      # en X = (pi/a, 0)
omega_M = np.sqrt(8 * K / m)      # en M = (pi/a, pi/a)

# GRAFICO 1: Relacion de dispersion en forma de una Superficie 3D
fig = plt.figure(figsize=(14, 6))

ax1 = fig.add_subplot(1, 2, 1, projection='3d')
surf = ax1.plot_surface(KX, KY, omega, cmap='plasma',
                         edgecolor='none', alpha=0.85, antialiased=True)

# Puntos de alta simetría para tener referencia
# Gamma
ax1.scatter([0], [0], [0], color='cyan', s=100, edgecolor='black', 
            label=r'$\Gamma\ (0,0)$', zorder=5)
# X (4 puntos equivalentes)
for x, y in [(np.pi/a, 0), (-np.pi/a, 0), (0, np.pi/a), (0, -np.pi/a)]:
    ax1.scatter([x], [y], [omega_X], color='lime', s=80, edgecolor='black', zorder=5)
ax1.scatter([], [], [], color='lime', s=80, edgecolor='black', label=r'$X$')  # leyenda
# M (4 esquinas)
for x, y in [(np.pi/a, np.pi/a), (-np.pi/a, np.pi/a), 
             (np.pi/a, -np.pi/a), (-np.pi/a, -np.pi/a)]:
    ax1.scatter([x], [y], [omega_M], color='red', s=80, edgecolor='black', zorder=5)
ax1.scatter([], [], [], color='red', s=80, edgecolor='black', label=r'$M$')  # leyenda

ax1.set_xlabel(r'$k_x$', fontsize=13, labelpad=10)
ax1.set_ylabel(r'$k_y$', fontsize=13, labelpad=10)
ax1.set_zlabel(r'$\omega(k_x, k_y)$', fontsize=13, labelpad=10)
ax1.set_title(r'Superficie de dispersión $\omega(k_x, k_y)$' + '\n' +
              r'$\omega = \sqrt{\frac{4K}{m}[\sin^2(k_x a/2) + \sin^2(k_y a/2)]}$',
              fontsize=14)
ax1.legend(fontsize=10, loc='upper left')
fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=10, label=r'$\omega$')

# Vista preferencial
ax1.view_init(elev=25, azim=-60)

# GRAFICO 2: Curvas de nivel siendo la grafica derecha, obteniendo una vista superior
ax2 = fig.add_subplot(1, 2, 2)

# ajustar la densidad cerca de omega=0
levels = np.linspace(0, omega_M, 40)
contour = ax2.contourf(KX, KY, omega, levels=levels, cmap='plasma')
ax2.contour(KX, KY, omega, levels=levels[::5], colors='white', linewidths=0.5, alpha=0.5)

# Puntos de alta simetría
ax2.plot(0, 0, 'o', color='cyan', markersize=10, markeredgecolor='black', label=r'$\Gamma$')
ax2.plot([np.pi/a, -np.pi/a, 0, 0], [0, 0, np.pi/a, -np.pi/a], 
         'o', color='lime', markersize=8, markeredgecolor='black', label=r'$X$')
ax2.plot([np.pi/a, -np.pi/a, np.pi/a, -np.pi/a], 
         [np.pi/a, -np.pi/a, -np.pi/a, np.pi/a], 
         'o', color='red', markersize=8, markeredgecolor='black', label=r'$M$')

# Para definir el Cuadrado de la primera zona de Brillouin
zona_x = [-np.pi/a, np.pi/a, np.pi/a, -np.pi/a, -np.pi/a]
zona_y = [-np.pi/a, -np.pi/a, np.pi/a, np.pi/a, -np.pi/a]
ax2.plot(zona_x, zona_y, 'w--', linewidth=1.5, alpha=0.7, label='1ª ZB')

ax2.set_xlabel(r'$k_x$', fontsize=13)
ax2.set_ylabel(r'$k_y$', fontsize=13)
ax2.set_title(r'Curvas de nivel: $\omega(k_x, k_y) = \mathrm{cte}$', fontsize=14)
ax2.set_aspect('equal')
ax2.legend(fontsize=9, loc='upper right')
fig.colorbar(contour, ax=ax2, shrink=0.8, label=r'$\omega$')
plt.tight_layout()
plt.show()
