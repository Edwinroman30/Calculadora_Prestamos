#  SISTEMA CALCULADORA DE PRÉSTAMOS .

Este script esta basado en mi practica final de Introducción a la Programación, la cual consiste en realizar como su nombre lo indica: una calculadora prestamos o SISTEMA CALCULADORA DE PRÉSTAMOS usando el lenguaje de programación Python. También como requisito se deben usar distintas estructuras de datos y usar el paradigma de Programación Orientada a Objetos (POO).

**Instalación:**

Instalar Tabulate con el instalador PIP:

`$ pip install tabulate`

Instalar utilizando un proxy:

`$ pip install tabulate --proxy http://user:passw@srv_proxy:puerto`


**Modulos usados:**
- Tabulate.
- Datetime.


Para determinar la cuota:
$$
C = i * p / (1-(1+i)^{-n} )
$$
Donde 

> **C** = Cuota.
> **i** = Tasa anual Porcentaje (Pero debe de ser mensual, debido a que la formula trabaja con la tasa mensual, lo pedí  anual porque el ejemplo lo pedía de esa manera, de igual forma en el algoritmo la convertí a mensual).
> **p** = Monto.
> **n** = Plazo en meses.


**Consideraciones a tomar antes de llevar a cabo la formula de la cuota:**

Para llevar la **Tasa anual** a **Tasa mensual**, procedemos a lo siguiente:

$$
Tm= Ta/12
$$

Donde:

> **Tm** = Tasa Mensual.
> **Ta** = Tasa anual.

Para que quede en forma de porcentaje, que es la forma en la que trabaja la formula solo se le debe hacer lo siguiente:

$$
Tm= (Tm/100)
$$

De esta forma nuestra tasa estará de manera en forma de porcentaje lista para trabajar en la formula de la cuota.

**Balance o Saldo Inicial:**
En caso del programa el balance o saldo inicial (Osea el primero) va ha ser el insertado por primera vez por el usuarios, los demás se generaran según el ciclo y se toman en cuenta las siguientes formulas o cálculos.

 - Balance o Saldo Inicial = Saldo Inicial - Capital.

**Interés Generado :**

 - Interés_generado = Saldo_Inicial - Interés.

**Capital:**

 - Capital = Cuota - Interés Generado.

La cuota siempre va ha ser la misma, por lo que podemos tomar como ejemplo el siguiente esquema que realice con a la hora de realizar el algoritmos:

<center>
<img src="Proceso_de_algoritmacion.jpg" width="100%" heigth="600px">
</center>


**BY: Edwin Roman**