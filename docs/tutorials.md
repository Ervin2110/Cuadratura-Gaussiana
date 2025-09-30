Para usar este módulo, primero se importa la librería y se especifica el módulo a usar:

```python3

from cuadrature import cuadrature

```
Una vez importado el módulo, se llama a la función de la siguiente forma:

```python3

cuadrature.cuadrature()

```

Esta función tiene 3 argumentos que tienen por defecto valores enteros, los cuales representan 3 ordenes diferentes de los polinomios de Legendre que se usan en la cuadratura Gaussiana, permitiendo que lo único que tenga que hacer sea llamar a la función y visualizar los resultados con $N = 2$, $N = 3$ y $N = 4$, el cual es el valor real.

Con esto, la función imprimirá la aproximación de la función con este método con los ordenes de los polinomios por defecto, junto con el valor y el orden del polinomio que genera la aproximación exacta:

```python3

Resultado de aproximación con polinomio de grado 2: 306,8199344959197
Resultado de aproximación con polinomio de grado 3: 317,264151733829
Resultado de aproximación con polinomio de grado 4: 317,3453903341579
Resultado correcto, polinomio de grado 4: 317,3453903341579

```
