---
icon: octicons/pivot-column-24
tags:
  - Paquetes de terceros
  - Ciencia de datos
  - Pandas
---

# Series { #series }

Podríamos pensar en una **serie** como un [`ndarray`](../numpy.md#ndarray) en el que cada valor tiene asignado una etiqueta (índice) y además admite un título (nombre).

## Creación { #create }

Veamos varios _mecanismos de creación de series_, con el objetivo de conseguir los valores $[1,2,3]$:

=== "Usando una lista"

    ```pycon
    >>> pd.Series([1, 2, 3])
    0    1
    1    2
    2    3
    dtype: int64
    ```

    !!! note "Índice por defecto"
    
        El índice por defecto (etiquetas de los datos) empieza en 0 y usa números enteros positivos.

=== "Con índice personalizado"

    ```pycon
    >>> pd.Series(range(1, 4), index=['a', 'b', 'c'])
    a    1
    b    2
    c    3
    dtype: int64
    ```

=== "Usando un diccionario"

    ```pycon
    >>> items = {'a': 1, 'b': 2, 'c': 3}
    
    >>> pd.Series(items)
    a    1
    b    2
    c    3
    dtype: int64
    ```

Ninguna de las series anteriores tienen nombre. Lo podemos hacer usando el parámetro `name` en la creación de la serie:

```pycon
>>> pd.Series([1, 2, 3], name='integers')
0    1
1    2
2    3
Name: integers, dtype: int64
```
    
!!! exercise "Ejercicio"

    Crea una serie de pandas con valores enteros en el intervalo $[1,26]$ y etiquetas `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`. Busca una manera ^^programática^^ (no manual) de hacerlo (recuerda el módulo [`string`](../../../stdlib/text-processing/string.md)).

    [:material-lightbulb: Solución](../files/pandas/create_series.py)

## Atributos { #attrs }

Las [series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) en pandas contienen gran cantidad de atributos. A continuación destacaremos algunos de ellos.

Para ilustrar los diferentes <span class="example">ejemplos:material-flash:</span> de todo este capítulo vamos a usar datos de **gases nobles**[^1]:

<div class="grid cards" markdown>

-   Construcción de la serie:

    ```pycon
    >>> density = pd.Series({#(1)!
    ...     'Helio': 0.1785,
    ...     'Neón': 0.9002,
    ...     'Argón': 1.7818,
    ...     'Kriptón': 3.708,
    ...     'Xenón': 5.851,
    ...     'Radón': 9.97
    ... }, name='Gas Density')
    ```
    { .annotate }
    
    1. Densidad de los gases nobles medida en $kg/m^3$

-   Visualización de la serie:

    ```pycon
    >>> density
    Helio      0.1785
    Neón       0.9002
    Argón      1.7818
    Kriptón    3.7080
    Xenón      5.8510
    Radón      9.9700
    Name: Gas Density, dtype: float64
    ```
    
</div>

=== "Índice"

    ```pycon
    >>> density.index
    Index(['Helio', 'Neón', 'Argón', 'Kriptón', 'Xenón', 'Radón'], dtype='object')
    ```

=== "Valores"

    ```pycon
    >>> density.values
    array([0.1785, 0.9002, 1.7818, 3.708 , 5.851 , 9.97  ])
    ```

=== "Tipo de datos"

    ```pycon
    >>> density.dtype
    dtype('float64')
    ```

=== "Nombre"

    ```pycon
    >>> density.name
    'Gas Density'    
    ```

=== "Memoria ocupada"

    ```pycon
    >>> employees.nbytes
    48
    ```

=== "Número de registros"

    ```pycon
    >>> employees.size
    6 
    ```

## Selección de registros { #record-select }

La selección de los datos se puede realizar desde múltiples aproximaciones. A continuación veremos las posiblidades que nos ofrece pandas para seleccionar/filtrar los registros de una serie.

### Selección usando indexado numérico { #index-select }

Para acceder a los registros por su posición (índice numérico) utilizamos el atributo `.iloc`:

```pycon
>>> density.iloc[0]#(1)!
np.float64(0.1785)

>>> density.iloc[-1]
np.float64(9.97)

>>> density.iloc[2:5]
Argón      1.7818
Kriptón    3.7080
Xenón      5.8510
Name: Gas Density, dtype: float64

>>> density.iloc[1:6:2]
Neón       0.9002
Kriptón    3.7080
Radón      9.9700
Name: Gas Density, dtype: float64
```
{ .annotate }

1. El uso `density[0]` está obsoleto y se recomienda la migración a `density.iloc[0]`. En caso de usarlo obtendríamos el siguiente _warning_: `FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use ser.iloc[pos]`.

### Selección usando etiquetas { #label-select }

En el caso de aquellas series que dispongan de un índice con etiquetas, podemos acceder a sus registros utilizando el atributo `loc`:

```pycon
>>> density.loc['Helio']#(1)!
np.float64(0.1785)

>>> density['Helio':'Xenón']
Helio      0.1785
Neón       0.9002
Argón      1.7818
Kriptón    3.7080
Xenón      5.8510
Name: Gas Density, dtype: float64

>>> density['Helio':'Xenón':2]
Helio    0.1785
Argón    1.7818
Xenón    5.8510
Name: Gas Density, dtype: float64
```
{ .annotate }

1. Equivale a la sintaxis :material-arrow-right-bold: `#!python density['Helio']` o incluso a `#!python density.Helio`.


### Fragmentos de comienzo y fin { #head-tail }

A nivel exploratorio, es bastante cómodo acceder a una porción inicial (o final) de los datos que manejamos. Esto se puede hacer de forma muy sencilla con series:

```pycon
>>> density.head(3)
Helio    0.1785
Neón     0.9002
Argón    1.7818
Name: Gas Density, dtype: float64

>>> density.tail(3)
Kriptón    3.708
Xenón      5.851
Radón      9.970
Name: Gas Density, dtype: float64
```

## Operaciones { #ops }

Si tenemos en cuenta que una serie contiene valores en formato `ndarray` podemos concluir que las [operaciones sobre arrays](https://aprendepython.es/pypi/datascience/numpy/#operaciones-sobre-arrays) son aplicables al caso de las series.

Veamos algunos <span class="example">ejemplos:material-flash:</span> de operaciones que podemos aplicar sobre series:

### Operaciones lógicas { #logical-ops }

Supongamos que queremos filtrar aquellos **gases cuya densidad sea mayor que 3 $kg/m^3$**:

```pycon
>>> density
Helio      0.1785
Neón       0.9002
Argón      1.7818
Kriptón    3.7080
Xenón      5.8510
Radón      9.9700
Name: Gas Density, dtype: float64

>>> density > 3#(1)!
Helio      False
Neón       False
Argón      False
Kriptón     True
Xenón       True
Radón       True
Name: Gas Density, dtype: bool

>>> density[density > 3]#(2)!
Kriptón    3.708
Xenón      5.851
Radón      9.970
Name: Gas Density, dtype: float64
```
{ .annotate }

1. Se obtiene una serie «booleana».
2. Para obtener los datos filtrados debemos aplicar la «máscara» anterior.

### Ordenación { #sort }

Es posible ordenar una serie por sus valores o por su índice:

=== "Ordenación de valores"

    ```pycon
    >>> density.sort_values()#(1)!
    Helio      0.1785
    Neón       0.9002
    Argón      1.7818
    Kriptón    3.7080
    Xenón      5.8510
    Radón      9.9700
    Name: Gas Density, dtype: float64
    ```
    { .annotate }
    
    1.  - Ordenación de una serie por sus valores.
        - El argumento `ascending=False` hará que la ordenación sea de mayor a menor.
        - El argumento `inplace=True` hará que se modifique la serie en vez de retornar una nueva.

=== "Ordenación de índice"

    ```pycon
    >>> density.sort_index()#(1)!
    Argón      1.7818
    Helio      0.1785
    Kriptón    3.7080
    Neón       0.9002
    Radón      9.9700
    Xenón      5.8510
    Name: Gas Density, dtype: float64
    ```
    { .annotate }

    1.  - Ordenación de una serie por su índice.
        - El argumento `ascending=False` hará que la ordenación sea de mayor a menor.
        - El argumento `inplace=True` hará que se modifique la serie en vez de retornar una nueva.

### Contando valores { #count }

```pycon
>>> marks = pd.Series([5, 5, 3, 6, 5, 2, 8, 3, 8, 7, 6])

>>> marks.value_counts()#(1)!
5    3
3    2
6    2
8    2
2    1
7    1
dtype: int64

>>> marks.nunique()#(2)!
6

>>> marks.count()#(3)!
11
```
{ .annotate }

1.  Tabla de frecuencias de la serie.
2.  Número de valores únicos de la serie.
3.  Número de valores no nulos de la serie.

### Operaciones aritméticas { #arith-ops }

Se distingue el tipo de operación en función de los operandos:

#### Operaciones entre series y escalaras { #series-scalar-ops }

En el siguiente <span class="example">ejemplo:material-flash:</span> pasamos la densidad de los gases nobles de $kg/m^3$ a $g/m^3$:

```pycon
>>> density * 1000
Helio       178.5
Neón        900.2
Argón      1781.8
Kriptón    3708.0
Xenón      5851.0
Radón      9970.0
Name: Gas Density, dtype: float64
```    

#### Operaciones entre series { #series-ops }

Para trabajar a posteriori, vamos a crear una nueva serie que almacena el **radio atómico** de los gases nobles medido en $nm$[^1]:

```pycon
>>> radius = pd.Series({
...     'Helio': 0.05,
...     'Neón': 0.07,
...     'Argón': 0.094,
...     'Kriptón': 0.109,
...     'Xenón': 0.13,
...     'Radón': 0.152
... }, name='Gas Radius')
```

Supongamos que en el siguiente <span class="example">ejemplo:material-flash:</span> queremos calcular la **proporción entre el radio y la densidad de cada gas noble**:

```pycon
>>> radius / density
Helio      0.280112
Neón       0.077760
Argón      0.052756
Kriptón    0.029396
Xenón      0.022218
Radón      0.015246
dtype: float64
```

!!! tip "Correspondencia de operación"

    Ten en cuenta que las operaciones se realizan entre registros que tienen el mismo índice (etiqueta).    
    

### Funciones estadísticas { #stats }

Existen multitud de funciones estadísticas que podemos aplicar a una serie. Dependiendo del tipo de dato con el que estamos trabajando, serán más útiles unas que otras.

Veamos dos <span class="example">ejemplos:material-flash:</span> de función estadística:

```pycon
>>> density.mean()
np.float64(3.731583333333333)

>>> radius.std()
np.float64(0.03772753194507516)
```

### Máximos y mínimos { #max-min }

El abanico de posibilidades es muy amplio en cuanto a la búsqueda de valores máximos y mínimos en una serie. Veamos lo que nos ofrece pandas a este respecto:

=== "Máximo/mínimo (valor)"

    ```pycon
    >>> density.min()#(1)!
    np.float64(0.1785)

    >>> density.max()#(2)!
    np.float64(9.97)
    ```
    { .annotate }
    
    1. Valor mínimo de la serie.
    2. Valor máximo de la serie.

=== "Máximo/mínimo (índice)"

    ```pycon
    >>> density.argmin()#(1)!
    np.int64(0)

    >>> density.argmax()#(2)!
    np.int64(5)
    ```
    { .annotate }

    1. Índice del valor mínimo de la serie.
    2. Índice del valor máximo de la serie.
    
=== "Máximo/mínimo (etiqueta)"

    ```pycon
    >>> density.idxmin()#(1)!
    'Helio'
    >>> density.idxmax()#(2)!
    'Radón'
    ```    
    { .annotate }

    1. Etiqueta del valor mínimo de la serie.
    2. Etiqueta del valor máximo de la serie.

=== "Máximo/mínimo ($n$)"

    ```pycon
    >>> density.nsmallest(3)#(1)!
    Helio    0.1785
    Neón     0.9002
    Argón    1.7818
    Name: Gas Density, dtype: float64

    >>> density.nlargest(3)#(2)!
    Radón      9.970
    Xenón      5.851
    Kriptón    3.708
    Name: Gas Density, dtype: float64
    ```    
    { .annotate }

    1. $n$ menores valores de la serie.
    2. $n$ mayores valores de la serie.

## Exportación de series { #export-series }

Suele ser bastante habitual intercambiar datos en distintos formatos (y aplicaciones). Para ello, pandas nos permite exportar una serie a multitud de formatos. Veamos algunos de ellos:

=== "De serie a lista"

    ```pycon
    >>> density.to_list()
    [0.1785, 0.9002, 1.7818, 3.708, 5.851, 9.97]
    ```

=== "De serie a diccionario"

    ```pycon
    >>> density.to_dict()
    {'Helio': 0.1785, 'Neón': 0.9002, 'Argón': 1.7818, 'Kriptón': 3.708, 'Xenón': 5.851, 'Radón': 9.97}
    ```

=== "De serie a CSV"

    ```pycon
    >>> density.to_csv()
    ',Gas Density\nHelio,0.1785\nNeón,0.9002\nArgón,1.7818\nKriptón,3.708\nXenón,5.851\nRadón,9.97\n'
    ```

=== "De serie a JSON"

    ```pycon
    >>> density.to_json()
    '{"Helio":0.1785,"Ne\\u00f3n":0.9002,"Arg\\u00f3n":1.7818,"Kript\\u00f3n":3.708,"Xen\\u00f3n":5.851,"Rad\\u00f3n":9.97}'
    ```

=== "De serie a DataFrame"

    ```pycon
    >>> density.to_frame()
             Gas Density
    Helio         0.1785
    Neón          0.9002
    Argón         1.7818
    Kriptón       3.7080
    Xenón         5.8510
    Radón         9.9700
    ```

Y muchos otros como: `to_clipboard()`, `to_numpy()`, `to_pickle()`, `to_string()`, `to_xarray()`, `to_excel()`, `to_hdf()`, `to_latex()`, `to_markdown()`, `to_period()`, `to_sql()` o `to_timestamp()`.


[^1]: Datos capturados desde [Wikipedia](https://es.wikipedia.org/wiki/Gases_nobles) en abril de 2025.
