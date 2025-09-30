La idea principal es poder observar la integral como una suma de un polinomio de la siguiente forma: $\int_{a}^{b}dxf(x) \approx \sum_{k=1}^{N} w_{k}f(x)_{k}$ donde:

$f(x)$ es la función a integrar.//
$w_{k}$ son los llamados "pesos".//
$x_{k}$ son los puntos de muestro de la función.

Los puntos de muestreo en la cuadratura Gaussiana se escogen de tal manera que no son equidistantes, lo que permite más grados de libertad (mayor número de pará,etros libres que se pueden ajustar) para la discretización en N subregiones, permitiendo que la aproximación se exacta para un polinomio de orden $2N - 1$.

A pesar de que la aproximación exacta se alcanza con unos pocos puntos de muestreo, la cuadratura Gaussiana se vuelve problemática en funciones que tienen regiones no muy bien comportadas, haciendo que se requieran de más puntos de muestreo, además, evaluar el error con este método es muy complicado si se quiere saber de manera precisa.

En este módulo en específico, se usa la cuadratura Gaussiana con los polinomios de Legendre, los cuales son un sistema de polinomios ortogonales que pueden ser definidos de manera recursiva y dentro del intervalo [-1, 1]
