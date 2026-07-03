# Simulación Numérica de Modos Fonónicos y Densidad de Estados (DOS) en una Red Cristalina 2D

Este repositorio contiene el desarrollo teórico y la implementación numérica en Python para resolver la dinámica de red de un cristal bidimensional cuadrado clásico. El proyecto combina el formalismo de la física del estado sólido con técnicas de diagonalización de matrices dinámicas para obtener las relaciones de dispersión y la Densidad de Estados (DOS).

## 🚀 Características del Proyecto
* **Resolución Teórica:** Modelado analítico mediante ecuaciones de movimiento clásico y formalismo de matriz dinámica en LaTeX.
* **Cálculo Numérico:** Implementación en Python utilizando `NumPy` y `SciPy` para resolver problemas de eigenvalores en la Primera Zona de Brillouin.
* **Visualización de Datos:** Gráficas de alta calidad de las ramas fonónicas y de la DOS numérica frente a la analítica (Singularidades de Van Hove) usando `Matplotlib`.

---

## 📐 Fundamento Teórico

Consideramos una red bidimensional cuadrada con átomos de masa $M$ conectados a sus primeros vecinos mediante resortes de constante elástica $C$. Las ecuaciones de movimiento para el desplazamiento del átomo en la posición $(l,m)$ están dadas por:

$$M \ddot{u}_{l,m} = -C (2u_{l,m} - u_{l+1,m} - u_{l-1,m}) - C' (2u_{l,m} - u_{l,m+1} - u_{l,m-1})$$

Proponiendo soluciones de tipo onda viajera $u_{l,m} = \epsilon e^{i(k_x la + k_y ma - \omega t)}$, el problema se reduce a encontrar los eigenvalores de la **Matriz Dinámica** $D(\mathbf{k})$:

$$\det|D(\mathbf{k}) - \omega^2 I| = 0$$

Para una red cuadrada con interacciones a primeros vecinos, la relación de dispersión analítica resultante es:

$$\omega(\mathbf{k}) = 2 \sqrt{\frac{C}{M}} \left| \sin\left(\frac{k_x a}{2}\right) \right| + \dots$$

---

## 📊 Resultados y Gráficas

Las simulaciones numéricas permiten mapear la frecuencia $\omega$ a lo largo de las direcciones de alta simetría de la zona de Brillouin ($\Gamma \rightarrow X \rightarrow M \rightarrow \Gamma$) y evaluar la densidad de estados.

### 1. Relación de Dispersión Fonónica
*(Inserta aquí tu gráfica de las bandas de energía/frecuencia)*
![Relación de Dispersión](assets/dispesion red2dfonones.png)

### 2. Densidad de Estados Numérica (DOS)
*(Inserta aquí tu gráfica del histograma o curva de la DOS, idealmente mostrando las singularidades)*
![Densidad de Estados](assets/dos_numerical.png)

---

## 🛠️ Tecnologías y Librerías Utilizadas

* **Python 3.x** - Lenguaje principal de desarrollo.
* **NumPy** - Para la construcción de mallas en el espacio recíproco y operaciones matriciales eficientes.
* **SciPy** - Utilizado para la diagonalización matemática y algoritmos de integración.
* **Matplotlib & Seaborn** - Para la generación de gráficos científicos listos para publicación.
* **LaTeX** - Empleado para la redacción del reporte detallado del proyecto.

---

## 📁 Estructura del Repositorio

* `/src`: Contiene los scripts de Python (`simulacion_red.py` o Jupyter Notebooks).
* `/docs`: Reporte final en PDF generado con el código de LaTeX original.
* `/assets`: Imágenes y gráficas utilizadas en este archivo de presentación.

---

## 🔧 Cómo Ejecutar la Simulación

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/TU_USUARIO/red-bidimensional-fonones.git](https://github.com/TU_USUARIO/red-bidimensional-fonones.git)
