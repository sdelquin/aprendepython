---
icon: simple/pandas
---

# Pandas { #pandas }

![Panda](../images/pandas/panda.jpg)
(1)
{ .annotate }

1. :fontawesome-regular-copyright: [Sid Balachandran](https://unsplash.com/@itookthose) :material-at: [Unsplash](https://unsplash.com) 

[`pandas`](https://pandas.pydata.org/docs/) es un paquete «open-source» especializada en la manipulación y el análisis de datos, ofreciendo estructuras de datos y operaciones para trabajar de forma sencilla y potente con gran cantidad de información.

## Instalación { #install }

```console
pip install pandas
```

## Modo de uso { #usage }

La forma más habitual de importar esta librería es utilizar el alias `pd`:

```pycon
>>> import pandas as pd
```

Si bien en [NumPy](../numpy.md) la estructura de datos fundamental es el `ndarray`, en pandas existen dos estructuras de datos sobre las que giran todas las operaciones:

- [x] [Series](series.md).
- [x] [Dataframes](dataframes.md).
