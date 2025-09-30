#!/usr/bin/erv python3

""" Aproxima la integral de una función

Este módulo permite al usuario realizar una aproximación de la integral por medio de la cuadratura Gaussiana.

Ejemplos:

    >>> from cuadrature import cuadrature

    >>> cuadrature.gaussxw(4)
    [-0.86113631 -0.33998104  0.33998104  0.86113631] [0.34785485 0.65214515 0.65214515 0.34785485]

    >>> cuadrature.gaussxwab(1, 3, x, w)
    [1.13886369 1.66001896 2.33998104 2.86113631] [0.34785485 0.65214515 0.65214515 0.34785485]

    >>> cuadrature.fInt(1)
    0.09070257317431829

    >>> cuadrature.cuadrature()
    Resultado de aproximación con polinomio de orden 2: 306,8199344959197
    Resultado de aproximación con polinomio de orden 3: 317,264151733829
    Resultado de aproximación con polinomio de orden 4: 317,3453903341579
    Resultado correcto, polinomio de orden 4: 317,3453903341579

El módulo contiene las siguientes funciones:

- `gaussxw(N)` - Devuelve los puntos de muestreo y los pesos del polinomio de Legendre de orden N.
- `gaussxwab(a, b, x, w)` - Devuelve los puntos de muestreo y los pesos del polinomio de Legendre de orden N, escalados a los límites requeridos.
- `funcInt(x)` - Devuelve el resultado de evaluar x en la función.
- `polinomios(N2 = 2, N3 = 3, N4 = 4)` - Imprime los valores de la función aproximada con polinomios de Legendre de orden 2, 3 y 4.
"""

from scipy.special import legendre
import numpy as np


def gaussxw(N):

    """Puntos de muestreo y pesos de la cuadratura de Gauss con polinomios de Legendre.

    Ejemplos:

        >>> gausxw(4)
        [-0.86113631 -0.33998104  0.33998104  0.86113631] [0.34785485 0.65214515 0.65214515 0.34785485]

    Args:
        N (int): Entero positivo, representa el grado del polimomio de Legendre.

    Returns:
        Tuple[numpy.ndarray, numpy.ndarray]:
            - x (float): Puntos de muestreo del polinomio de Legendre.
            - w (float): Pesos relacionados a los puntos de muestreo.
    """

    x, w = np.polynomial.legendre.leggauss(N)

    return x, w

def gaussxwab(a, b, x, w):

    """Puntos de muestreo y pesos escalados a los límites requeridos.

    Ejemplos:

        >>> x, w = np.polynomial.legendre.leggauss(4)
        >>> gausxwab(1, 3, x, w):
        [1.13886369 1.66001896 2.33998104 2.86113631] [0.34785485 0.65214515 0.65214515 0.34785485]

    Args:
        a (float): Límite inferior de la integral a aproximar.
        b (float): Límite superior de la integral a aproximar,
        x (numpy.array): Puntos de muestreo del polinomio (shape(N)).
        w (numpy.array): Pesos del polinomio (shape(N)).

    Returns:

        Tuple[numpy.ndarray, numpy.ndarray]:

            x (float): Puntos de muestreo escalados.
            w (float): Pesos escalados.

    """

    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w


def funcInt(x):

    """Evalúa puntos en la función a integrar.

    Ejemplos:

        >>> fInt(1)
        0.09070257317431829
        >>> fInt(2)
        67.0272099812317

    Args:
        x (float): Número flotante en el que se evalua la función.

    Returns:
        float: un número representando la evaluación del punto `x` en la función.
        """

    return x ** 6 - x ** 2 * np.sin(2 * x)

def polinomios(N2 = 2, N3 = 3, N4 = 4):

    """ Genera la aproximación de la función con 3 diferentes ordenes de polinomios de Legendre.

    Examples:
        >>> polinomios()
        Resultado de aproximación con polinomio orden 2: 306,8199344959197
        Resultado de aproximación con polinomio orden 3: 317,264151733829
        Resultado de aproximación con polinomio orden 4: 317,3453903341579
        Resultado correcto, polinomio orden 4: 317,3453903341579

    Args:
        N2 (int): Orden 2 del polinomio. Por defecto 2.
        N3 (int): Orden 3 del polinomio. Por defecto 3.
        N4 (int): Orden 4 del polinomio. Por defecto 4.

    Outputs:
        Imprime resultados de aproximaciones de la integral por polinomios de Legendre de los ordenes por defecto y el resultado exacto.

        Note:
            Esta función no retorna valores, solo imprime resultados.

    """

    x2, w2 = gaussxw(N2)
    x2Esc, w2Esc = gaussxwab(1, 3, x2, w2)

    x3, w3 = gaussxw(N3)
    x3Esc, w3Esc = gaussxwab(1, 3, x3, w3)

    x4, w4 = gaussxw(N4)
    x4Esc, w4Esc = gaussxwab(1, 3, x4, w4)

    func2 = np.sum(w2Esc * funcInt(x2Esc))
    func3 = np.sum(w3Esc * funcInt(x3Esc))
    func4 = np.sum(w4Esc * funcInt(x4Esc))

    print("Resultado de aproximación con polinomio orden 2: " + str(func2))
    print("Resultado de aproximación con polinomio orden 3: " + str(func3))
    print("Resultado de aproximación con polinomio orden 4: " + str(func4))
    print("Resultado correcto, polinomio orden 4: " + str(func4))
