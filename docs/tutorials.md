Para usar este módulo, primero se importa la librería y se especifica el módulo a usar:

```python3

from cuadrature import cuadrature

```
Una vez importado el módulo, se llama a la función de la siguiente forma:

```python3

cuadrature.cuadrature()

```

Esta función tiene 3 argumentos que esperan valores enteros, los cuales representaran 3 ordenes, ya sean diferentes o iguales, de los polinomios de Legendre que se usan en la cuadratura Gaussiana. Estos argumentos no son obligatorios ponerlos, puesto que ya traen 3 valores por defecto (N1 = 2, N2 = 3, N3 = 4).

Si no se coloca ningún argumento, la función imprimirá la aproximación de la función con este método con los ordenes de los polinomios por defecto, además de el valor y el orden del polinomio que genera la aproximación exacta:

```python3

Resultado de aproximación con polinomio de grado 2: 306,8199344959197
Resultado de aproximación con polinomio de grado 3: 317,264151733829
Resultado de aproximación con polinomio de grado 4: 317,3453903341579
Resultado correcto, polinomio de grado 4: 317,3453903341579

```

En cambio, si se introducen argumentos, los valores de las aproximaciones cambiarán, según los ordenes de los polinomios que hayamos introducido:

```python3

cuadrature.cuadrature(1,5,6)

Resultado de aproximación con polinomio de grado 1: 306,8199344959197
Resultado de aproximación con polinomio de grado 5: 317,264151733829
Resultado de aproximación con polinomio de grado 6: 317,3453903341579
Resultado correcto, polinomio de grado 4: 317,3453903341579

```
