---
icon: octicons/table-24
tags:
  - Paquetes de terceros
  - Ciencia de datos
  - Pandas
---

# DataFrames { #dataframes }

Un DataFrame es una **estructura tabular compuesta por series**. Se trata del tipo de datos fundamental en pandas y sobre el que giran la mayoría de operaciones que podemos realizar.

Podemos ver un DataFrame como la «suma» de varias [series](series.md)[^1]...

![Dark image](../images/pandas/series-and-dataframes-dark.svg#only-dark)
![Light image](../images/pandas/series-and-dataframes-light.svg#only-light)

## Creación { #create }

Existen múltiples formas de crear un DataFrame en pandas.

### Desde diccionario de listas { #create-from-dict-of-lists }

Cada elemento del diccionario se convierte en una **columna**, donde su clave es el nombre y sus valores se despliegan en «vertical»:

```pycon
>>> data = {'A': [1, 2, 3], 'B': [4, 5, 6]}

>>> pd.DataFrame(data)#(1)!
    A  B
0  1  4
1  2  5
2  3  6
```
{ .annotate }

1.  - Cada clave del diccionario se convierte en el nombre de una columna.
    - Cada valor del diccionario (lista) se convierte en los valores de la columna.

### Desde lista de diccionarios { #create-from-list-of-dicts }

Cada elemento de la lista se convierte en una **fila**. Las claves de cada diccionario serán los nombres de las columnas y sus valores se despliegan en «horizontal»:

```pycon
>>> data = [{'A': 1, 'B': 2, 'C': 3}, {'A': 4, 'B': 5, 'C': 6}]

>>> pd.DataFrame(data)#(1)!
    A  B  C
0  1  2  3
1  4  5  6
```
{ .annotate }

1.  - Cada diccionario de la lista se convierte en una fila.
    - Cada clave del diccionario se convierte en el nombre de una columna.
    - Cada valor del diccionario se convierte en los valores de la columna.

### Desde lista de listas { #create-from-list-of-lists }

Cada elemento de la lista se convierte en una **fila** y sus valores se despliegan en «horizontal». Los nombres de las columnas deben pasarse como parámetro opcional:

```pycon
>>> data = [[1, 2], [3, 4], [5, 6]]

>>> pd.DataFrame(data, columns=['A', 'B'])#(1)!
    A  B
0  1  2
1  3  4
2  5  6
```
{ .annotate }

1.  - Cada lista de la lista se convierte en una fila.
    - Los nombres de las columnas se asignan mediante el argumento `columns`.

### Desde series { #create-from-series }

Constuir un DataFrame a partir de series es una aproximación bastante natural en el mundo pandas:

```pycon
>>> employees
Apple        164000
Samsung      270372
Google       190234
Microsoft    221000
Huawei       207000
Dell         133000
Meta          86482
Foxconn      767062
Sony         112994
Name: Tech Employees, dtype: int64

>>> revenues
Apple        394.33
Samsung      234.13
Google       282.84
Microsoft    198.27
Huawei        95.49
Dell         102.30
Meta         116.61
Foxconn      222.54
Sony          85.25
Name: Tech Revenues, dtype: float64

>>> pd.DataFrame({'employees': employees, 'revenues': revenues})#(1)!
            employees  revenues
Apple         164000    394.33
Samsung       270372    234.13
Google        190234    282.84
Microsoft     221000    198.27
Huawei        207000     95.49
Dell          133000    102.30
Meta           86482    116.61
Foxconn       767062    222.54
Sony          112994     85.25
```
{ .annotate }

1. Hemos usado la aproximación de un diccionario pero ahora con valores siendo series.

!!! exercise "Ejercicio"

    Crea el siguiente DataFrame[^2] en pandas:

    |Island        | Population|    Area| Province|
    |:-------------|----------:|-------:|--------:|
    |El Hierro     |      11423|  268.71|     TF|
    |Fuerteventura​ |     120021| 1665.74|     LP|
    |Gran Canaria  |     853262| 1560.10|     LP|
    |La Gomera     |      21798|  369.76|     TF|
    |Lanzarote​     |     156112|  888.07|     LP|
    |La Palma      |      83439|  708.32|     TF|
    |Tenerife      |     931646| 2034.38|     TF|

    Aclaraciones:

    - La superficie (_Area_) está expresada en $km^2$
    - `TF` :material-arrow-right-bold: Provincia de Santa Cruz de Tenerife.
    - `LPGC` :material-arrow-right-bold: Provincia de Las Palmas.

    :material-check-all:{ .blue } Utilizaremos este DataFrame en próximos ejercicios y lo identificaremos como **democan**.

    [:material-lightbulb: Solución](../files/pandas/create_dataframe.py)

### Gestión del índice { #index-management }

Cuando creamos un DataFrame, pandas autocompleta el índice con un valor entero autoincremental comenzando desde cero:

```pycon
>>> pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
   A  B
0  1  3
1  2  4
```

Si queremos convertir alguna columna en el índice de la tabla, podemos hacerlo así:

```pycon
>>> stats = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

>>> stats.set_index('A')#(1)!
   B
A
1  3
2  4
```
{ .annotate }

1.  - Columna A como índice.
    - Para cambiar el nombre `A` del índice podemos asignar un valor a `#!python df.index.name`

Podemos añadir un parámetro (en la creación) para especificar los valores que queremos incluir en el índice:

```pycon
>>> pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['R1', 'R2'])
    A  B
R1  1  3
R2  2  4
```

En aquellos DataFrames que disponen de un índice etiquetado, es posible resetearlo:

```pycon
>>> pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['R1', 'R2']).reset_index()
  index  A  B
0    R1  1  3
1    R2  2  4
```

!!! exercise "Ejercicio"

    Haz que la columna _Island_ se convierta en el índice del DataFrame **democan**:

    ```pycon
                   Population     Area Province
    Island
    El Hierro           11423   268.71       TF
    Fuerteventura      120021  1665.74       LP
    Gran Canaria       853262  1560.10       LP
    La Gomera           21798   369.76       TF
    Lanzarote          156112   888.07       LP
    La Palma            83439   708.32       TF
    Tenerife           931646  2034.38       TF
    ```

    [:material-lightbulb: Solución](../files/pandas/index_dataframe.py)

### Lectura de fuentes externas { #read }

Lo más habitual cuando se trabaja en ciencia de datos es tener la información en distintas fuentes auxiliares: bases de datos, ficheros, llamadas remotas a APIs, etc. Pandas nos ofrece una variedad enorme de funciones para cargar datos desde, prácticamente, cualquier origen.

|Función|Explicación|
|---|---|
|[read_pickle](https://pandas.pydata.org/docs/reference/api/pandas.read_pickle.html)|Lectura de datos en formato pickle (Python)|
|[read_table](https://pandas.pydata.org/docs/reference/api/pandas.read_table.html)|Lectura de ficheros con delimitadores|
|[read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)|Lectura de ficheros .csv|
|[read_fwf](https://pandas.pydata.org/docs/reference/api/pandas.read_fwf.html)|Lectura de tablas con líneas de ancho fijo|
|[read_clipboard](https://pandas.pydata.org/docs/reference/api/pandas.read_clipboard.html)|Lectura de texto del portapapeles|
|[read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)|Lectura de ficheros excel|
|[read_json](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html)|Lectura de ficheros json|
|[read_html](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html)|Lectura de tablas HTML|
|[read_xml](https://pandas.pydata.org/docs/reference/api/pandas.read_xml.html)|Lectura de documentos XML|
|[read_hdf](https://pandas.pydata.org/docs/reference/api/pandas.read_hdf.html)|Lectura de objetos pandas almacenados en fichero|
|[read_feather](https://pandas.pydata.org/docs/reference/api/pandas.read_feather.html)|Lectura de objetos en formato "feather"|
|[read_parquet](https://pandas.pydata.org/docs/reference/api/pandas.read_parquet.html)|Lectura de objetos en formato "parquet"|
|[read_orc](https://pandas.pydata.org/docs/reference/api/pandas.read_orc.html)|Lectura de objetos en formato ORC|
|[read_sas](https://pandas.pydata.org/docs/reference/api/pandas.read_sas.html)|Lectura de ficheros SAS|
|[read_spss](https://pandas.pydata.org/docs/reference/api/pandas.read_spss.html)|Lectura de ficheros SPSS|
|[read_sql_table](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_table.html)|Lectura de tabla SQL|
|[read_sql_query](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html)|Lectura de una consulta SQL|
|[read_sql](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html)|Wrapper para ``read_sql_table`` y ``read_sql_query``|
|[read_gbq](https://pandas.pydata.org/docs/reference/api/pandas.read_gbq.html)|Lectura de datos desde Google BigQuery|
|[read_stata](https://pandas.pydata.org/docs/reference/api/pandas.read_stata.html)|Lectura de ficheros Stata|

!!! tip "Escritura"

    Todas estas funciones tienen su equivalente para escribir datos en los distintos formatos. En vez de `read_` habría que usar el prefijo `to_`. Por ejemplo: `.to_csv()`, `.to_json()` o`.to_sql()` 

De aquí en adelante usaremos el fichero [`tech.csv`](../files/pandas/tech.csv)[^1] que contiene la lista de las mayores empresas tecnológicas por ingresos totales (en billones de dólares)[^3]:

```pycon
>>> df = pd.read_csv('tech.csv', index_col='Company')#(1)!

>>> df
                     Revenue  Employees             City        Country
Company
Amazon                574.80    1525000          Seattle  United States
Apple                 394.33     164000        Cupertino  United States
Alphabet              282.84     190234    Mountain View  United States
Samsung Electronics   234.13     270372            Suwon    South Korea
Foxconn               222.54     767062  New Taipei City         Taiwan
Microsoft             198.27     221000          Redmond  United States
Jingdong              152.80     310000          Beijing          China
Alibaba               130.35     204891           Yuhang          China
AT&T                  122.40     149900           Dallas  United States
Meta                  116.61      86482       Menlo Park  United States
Deutsche Telekom      112.00     205000             Bonn        Germany
Dell Technologies     102.30     133000       Round Rock  United States
Huawei                 95.49     207000         Shenzhen          China
Sony                   85.25     112994            Tokyo          Japan
Tencent                82.44     108436         Shenzhen          China
Hitachi                80.39     322525            Tokyo          Japan
TSMC                   76.02      73090  New Taipei City         Taiwan
LG Electronics         64.95      74000            Seoul    South Korea
Intel                  63.05     131900      Santa Clara  United States
HP Inc.                62.98      53000        Palo Alto  United States
Lenovo                 61.95      71500        Hong Kong      Hong Kong
Panasonic              61.90     233391            Osaka          Japan
Accenture              61.59     721000           Dublin        Ireland
Nvidia                 60.93      29600      Santa Clara  United States
IBM                    60.53     303100           Armonk  United States
```
{ .annotate }

1. Es habitual usar `df` como nombre de variable para un DataFrame.

!!! exercise "Ejercicio"

    Carga el conjunto de datos **democan** desde [`democan.csv`](../files/pandas/democan.csv) en un DataFrame `df` indicando que la columna `Island` sea su índice.

    :material-web: También es posible cargar el «dataset» a través de la URL que conseguimos con botón derecho: copiar enlace.

    [:material-lightbulb: Solución](../files/pandas/load_dataframe.py)

## Características { #features }

Veamos las principales características de un DataFrame.

### Muestra parcial { #chunks }

Para «echar un vistazo» a los datos, existen dos funciones muy recurridas:

```pycon
>>> df.head()#(1)!
                        Revenue  Employees             City        Country
Company
Amazon                574.80    1525000          Seattle  United States
Apple                 394.33     164000        Cupertino  United States
Alphabet              282.84     190234    Mountain View  United States
Samsung Electronics   234.13     270372            Suwon    South Korea
Foxconn               222.54     767062  New Taipei City         Taiwan

>>> df.tail()#(2)!
            Revenue  Employees         City        Country
Company
Lenovo       61.95      71500    Hong Kong      Hong Kong
Panasonic    61.90     233391        Osaka          Japan
Accenture    61.59     721000       Dublin        Ireland
Nvidia       60.93      29600  Santa Clara  United States
IBM          60.53     303100       Armonk  United States
```
{ .annotate }

1. También admite un parámetro indicando el número de registros a mostrar.
2. También admite un parámetro indicando el número de registros a mostrar.

### Información sobre los datos { #info }

Pandas ofrece algunas funciones que proporcionan un cierto «resumen» de los datos a nivel descriptivo. Veamos algunas de ellas:

=== "Información sobre columnas"

    ```pycon
    >>> df.info()#(1)!
    <class 'pandas.core.frame.DataFrame'>
    Index: 25 entries, Amazon to IBM
    Data columns (total 4 columns):
        #   Column     Non-Null Count  Dtype
    ---  ------     --------------  -----
        0   Revenue    25 non-null     float64
        1   Employees  25 non-null     int64
        2   City       25 non-null     object
        3   Country    25 non-null     object
    dtypes: float64(1), int64(1), object(2)
    memory usage: 1000.0+ bytes
    ```
    { .annotate }
    
    1. Información sobre columnas.

=== "Resumen de variables"

    ```pycon
    >>> df.describe()#(1)!
                Revenue     Employees
    count   25.000000  2.500000e+01
    mean   142.433600  2.667391e+05
    std    122.595103  3.177151e+05
    min     60.530000  2.960000e+04
    25%     63.050000  1.084360e+05
    50%     95.490000  1.902340e+05
    75%    152.800000  2.703720e+05
    max    574.800000  1.525000e+06
    ```
    { .annotate }

    1.  - Descripción (resumen) de las variables numéricas.
        - Devuelve un DataFrame.

=== "Uso de memoria"

    ```pycon
    >>> df.memory_usage()#(1)!
    Index        200
    Revenue      200
    Employees    200
    City         200
    Country      200
    dtype: int64
    ```
    { .annotate }

    1.  - Uso de memoria.
        - Devuelve una serie.

### Atributos { #attributes }

=== "Tamaños y dimensiones"

    ```pycon
    >>> df.shape
    (25, 4)

    >>> df.size
    100

    >>> df.ndim
    2
    ```

=== "Índice, columnas y valores"

    ```pycon
    >>> df.index
    Index(['Amazon', 'Apple', 'Alphabet', 'Samsung Electronics', 'Foxconn',
           'Microsoft', 'Jingdong', 'Alibaba', 'AT&T', 'Meta', 'Deutsche Telekom',
           'Dell Technologies', 'Huawei', 'Sony', 'Tencent', 'Hitachi', 'TSMC',
           'LG Electronics', 'Intel', 'HP Inc.', 'Lenovo', 'Panasonic',
           'Accenture', 'Nvidia', 'IBM'],
          dtype='object', name='Company')

    >>> df.columns
    Index(['Revenue', 'Employees', 'City', 'Country'], dtype='object')

    >>> df.values
    array([[574.8, 1525000, 'Seattle', 'United States'],
           [394.33, 164000, 'Cupertino', 'United States'],
           [282.84, 190234, 'Mountain View', 'United States'],
           [234.13, 270372, 'Suwon', 'South Korea'],
           [222.54, 767062, 'New Taipei City', 'Taiwan'],
           [198.27, 221000, 'Redmond', 'United States'],
           [152.8, 310000, 'Beijing', 'China'],
           [130.35, 204891, 'Yuhang', 'China'],
           [122.4, 149900, 'Dallas', 'United States'],
           [116.61, 86482, 'Menlo Park', 'United States'],
           [112.0, 205000, 'Bonn', 'Germany'],
           [102.3, 133000, 'Round Rock', 'United States'],
           [95.49, 207000, 'Shenzhen', 'China'],
           [85.25, 112994, 'Tokyo', 'Japan'],
           [82.44, 108436, 'Shenzhen', 'China'],
           [80.39, 322525, 'Tokyo', 'Japan'],
           [76.02, 73090, 'New Taipei City', 'Taiwan'],
           [64.95, 74000, 'Seoul', 'South Korea'],
           [63.05, 131900, 'Santa Clara', 'United States'],
           [62.98, 53000, 'Palo Alto', 'United States'],
           [61.95, 71500, 'Hong Kong', 'Hong Kong'],
           [61.9, 233391, 'Osaka', 'Japan'],
           [61.59, 721000, 'Dublin', 'Ireland'],
           [60.93, 29600, 'Santa Clara', 'United States'],
           [60.53, 303100, 'Armonk', 'United States']], dtype=object)
    ```

## Acceso { #access }

Es fundamental conocer la estructura de un DataFrame para su adecuado manejo:

![Dark image](../images/pandas/dataframe-structure-dark.svg#only-dark)
![Light image](../images/pandas/dataframe-structure-light.svg#only-light)

### Acceso a filas { #row-access }

Si queremos acceder a las filas de un conjunto de datos **mediante la posición (índice numérico)** del registro usamos el atributo `iloc`:

```pycon
>>> df.iloc[0]#(1)!
Revenue              574.8
Employees          1525000
City               Seattle
Country      United States
Name: Amazon, dtype: object

>>> df.iloc[-1]#(2)!
Revenue              60.53
Employees           303100
City                Armonk
Country      United States
Name: IBM, dtype: object

>>> df.iloc[3:5]#(3)!
                     Revenue  Employees             City      Country
Company
Samsung Electronics   234.13     270372            Suwon  South Korea
Foxconn               222.54     767062  New Taipei City       Taiwan

>>> df.iloc[::5]#(4)!
                  Revenue  Employees       City        Country
Company
Amazon             574.80    1525000    Seattle  United States
Microsoft          198.27     221000    Redmond  United States
Deutsche Telekom   112.00     205000       Bonn        Germany
Hitachi             80.39     322525      Tokyo          Japan
Lenovo              61.95      71500  Hong Kong      Hong Kong
```
{ .annotate }

1.  - Acceso a la primera fila.
    - El acceso a un registro individual devuelve una serie.
2.  - Acceso a la última fila.
    - El acceso a un registro individual devuelve una serie.
3. Acceso a la segunda y tercera fila.
4. Acceso a todas las filas «saltando» de 5 en 5.

Si queremos acceder a las filas de un conjunto de datos **mediante la etiqueta del registro** usamos el atributo `loc`:

```pycon
>>> df.loc['Apple']#(1)!
Revenue             394.33
Employees           164000
City             Cupertino
Country      United States
Name: Apple, dtype: object

>>> df.loc['IBM']#(2)!
Revenue              60.53
Employees           303100
City                Armonk
Country      United States
Name: IBM, dtype: object

>>> df.loc['Alphabet':'Microsoft']#(3)!
                     Revenue  Employees             City        Country
Company
Alphabet              282.84     190234    Mountain View  United States
Samsung Electronics   234.13     270372            Suwon    South Korea
Foxconn               222.54     767062  New Taipei City         Taiwan
Microsoft             198.27     221000          Redmond  United States
```
{ .annotate }

1.  - Acceso al registro con etiqueta _Apple_.
    - El acceso a un registro individual devuelve una serie.
2.  - Acceso al registro con etiqueta _IBM_.
    - El acceso a un registro individual devuelve una serie.
3. Acceso al rango de registros entre las etiquetas _Alphabet_ y _Microsoft_.

### Acceso a columnas { #col-access }

El acceso a columnas se realiza directamente utilizando corchetes, como si fuera un diccionario:

```pycon
>>> df['Revenue']#(1)!
Company
Amazon                 574.80
Apple                  394.33
Alphabet               282.84
Samsung Electronics    234.13
Foxconn                222.54
Microsoft              198.27
Jingdong               152.80
Alibaba                130.35
AT&T                   122.40
Meta                   116.61
Deutsche Telekom       112.00
Dell Technologies      102.30
Huawei                  95.49
Sony                    85.25
Tencent                 82.44
Hitachi                 80.39
TSMC                    76.02
LG Electronics          64.95
Intel                   63.05
HP Inc.                 62.98
Lenovo                  61.95
Panasonic               61.90
Accenture               61.59
Nvidia                  60.93
IBM                     60.53
Name: Revenue, dtype: float64
```
{ .annotate }

1. El acceso a una columna individual devuelve una serie.

Se pueden seleccionar varias columnas a la vez pasando una lista con sus nombres:

```pycon
>>> df[['Employees', 'City']].head()#(1)!
                     Employees             City
Company
Amazon                 1525000          Seattle
Apple                   164000        Cupertino
Alphabet                190234    Mountain View
Samsung Electronics     270372            Suwon
Foxconn                 767062  New Taipei City
```
{ .annotate }

1. Devuelve un DataFrame.

Esta misma sintaxis permite la **reordenación de las columnas** de un DataFrame, si asignamos el resultado a la misma (u otra) variable:

```pycon
>>> df_reordered = df[['City', 'Country', 'Revenue', 'Employees']]

>>> df_reordered.head()
                                City        Country  Revenue  Employees
Company
Amazon                       Seattle  United States   574.80    1525000
Apple                      Cupertino  United States   394.33     164000
Alphabet               Mountain View  United States   282.84     190234
Samsung Electronics            Suwon    South Korea   234.13     270372
Foxconn              New Taipei City         Taiwan   222.54     767062
```

### Acceso a filas y columnas { #row-col-access }

Si mezclamos los dos accesos anteriores podemos seleccionar datos de forma muy precisa. Como siempre, partimos del «dataset» de empresas tecnológicas:

```pycon
>>> df.head()
                     Revenue  Employees             City        Country
Company
Amazon                574.80    1525000          Seattle  United States
Apple                 394.33     164000        Cupertino  United States
Alphabet              282.84     190234    Mountain View  United States
Samsung Electronics   234.13     270372            Suwon    South Korea
Foxconn               222.54     767062  New Taipei City         Taiwan
```

Acceso al **primer valor del número de empleados/as**. Formas equivalentes de hacerlo:

```pycon
>>> df.iloc[0, 0]
np.float64(574.8)

>>> df.loc['Amazon', 'Revenue']
np.float64(574.8)
```

Acceso a **ciudad y país de las empresas Sony, Panasonic y Lenovo**:

```pycon
>>> df.loc[['Sony', 'Panasonic', 'Lenovo'], ['City', 'Country']]
                City    Country
Company
Sony           Tokyo      Japan
Panasonic      Osaka      Japan
Lenovo     Hong Kong  Hong Kong
```

Acceso a la **última columna** del DataFrame:

```pycon
>>> df.iloc[:, -1]
Company
Amazon                 United States
Apple                  United States
Alphabet               United States
Samsung Electronics      South Korea
Foxconn                       Taiwan
Microsoft              United States
Jingdong                       China
Alibaba                        China
AT&T                   United States
Meta                   United States
Deutsche Telekom             Germany
Dell Technologies      United States
Huawei                         China
Sony                           Japan
Tencent                        China
Hitachi                        Japan
TSMC                          Taiwan
LG Electronics           South Korea
Intel                  United States
HP Inc.                United States
Lenovo                     Hong Kong
Panasonic                      Japan
Accenture                    Ireland
Nvidia                 United States
IBM                    United States
Name: Country, dtype: object
```

Acceso a las **tres últimas filas (empresas) y a las dos primeras columnas**:

```pycon
>>> df.iloc[-3:, :2]
           Revenue  Employees
Company
Accenture    61.59     721000
Nvidia       60.93      29600
IBM          60.53     303100
```

Acceso a las **filas que van desde «Meta» a «Huawei» y a las columnas que van desde «Revenue» hasta «City»**:

```pycon
>>> df.loc['Meta':'Huawei', 'Revenue':'City']
                   Revenue  Employees        City
Company
Meta                116.61      86482  Menlo Park
Deutsche Telekom    112.00     205000        Bonn
Dell Technologies   102.30     133000  Round Rock
Huawei               95.49     207000    Shenzhen
```

### Selección condicional { #conditional-selection }

Es posible aplicar ciertas condiciones en la selección de los datos para obtener el subconjunto que estemos buscando. Veremos distintas aproximaciones a esta técnica.

Supongamos que queremos seleccionar aquellas **empresas con base en Estados Unidos**. Si aplicamos la condición sobre la columna obtendremos una serie de tipo «booleano» en la que se indica para qué registros se cumple la condición (incluyendo el índice):

```pycon
>>> df['Country'] == 'United States'
Company
Amazon                  True
Apple                   True
Alphabet                True
Samsung Electronics    False
Foxconn                False
Microsoft               True
Jingdong               False
Alibaba                False
AT&T                    True
Meta                    True
Deutsche Telekom       False
Dell Technologies       True
Huawei                 False
Sony                   False
Tencent                False
Hitachi                False
TSMC                   False
LG Electronics         False
Intel                   True
HP Inc.                 True
Lenovo                 False
Panasonic              False
Accenture              False
Nvidia                  True
IBM                     True
Name: Country, dtype: bool
```

Si aplicamos esta «máscara» al conjunto original de datos, obtendremos las empresas que estamos buscando:

```pycon
>>> df[df['Country'] == 'United States']
                   Revenue  Employees           City        Country
Company
Amazon              574.80    1525000        Seattle  United States
Apple               394.33     164000      Cupertino  United States
Alphabet            282.84     190234  Mountain View  United States
Microsoft           198.27     221000        Redmond  United States
AT&T                122.40     149900         Dallas  United States
Meta                116.61      86482     Menlo Park  United States
Dell Technologies   102.30     133000     Round Rock  United States
Intel                63.05     131900    Santa Clara  United States
HP Inc.              62.98      53000      Palo Alto  United States
Nvidia               60.93      29600    Santa Clara  United States
IBM                  60.53     303100         Armonk  United States
```

También es posible aplicar condiciones compuestas. Supongamos que necesitamos selecionar aquellas **empresas con más de 100 billones[^3] de dólares de ingresos y más de 100000 empleados/as**:

```pycon
>>> revenue_condition = df['Revenue'] > 100
>>> employees_condition = df['Employees'] > 100_000

>>> df[revenue_condition & employees_condition]
                     Revenue  Employees             City        Country
Company
Amazon                574.80    1525000          Seattle  United States
Apple                 394.33     164000        Cupertino  United States
Alphabet              282.84     190234    Mountain View  United States
Samsung Electronics   234.13     270372            Suwon    South Korea
Foxconn               222.54     767062  New Taipei City         Taiwan
Microsoft             198.27     221000          Redmond  United States
Jingdong              152.80     310000          Beijing          China
Alibaba               130.35     204891           Yuhang          China
AT&T                  122.40     149900           Dallas  United States
Deutsche Telekom      112.00     205000             Bonn        Germany
Dell Technologies     102.30     133000       Round Rock  United States
```

Los operadores lógicos que se pueden utilizar para combinar condiciones de selección son los siguientes:

| Operador | Significado |
| --- | --- |
| `|` | «or» lógico |
| `&` | «and» lógico |
| `~` | «not» lógico |
| `^` | «xor» lógico |

Imaginemos ahora que estamos buscando aquellas **empresas establecidas en Shenzen o Tokyo**. Una posible aproximación sería utilizar una condición compuesta, pero existe la función `isin()` que nos permite comprobar si un valor está dentro de una lista de opciones:

```pycon
>>> mask = df['City'].isin(['Shenzhen', 'Tokyo'])

>>> df[mask]
         Revenue  Employees      City Country
Company
Huawei     95.49     207000  Shenzhen   China
Sony       85.25     112994     Tokyo   Japan
Tencent    82.44     108436  Shenzhen   China
Hitachi    80.39     322525     Tokyo   Japan
```

!!! exercise "Ejercicio"

    Encuentra los siguientes subconjuntos del dataset [`democan`](../files/pandas/democan.csv):

    1. Filas con los datos de las islas de El Hierro y La Gomera.
    2. Columna de provincia.
    3. Columna de área para todas las islas «saltando de dos en dos».
    4. Islas con más de $1000 km^2$ de extensión.

    [:material-lightbulb: Solución](../files/pandas/df_access.py)

#### Selección mediante «query» { #query-select }

Pandas provee una alternativa para la selección condicional de registros a través de la función [`query()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html). Admite una sintaxis de consulta mediante operadores de comparación.


Veamos las mismas consultas de <span class="example">ejemplo:material-flash:</span> que para el apartado anterior:

```pycon
>>> df.query('Country == "United States"')
                   Revenue  Employees           City        Country
Company
Amazon              574.80    1525000        Seattle  United States
Apple               394.33     164000      Cupertino  United States
Alphabet            282.84     190234  Mountain View  United States
Microsoft           198.27     221000        Redmond  United States
AT&T                122.40     149900         Dallas  United States
Meta                116.61      86482     Menlo Park  United States
Dell Technologies   102.30     133000     Round Rock  United States
Intel                63.05     131900    Santa Clara  United States
HP Inc.              62.98      53000      Palo Alto  United States
Nvidia               60.93      29600    Santa Clara  United States
IBM                  60.53     303100         Armonk  United States

>>> df.query('Revenue > 100 & Employees > 100_000')
                     Revenue  Employees             City        Country
Company
Amazon                574.80    1525000          Seattle  United States
Apple                 394.33     164000        Cupertino  United States
Alphabet              282.84     190234    Mountain View  United States
Samsung Electronics   234.13     270372            Suwon    South Korea
Foxconn               222.54     767062  New Taipei City         Taiwan
Microsoft             198.27     221000          Redmond  United States
Jingdong              152.80     310000          Beijing          China
Alibaba               130.35     204891           Yuhang          China
AT&T                  122.40     149900           Dallas  United States
Deutsche Telekom      112.00     205000             Bonn        Germany
Dell Technologies     102.30     133000       Round Rock  United States

>>> df.query('City in ["Shenzhen", "Tokyo"]')
         Revenue  Employees      City Country
Company
Huawei     95.49     207000  Shenzhen   China
Sony       85.25     112994     Tokyo   Japan
Tencent    82.44     108436  Shenzhen   China
Hitachi    80.39     322525     Tokyo   Japan
```

!!! tip "Nombres de columna"

    Si los nombres de columna contienen espacios, se puede hacer referencias a ellas con comillas invertidas.

#### Comparativa en consultas { #query-benchmark }

Hemos visto dos métodos para realizar consultas (o filtrado) en un DataFrame: usando selección booleana con corchetes y usando la función `query`. ¿Ambos métodos son igual de eficientes en términos de rendimiento?

Haremos una comparativa muy simple para tener, al menos, una idea de sus órdenes de magnitud. En primer lugar creamos un DataFrame con 3 columnas y 1 millón de valores aleatorios enteros en cada una de ellas:

```pycon
>>> size = 1_000_000
>>> data = {
...     'A': np.random.randint(1, 100, size=size),
...     'B': np.random.randint(1, 100, size=size),
...     'C': np.random.randint(1, 100, size=size)
... }
>>> df = pd.DataFrame(data)
>>> df.shape
(1000000, 3)
```

Ahora realizaremos la misma consulta sobre el DataFrame aplicando los métodos ya vistos:

```pycon
>>> %timeit df[(df['A'] > 50) & (df['B'] < 50)]
3.29 ms ± 403 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)

>>> %timeit df.query('A > 50 & B < 50')
4.49 ms ± 179 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

Sin que esto sea en modo alguno concluyente, da la sensación de que `query()` añade un cierto «overhead»[^4] al filtrado y aumentan los tiempos de cómputo.

## Modificación { #modification }

### Modificando valores existentes { #mod-existent }

Partiendo del [acceso a los datos](#access) que ya hemos visto, podemos asignar valores sin mayor dificultad.

Pero antes de modificar el DataFrame original, vamos a hacer una copia del mismo:

```pycon
>>> df_mod = df.copy()
>>> df_mod.equals(df)#(1)!
True
```
{ .annotate }

1. Comprueba que todos los valores de cada DataFrame son iguales.

Supongamos que hemos cometido un **error en el número de empleados/as de Apple** y queremos corregirlo:

```pycon hl_lines="8"
>>> df_mod.loc['Apple']
Revenue             394.33
Employees           164000
City             Cupertino
Country      United States
Name: Apple, dtype: object

>>> df_mod.loc['Apple', 'Employees'] = 146_000

>>> df_mod.loc['Apple']
Revenue             394.33
Employees           146000
City             Cupertino
Country      United States
Name: Apple, dtype: object
```

Supongamos que no se había contemplado una **subida del 20% en los ingresos** (para todas las empresas) y queremos reflejarla:

```pycon
>>> df_mod['Revenue'] *= 1.20

>>> df_mod['Revenue'].head()
Company
Amazon                 689.760
Apple                  473.196
Alphabet               339.408
Samsung Electronics    280.956
Foxconn                267.048
Name: Revenue, dtype: float64
```

Supongamos que todas las empresas tecnológicas **mueven su sede a Tenerife (España)** y queremos reflejarlo:

```pycon
>>> df_mod['City'] = 'Tenerife'#(1)!
>>> df_mod['Country'] = 'Spain'#(2)!

>>> df_mod.head()
                     Revenue  Employees      City Country
Company
Amazon               689.760    1525000  Tenerife   Spain
Apple                473.196     146000  Tenerife   Spain
Alphabet             339.408     190234  Tenerife   Spain
Samsung Electronics  280.956     270372  Tenerife   Spain
Foxconn              267.048     767062  Tenerife   Spain
```
{ .annotate }

1. Se produce un «broadcast» o difusión del valor escalar en todos los registros del «dataset».
2. Se produce un «broadcast» o difusión del valor escalar en todos los registros del «dataset».

### Reemplazo de valores { #replace }

Hay una función muy importante en lo relativo a la modificación de valores. Se trata de `replace()` y admite una amplia variedad de parámetros. Se puede usar tanto para tipos numéricos como textuales.

Uno de los usos más habituales es la **recodificación**. Supongamos que queremos recodificar los países en [ISO3166 Alpha-3](https://es.wikipedia.org/wiki/ISO_3166-1_alfa-3) para el DataFrame de empresas tecnológicas:

```pycon
>>> iso3166 = {
...     'United States': 'USA',
...     'South Korea': 'KOR',
...     'Taiwan': 'TWN',
...     'China': 'CHN',
...     'Japan': 'JPN',
...     'Germany': 'DEU',
...     'Hong Kong': 'HKG',
...     'Ireland': 'IRL'
... }

>>> df['Country'].replace(iso3166)
Company
Amazon                 USA
Apple                  USA
Alphabet               USA
Samsung Electronics    KOR
Foxconn                TWN
Microsoft              USA
Jingdong               CHN
Alibaba                CHN
AT&T                   USA
Meta                   USA
Deutsche Telekom       DEU
Dell Technologies      USA
Huawei                 CHN
Sony                   JPN
Tencent                CHN
Hitachi                JPN
TSMC                   TWN
LG Electronics         KOR
Intel                  USA
HP Inc.                USA
Lenovo                 HKG
Panasonic              JPN
Accenture              IRL
Nvidia                 USA
IBM                    USA
Name: Country, dtype: object
```

!!! exercise "Ejercicio"

    Recodifica la columna _Province_ del «dataset» [`democan`](../files/pandas/democan.csv) de tal manera que aparezcan las provincias con el texto completo: _Santa Cruz de Tenerife_ y _Las Palmas de Gran Canaria_.

    [:material-lightbulb: Solución](../files/pandas/recoding.py)

### Insertando y borrando filas { #add-delete-rows }

Insertar una fila en un DataFrame es equivalente a [añadir una clave en un diccionario](../../../core/datastructures/dicts.md#add-modify), donde la clave es el índice (o etiqueta) de la fila en cuestión.

Supongamos que queremos incluir una **nueva empresa «Cisco»**:

```pycon hl_lines="11 20"
>>> cisco = pd.Series(
...     {'Revenue': 51_904, 'Employees': 75_900, 'City': 'San Jose', 'Country': 'United States'}
... )
>>> cisco
Revenue              51904
Employees            75900
City              San Jose
Country      United States
dtype: object

>>> df_mod.loc['Cisco'] = cisco

>>> df_mod.tail()
             Revenue  Employees      City        Country
Company
Panasonic     74.280   233391.0  Tenerife          Spain
Accenture     73.908   721000.0  Tenerife          Spain
Nvidia        73.116    29600.0  Tenerife          Spain
IBM           72.636   303100.0  Tenerife          Spain
Cisco      51904.000    75900.0  San Jose  United States
```

Imaginemos ahora que **Meta, Sony e Hitachi** caen en bancarrota y debemos eliminarlas de nuestro conjunto de datos:

```pycon hl_lines="1"
>>> df_mod = df_mod.drop(labels=['Meta', 'Sony', 'Hitachi'])

>>> df_mod.index#(1)!
Index(['Amazon', 'Apple', 'Alphabet', 'Samsung Electronics', 'Foxconn',
       'Microsoft', 'Jingdong', 'Alibaba', 'AT&T', 'Deutsche Telekom',
       'Dell Technologies', 'Huawei', 'Tencent', 'TSMC', 'LG Electronics',
       'Intel', 'HP Inc.', 'Lenovo', 'Panasonic', 'Accenture', 'Nvidia', 'IBM',
       'Cisco'],
      dtype='object', name='Company')
```
{ .annotate }

1. Las empresas eliminadas ya no aparecen en el índice.

### Insertando y borrando columnas { #add-delete-cols }

Insertar una columna en un DataFrame es equivalente a [añadir una clave en un diccionario](../../../core/datastructures/dicts.md#add-modify), donde la clave es el índice (o etiqueta) de la columna en cuestión.

Supongamos que queremos **añadir una columna «Expenses» (gastos)**. No manejamos esta información, así que, a modo de ejemplo, utilizaremos unos valores aleatorios:

```pycon hl_lines="6"
>>> expenses = np.random.randint(50, 500, size=23)
>>> expenses
array([396, 183, 419, 346, 378, 481, 376, 350, 229, 226, 486, 429, 285,
       291, 301, 277, 193,  55,  75, 406, 350, 372, 268])

>>> df_mod['Expenses'] = expenses

>>> df_mod.head()
                     Revenue  Employees      City Country  Expenses
Company
Amazon               689.760  1525000.0  Tenerife   Spain       396
Apple                473.196   146000.0  Tenerife   Spain       183
Alphabet             339.408   190234.0  Tenerife   Spain       419
Samsung Electronics  280.956   270372.0  Tenerife   Spain       346
Foxconn              267.048   767062.0  Tenerife   Spain       378
```

En el caso de que no nos haga falta una columna podemos borrarla fácilmente. Una opción sería utilizar la sentencia `del`, pero seguiremos con el uso de funciones propias de pandas. Imaginemos que queremos **eliminar la columna «Expenses»**:

```pycon hl_lines="4"
>>> df_mod.columns
Index(['Revenue', 'Employees', 'City', 'Country', 'Expenses'], dtype='object')

>>> df_mod = df_mod.drop(labels='Expenses', axis=1)#(1)!

>>> df_mod.columns
Index(['Revenue', 'Employees', 'City', 'Country'], dtype='object')
```
{ .annotate }

1. Recuerda que el parámetro `axis` indica en qué «dirección» estamos trabajando. Véase el [acceso a un DataFrame](#access).

!!! exercise "Ejercicio"

    Añade una nueva columna _Density_ a [`democan`](../files/pandas/democan.csv) de tal manera que represente la densidad de población de cada isla del archipiélago canario.

    [:material-lightbulb: Solución](../files/pandas/pop_density.py)

### Renombrando columnas { #rename-cols }

También es posible **renombrar columnas** utilizando la función `rename()` de pandas.

Supongamos un caso de uso en el que queremos **renombrar las columnas a sus tres primeras letras en minúsculas**. Tenemos dos maneras de hacerlo:

=== "Mediante un diccionario"

    ```pycon
    >>> new_columns = {'Revenue': 'rev', 'Employees': 'emp', 'City': 'cit', 'Country': 'cou'}

    >>> df_mod.rename(columns=new_columns).head(3)#(1)!
                             rev       emp       cit    cou
    Company
    Apple                473.196  146000.0  Tenerife  Spain
    Alphabet             339.408  190234.0  Tenerife  Spain
    Samsung Electronics  280.956  270372.0  Tenerife  Spain
    ```
    { .annotate }
    
    1. Si en vez del parámetro nominal `columns` utilizamos el parámetro `index` estaremos renombrando los valores del índice. Se aplica el mismo comportamiento ya visto.

=== "Mediante una función «lambda»"

    ```pycon
    >>> df.rename(columns=lambda c: c.lower()[:3]).head(3)#(1)!
                  rev      emp       cit    cou
    Company
    Amazon    689.760  1525000  Tenerife  Spain
    Apple     473.196   146000  Tenerife  Spain
    Alphabet  339.408   190234  Tenerife  Spain
    ```    
    { .annotate }
    
    1. Si en vez del parámetro nominal `columns` utilizamos el parámetro `index` estaremos renombrando los valores del índice. Se aplica el mismo comportamiento ya visto.


La primera sería directamente creando un «mapping» entre los nombres de columna actuales y los nombres nuevos:


### Modificación «in-situ» { #inplace }

Muchas de las funciones de pandas se dicen «no destructivas» en el sentido de que no modifican el conjunto de datos original, sino que devuelven uno nuevo con las modificaciones realizadas. Pero este comportamiento se puede modificar utilizando el parámetro `inplace`.

Veamos un <span class="example">ejemplo:material-flash:</span> borrando algunas columnas:

```pycon hl_lines="10"
>>> df_mod.head()
                     Revenue  Employees      City Country
Company
Amazon               689.760  1525000.0  Tenerife   Spain
Apple                473.196   146000.0  Tenerife   Spain
Alphabet             339.408   190234.0  Tenerife   Spain
Samsung Electronics  280.956   270372.0  Tenerife   Spain
Foxconn              267.048   767062.0  Tenerife   Spain

>>> df_mod.drop(labels='Amazon', inplace=True)#(1)!

>>> df_mod.head()
                     Revenue  Employees      City Country
Company
Apple                473.196   146000.0  Tenerife   Spain
Alphabet             339.408   190234.0  Tenerife   Spain
Samsung Electronics  280.956   270372.0  Tenerife   Spain
Foxconn              267.048   767062.0  Tenerife   Spain
Microsoft            237.924   221000.0  Tenerife   Spain
```
{ .annotate }

1. No es necesario «reasignar» el _dataframe_ ya que `inplace=True` lo modifica «in-situ».

## Otras operaciones { #operations }

Aunque hay una enorme cantidad de operaciones sobre DataFrames, en este apartado trataremos de hacer un recorrido por algunas de las más recurrentes.

### Manejando cadenas de texto { #strings }

A menudo solemos trabajar con datos que incluyen información textual. Pandas también nos ofrece herramientas para cubrir estos casos.

De hecho, simplemente debemos utilizar el manejador str y tendremos a disposición la gran mayoría de funciones vistas en la sección de [cadenas de texto](../../../core/datatypes/strings.md).

Veamos un primer <span class="example">ejemplo:material-flash:</span> en el que **pasamos a mayúsculas las ciudades** en las que se localizan las empresas tecnológicas:

```pycon
>>> df['City'].str.upper().head()
Company
Amazon                         SEATTLE
Apple                        CUPERTINO
Alphabet                 MOUNTAIN VIEW
Samsung Electronics              SUWON
Foxconn                NEW TAIPEI CITY
Name: City, dtype: object
```

Otro supuesto sería el de **sustituir espacios por subguiones en los países** de las empresas:

```pycon
>>> df['Country'].str.replace(' ', '_').head()
Company
Amazon                 United_States
Apple                  United_States
Alphabet               United_States
Samsung Electronics      South_Korea
Foxconn                       Taiwan
Name: Country, dtype: object
```

### Expresiones regulares { #regex }

El uso de expresiones regulares aporta una gran expresividad. Veamos su aplicación con tres casos de uso:

=== "Filtrado de filas"

    Supongamos que queremos **filtrar las empresas y quedarnos con las que comienzan por vocal**:

    ```pycon
    >>> import re

    >>> mask = df.index.str.match(r'^[aeiou]', flags=re.IGNORECASE)#(1)!

    >>> df[mask]
               Revenue  Employees           City        Country
    Company
    Amazon      574.80    1525000        Seattle  United States
    Apple       394.33     164000      Cupertino  United States
    Alphabet    282.84     190234  Mountain View  United States
    Alibaba     130.35     204891         Yuhang          China
    AT&T        122.40     149900         Dallas  United States
    Intel        63.05     131900    Santa Clara  United States
    Accenture    61.59     721000         Dublin        Ireland
    IBM          60.53     303100         Armonk  United States
    ```
    { .annotate }
    
    1. Dado que el nombre de la empresa está actuando como índice del «dataset», hemos aplicado la búsqueda sobre `.index`.

=== "Reemplazo de valores"

    Ahora imaginemos que vamos a **sustituir aquellas ciudades que empiezan con «S» o «T» por «Stanton»**:

    ```pycon
    >>> df['City'].str.replace(r'^[ST].*', 'Stanton', regex=True).head()
    Company
    Amazon                         Stanton
    Apple                        Cupertino
    Alphabet                 Mountain View
    Samsung Electronics            Stanton
    Foxconn                New Taipei City
    Name: City, dtype: object
    ```

=== "Extracción de columnas"

    supongamos que queremos **dividir la columna «Country»** en dos columnas usando el espacio como separador:

    ```pycon
    >>> df['Country'].str.split(' ', expand=True).head()
                              0       1
    Company
    Amazon               United  States
    Apple                United  States
    Alphabet             United  States
    Samsung Electronics   South   Korea
    Foxconn              Taiwan    None
    ```
    
Existen otras funciones interesantes de Pandas que trabajan sobre expresiones regulares:

| Función | Explicación |
| --- | --- |
| [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html) | Contar el número de ocurrencias de un patrón. |
| [`contains()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.contains.html) | Comprobar si existe un determinado patrón. |
| [`extract()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.extract.html) | Extraer grupos de captura sobre un patrón. |
| [`findall()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.findall.html) | Encontrar todas las ocurrencias de un patrón. |

### Manejando fechas { #dates }

Suele ser habitual tener que manejar datos en formato fecha (o fecha-hora). Pandas ofrece un amplio abanico de posibilidades para ello. Veamos algunas de las herramientas disponibles.

Para ejemplificar este apartado hemos añadido al «dataset» de empresas tecnológicas una **nueva columna con las fechas de fundación de las empresas** (en formato «string»):

```pycon
>>> founded_at = [
...     '5/7/1994',   # Amazon
...     '1/4/1976',   # Apple
...     '2/10/2015',  # Alphabet
...     '13/1/1969',  # Samsung Electronics
...     '20/2/1974',  # Foxconn
...     '4/4/1975',   # Microsoft
...     '18/6/1998',  # Jingdong
...     '4/4/1999',   # Alibaba
...     '3/3/1885',   # AT&T
...     '4/2/2004',   # Meta
...     '1/1/1995',   # Deutsche Telekom
...     '1/2/1984',   # Dell Technologies
...     '15/9/1987',  # Huawei
...     '7/5/1946',   # Sony
...     '11/11/1998', # Tencent
...     '1/2/1910',   # Hitachi
...     '21/2/1987',  # TSMC
...     '1/10/1958',  # LG Electronics
...     '18/7/1968',  # Intel
...     '1/1/1939',   # HP Inc.
...     '1/11/1984',  # Lenovo
...     '7/3/1918',   # Panasonic
...     '1/1/1989',   # Accenture
...     '5/4/1993',   # Nvidia
...     '16/6/1911'   # IBM
... ]

>>> df['Founded'] = founded_at

>>> df.head()
                     Revenue  Employees             City        Country    Founded
Company
Amazon                574.80    1525000          Seattle  United States   5/7/1994
Apple                 394.33     164000        Cupertino  United States   1/4/1976
Alphabet              282.84     190234    Mountain View  United States  2/10/2015
Samsung Electronics   234.13     270372            Suwon    South Korea  13/1/1969
Foxconn               222.54     767062  New Taipei City         Taiwan  20/2/1974

>>> df['Founded'].dtype#(1)!
dtype('O')
```
{ .annotate }

1. Columna de tipo **object**.

Lo primero que deberíamos hacer es convertir la columna «Founded» al tipo «datetime» usando la función [`to_datetime()`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html):

```pycon
>>> df['Founded'] = pd.to_datetime(df['Founded'], format='%d/%m/%Y')#(1)!

>>> df['Founded'].head()
Company
Amazon                1994-07-05
Apple                 1976-04-01
Alphabet              2015-10-02
Samsung Electronics   1969-01-13
Foxconn               1974-02-20
Name: Founded, dtype: datetime64[ns]
```
{ .annotate }

1. Dado que el formato de fecha no es [`ISO 8601`](https://es.wikipedia.org/wiki/ISO_8601) tendremos que especificar el formato con el parámetro `format`.

Es posible acceder a cada elemento de la fecha:

```pycon
df['fyear'] = df['Founded'].dt.year
df['fmonth'] = df['Founded'].dt.month
df['fday'] = df['Founded'].dt.day

>>> df.loc[:, 'Founded':].head()
                       Founded  fyear  fmonth  fday
Company
Amazon              1994-07-05   1994       7     5
Apple               1976-04-01   1976       4     1
Alphabet            2015-10-02   2015      10     2
Samsung Electronics 1969-01-13   1969       1    13
Foxconn             1974-02-20   1974       2    20
```

Por ejemplo, podríamos querer calcular el **número de años que llevan activas las empresas**:

```pycon
>>> pd.to_datetime('today').year - df['Founded'].dt.year
Company
Amazon                  31
Apple                   49
Alphabet                10
Samsung Electronics     56
Foxconn                 51
Microsoft               50
Jingdong                27
Alibaba                 26
AT&T                   140
Meta                    21
Deutsche Telekom        30
Dell Technologies       41
Huawei                  38
Sony                    79
Tencent                 27
Hitachi                115
TSMC                    38
LG Electronics          67
Intel                   57
HP Inc.                 86
Lenovo                  41
Panasonic              107
Accenture               36
Nvidia                  32
IBM                    114
Name: Founded, dtype: int32
```

Los tipos de datos «datetime» dan mucha flexibilidad a la hora de hacer consultas:

```pycon
>>> df.query('Founded <= 1950')#(1)!
           Revenue  Employees       City        Country    Founded  fyear  fmonth  fday
Company
AT&T        122.40     149900     Dallas  United States 1885-03-03   1885       3     3
Sony         85.25     112994      Tokyo          Japan 1946-05-07   1946       5     7
Hitachi      80.39     322525      Tokyo          Japan 1910-02-01   1910       2     1
HP Inc.      62.98      53000  Palo Alto  United States 1939-01-01   1939       1     1
Panasonic    61.90     233391      Osaka          Japan 1918-03-07   1918       3     7
IBM          60.53     303100     Armonk  United States 1911-06-16   1911       6    16

>>> df.query('Founded.dt.month == 1')#(2)!
                     Revenue  Employees       City        Country    Founded  fyear  fmonth  fday
Company
Samsung Electronics   234.13     270372      Suwon    South Korea 1969-01-13   1969       1    13
Deutsche Telekom      112.00     205000       Bonn        Germany 1995-01-01   1995       1     1
HP Inc.                62.98      53000  Palo Alto  United States 1939-01-01   1939       1     1
Accenture              61.59     721000     Dublin        Ireland 1989-01-01   1989       1     1

>>> df.query('9 <= Founded.dt.month <= 12')#(3)!
                Revenue  Employees           City        Country    Founded  fyear  fmonth  fday
Company
Alphabet         282.84     190234  Mountain View  United States 2015-10-02   2015      10     2
Huawei            95.49     207000       Shenzhen          China 1987-09-15   1987       9    15
Tencent           82.44     108436       Shenzhen          China 1998-11-11   1998      11    11
LG Electronics    64.95      74000          Seoul    South Korea 1958-10-01   1958      10     1
Lenovo            61.95      71500      Hong Kong      Hong Kong 1984-11-01   1984      11     1
```
{ .annotate }

1. Empresas creadas antes de 1950.
2. Empresas creadas en Enero.
3. Empresas creadas en el último cuatrimestre del año.

Hay ocasiones en las que necesitamos que **la fecha se convierta en el índice** del DataFrame:

```pycon
>>> df = df.reset_index().set_index('Founded').sort_index()

>>> df.head()
              Company  Revenue  Employees       City        Country  fyear  fmonth  fday
Founded
1885-03-03       AT&T   122.40     149900     Dallas  United States   1885       3     3
1910-02-01    Hitachi    80.39     322525      Tokyo          Japan   1910       2     1
1911-06-16        IBM    60.53     303100     Armonk  United States   1911       6    16
1918-03-07  Panasonic    61.90     233391      Osaka          Japan   1918       3     7
1939-01-01    HP Inc.    62.98      53000  Palo Alto  United States   1939       1     1
```

Esto nos permite indexar de forma mucho más precisa:

```pycon
>>> df.loc['1998']#(1)!
             Company  Revenue  Employees      City Country  fyear  fmonth  fday
Founded
1998-06-18  Jingdong   152.80     310000   Beijing   China   1998       6    18
1998-11-11   Tencent    82.44     108436  Shenzhen   China   1998      11    11

>>> df.loc['1970':'1980']#(2)!
              Company  Revenue  Employees             City        Country  fyear  fmonth  fday
Founded
1974-02-20    Foxconn   222.54     767062  New Taipei City         Taiwan   1974       2    20
1975-04-04  Microsoft   198.27     221000          Redmond  United States   1975       4     4
1976-04-01      Apple   394.33     164000        Cupertino  United States   1976       4     1

>>> df.loc['1975-1':'1984-3']#(3)!
                      Company  Revenue  Employees        City        Country  fyear  fmonth  fday
Founded
1975-04-04          Microsoft   198.27     221000     Redmond  United States   1975       4     4
1976-04-01              Apple   394.33     164000   Cupertino  United States   1976       4     1
1984-02-01  Dell Technologies   102.30     133000  Round Rock  United States   1984       2     1
```
{ .annotate }

1. Empresas creadas en 1988.
2. Empresas creadas entre 1970 y 1980.
3. Empresas creadas entre enero de 1975 y marzo de 1984.

!!! exercise "Ejercicio"

    Partiendo del fichero [`oasis.csv`](../files/pandas/oasis.csv) que contiene información sobre la discografía del grupo de pop británico [Oasis](https://www.oasisinet.com/), se pide:

    1. Carga el fichero en un DataFrame.
    2. Convierte la columna `album_release_date` a tipo «datetime».
    3. Encuentra los nombres de los álbumes publicados entre 2000 y 2005.

    [:material-lightbulb: Solución](../files/pandas/df_oasis.py)

### Manejando categorías { #categories }

Hasta ahora hemos visto tipos de datos numéricos, cadenas de texto y fechas. ¿Pero qué ocurre con las categorías?

Las categorías pueden ser tanto datos numéricos como textuales, con la característica de tener un número discreto (relativamente pequeño) de elementos y, en ciertas ocasiones, un orden preestablecido. Ejemplos de variables categóricas son: género, idioma, meses del año, color de ojos, nivel de estudios, grupo sanguíneo, valoración, etc.

Pandas facilita el [tratamiento de datos categóricos](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html) mediante un tipo específico `Categorical`.

Siguiendo con el «dataset» de empresas tecnológicas, vamos a añadir el continente al que pertenece cada empresa. En primera instancia mediante valores de texto habituales:

```pycon
>>> continents_from = [
...     'America',  # Amazon
...     'America',  # Apple
...     'America',  # Alphabet
...     'Asia',     # Samsung Electronics
...     'Asia',     # Foxconn
...     'America',  # Microsoft
...     'Asia',     # Jingdong
...     'Asia',     # Alibaba
...     'America',  # AT&T
...     'America',  # Meta
...     'Europe',   # Deutsche Telekom
...     'America',  # Dell Technologies
...     'Asia',     # Huawei
...     'Asia',     # Sony
...     'Asia',     # Tencent
...     'Asia',     # Hitachi
...     'Asia',     # TSMC
...     'Asia',     # LG Electronics
...     'America',  # Intel
...     'America',  # HP Inc.
...     'Asia',     # Lenovo
...     'Asia',     # Panasonic
...     'Europe',   # Accenture
...     'America',  # Nvidia
...     'America'   # IBM
... ]

>>> df['Continent'] = continents_from

>>> df['Continent'].head()
Company
Amazon                 America
Apple                  America
Alphabet               America
Samsung Electronics       Asia
Foxconn                   Asia
Name: Continent, dtype: object
```

Ahora podemos convertir esta columna a tipo categoría:

```pycon
>>> df['Continent'].astype('category')
Company
Amazon                 America
Apple                  America
Alphabet               America
Samsung Electronics       Asia
Foxconn                   Asia
Microsoft              America
Jingdong                  Asia
Alibaba                   Asia
AT&T                   America
Meta                   America
Deutsche Telekom        Europe
Dell Technologies      America
Huawei                    Asia
Sony                      Asia
Tencent                   Asia
Hitachi                   Asia
TSMC                      Asia
LG Electronics            Asia
Intel                  America
HP Inc.                America
Lenovo                    Asia
Panasonic                 Asia
Accenture               Europe
Nvidia                 America
IBM                    America
Name: Continent, dtype: category
Categories (3, object): ['America', 'Asia', 'Europe']
```

En este caso, al ser una conversión «automática», las categorías no han incluido ningún tipo de orden. Pero imaginemos que queremos establecer un orden para las categorías de continentes basadas, por ejemplo, en su población: Asia, África, Europa, América, Australia:

```pycon hl_lines="4 35"
>>> from pandas.api.types import CategoricalDtype

>>> continents = ('Asia', 'Africa', 'Europe', 'America', 'Australia')
>>> cat_continents = CategoricalDtype(categories=continents, ordered=True)

>>> df['Continent'] = df['Continent'].astype(cat_continents)
>>> df['Continent]
Company
Amazon                 America
Apple                  America
Alphabet               America
Samsung Electronics       Asia
Foxconn                   Asia
Microsoft              America
Jingdong                  Asia
Alibaba                   Asia
AT&T                   America
Meta                   America
Deutsche Telekom        Europe
Dell Technologies      America
Huawei                    Asia
Sony                      Asia
Tencent                   Asia
Hitachi                   Asia
TSMC                      Asia
LG Electronics            Asia
Intel                  America
HP Inc.                America
Lenovo                    Asia
Panasonic                 Asia
Accenture               Europe
Nvidia                 America
IBM                    America
Name: Continent, dtype: category
Categories (5, object): ['Asia' < 'Africa' < 'Europe' < 'America' < 'Australia']
```

El hecho de trabajar con **categorías ordenadas** permite (entre otras) estas operaciones:

```pycon
>>> df['Continent'].min()#(1)!
'Asia'

>>> df['Continent'].max()#(2)!
'America'

>>> df['Continent'].sort_values()#(3)!
Company
Huawei                    Asia
Panasonic                 Asia
Samsung Electronics       Asia
Foxconn                   Asia
Lenovo                    Asia
Jingdong                  Asia
Alibaba                   Asia
LG Electronics            Asia
TSMC                      Asia
Sony                      Asia
Tencent                   Asia
Hitachi                   Asia
Accenture               Europe
Deutsche Telekom        Europe
HP Inc.                America
Intel                  America
Amazon                 America
Dell Technologies      America
Meta                   America
AT&T                   America
Microsoft              America
Alphabet               America
Apple                  America
Nvidia                 America
IBM                    America
Name: Continent, dtype: category
Categories (5, object): ['Asia' < 'Africa' < 'Europe' < 'America' < 'Australia']
```
{ .annotate }

1. En condiciones normales (categorías sin ordenar) el mínimo hubiera sido America ya que se habrían ordenado alfabéticamente.
2. En condiciones normales (categorías sin ordenar) el máximo hubiera sido Asia ya que se habrían ordenado alfabéticamente.
3. La ordenación se verá más adelante pero en este caso ordenamos la columna por sus valores.

### Usando funciones estadísticas { #stats }

Vamos a aplicar las funciones estadísticas que proporciona pandas sobre la columna _Revenue_ de nuestro «dataset», aunque podríamos hacerlo sobre todas aquellas variables numéricas susceptibles:

```pycon
>>> df['Revenue'].head()
Company
Amazon                 574.80
Apple                  394.33
Alphabet               282.84
Samsung Electronics    234.13
Foxconn                222.54
Name: Revenue, dtype: float64
```

Función|Resultado|Descripción
---|---|---
`df['Revenue'].count()`|25|Número de observaciones no nulas
`df['Revenue'].sum()`|3560.84|Suma de los valores
`df['Revenue'].mean()`|142.43|Media de los valores
`df['Revenue'].median()`|95.49|Mediana de los valores
`df['Revenue'].min()`|60.53|Mínimo
`df['Revenue'].max()`|574.80|Máximo
`df['Revenue'].mode()`|Múltiples valores|Moda
`df['Revenue'].abs()`|Múltiples valores|Valor absoluto
`df['Revenue'].prod()`|1.98e+51|Producto de los valores
`df['Revenue'].std()`|122.60|Desviación típica
`df['Revenue'].var()`|15029.56|Varianza
`df['Revenue'].sem()`|24.52|Error típico de la media
`df['Revenue'].skew()`|2.35|Asimetría
`df['Revenue'].kurt()`|6.03|Apuntamiento
`df['Revenue'].quantile()`|95.49|Cuantiles (por defecto 50%)
`df['Revenue'].cumsum()`|Múltiples valores|Suma acumulativa
`df['Revenue'].cumprod()`|Múltiples valores|Producto acumulativo
`df['Revenue'].cummax()`|Múltiples valores|Máximo acumulativo
`df['Revenue'].cummin()`|Múltiples valores|Mínimo acumulativo

!!! exercise "Ejercicio"

    Partiendo del conjunto de datos [`democan`](../files/pandas/democan.csv), encuentra aquellas islas cuya población está por encima de la media del archipiélago canario.

    Resultado esperado :material-arrow-right-bold: Gran Canaria y Tenerife.

    [:material-lightbulb: Solución](../files/pandas/above_mean.py)

### Ordenando valores { #sort }

Una operación muy típica cuando trabajamos con datos es la de ordenarlos en base a ciertos criterios. Veamos cómo podemos hacerlo utilizando pandas. Volvemos a nuestro «dataset» tecnológico:

```pycon
>>> df.head()
                     Revenue  Employees             City        Country
Company
Amazon                574.80    1525000          Seattle  United States
Apple                 394.33     164000        Cupertino  United States
Alphabet              282.84     190234    Mountain View  United States
Samsung Electronics   234.13     270372            Suwon    South Korea
Foxconn               222.54     767062  New Taipei City         Taiwan
```

Supongamos que queremos tener el conjunto de datos **ordenado por el nombre de empresa**. Como, en este caso, la columna _Company_ constituye el índice, debemos ordenar por el índice:

```pycon
>>> df.sort_index()
                     Revenue  Employees             City        Country
Company
AT&T                  122.40     149900           Dallas  United States
Accenture              61.59     721000           Dublin        Ireland
Alibaba               130.35     204891           Yuhang          China
Alphabet              282.84     190234    Mountain View  United States
Amazon                574.80    1525000          Seattle  United States
Apple                 394.33     164000        Cupertino  United States
Dell Technologies     102.30     133000       Round Rock  United States
Deutsche Telekom      112.00     205000             Bonn        Germany
Foxconn               222.54     767062  New Taipei City         Taiwan
HP Inc.                62.98      53000        Palo Alto  United States
Hitachi                80.39     322525            Tokyo          Japan
Huawei                 95.49     207000         Shenzhen          China
IBM                    60.53     303100           Armonk  United States
Intel                  63.05     131900      Santa Clara  United States
Jingdong              152.80     310000          Beijing          China
LG Electronics         64.95      74000            Seoul    South Korea
Lenovo                 61.95      71500        Hong Kong      Hong Kong
Meta                  116.61      86482       Menlo Park  United States
Microsoft             198.27     221000          Redmond  United States
Nvidia                 60.93      29600      Santa Clara  United States
Panasonic              61.90     233391            Osaka          Japan
Samsung Electronics   234.13     270372            Suwon    South Korea
Sony                   85.25     112994            Tokyo          Japan
TSMC                   76.02      73090  New Taipei City         Taiwan
Tencent                82.44     108436         Shenzhen          China
```

Ahora imaginemos que necesitamos tener las **empresas ordenadas de mayor a menor número de ingresos**:

```pycon
>>> df.sort_index()
                     Revenue  Employees             City        Country
Company
AT&T                  122.40     149900           Dallas  United States
Accenture              61.59     721000           Dublin        Ireland
Alibaba               130.35     204891           Yuhang          China
Alphabet              282.84     190234    Mountain View  United States
Amazon                574.80    1525000          Seattle  United States
Apple                 394.33     164000        Cupertino  United States
Dell Technologies     102.30     133000       Round Rock  United States
Deutsche Telekom      112.00     205000             Bonn        Germany
Foxconn               222.54     767062  New Taipei City         Taiwan
HP Inc.                62.98      53000        Palo Alto  United States
Hitachi                80.39     322525            Tokyo          Japan
Huawei                 95.49     207000         Shenzhen          China
IBM                    60.53     303100           Armonk  United States
Intel                  63.05     131900      Santa Clara  United States
Jingdong              152.80     310000          Beijing          China
LG Electronics         64.95      74000            Seoul    South Korea
Lenovo                 61.95      71500        Hong Kong      Hong Kong
Meta                  116.61      86482       Menlo Park  United States
Microsoft             198.27     221000          Redmond  United States
Nvidia                 60.93      29600      Santa Clara  United States
Panasonic              61.90     233391            Osaka          Japan
Samsung Electronics   234.13     270372            Suwon    South Korea
Sony                   85.25     112994            Tokyo          Japan
TSMC                   76.02      73090  New Taipei City         Taiwan
Tencent                82.44     108436         Shenzhen          China
>>> df.sort_values(by='Revenue', ascending=False)
                     Revenue  Employees             City        Country
Company
Amazon                574.80    1525000          Seattle  United States
Apple                 394.33     164000        Cupertino  United States
Alphabet              282.84     190234    Mountain View  United States
Samsung Electronics   234.13     270372            Suwon    South Korea
Foxconn               222.54     767062  New Taipei City         Taiwan
Microsoft             198.27     221000          Redmond  United States
Jingdong              152.80     310000          Beijing          China
Alibaba               130.35     204891           Yuhang          China
AT&T                  122.40     149900           Dallas  United States
Meta                  116.61      86482       Menlo Park  United States
Deutsche Telekom      112.00     205000             Bonn        Germany
Dell Technologies     102.30     133000       Round Rock  United States
Huawei                 95.49     207000         Shenzhen          China
Sony                   85.25     112994            Tokyo          Japan
Tencent                82.44     108436         Shenzhen          China
Hitachi                80.39     322525            Tokyo          Japan
TSMC                   76.02      73090  New Taipei City         Taiwan
LG Electronics         64.95      74000            Seoul    South Korea
Intel                  63.05     131900      Santa Clara  United States
HP Inc.                62.98      53000        Palo Alto  United States
Lenovo                 61.95      71500        Hong Kong      Hong Kong
Panasonic              61.90     233391            Osaka          Japan
Accenture              61.59     721000           Dublin        Ireland
Nvidia                 60.93      29600      Santa Clara  United States
IBM                    60.53     303100           Armonk  United States
```

También es posible utilizar varias columnas en la ordenación. Pongamos que deseamos **ordenar los datos por país y por ciudad**. Veamos cómo afrontarlo:

```pycon
>>> df.sort_values(by=['Country', 'City'])
                     Revenue  Employees             City        Country
Company
Jingdong              152.80     310000          Beijing          China
Huawei                 95.49     207000         Shenzhen          China
Tencent                82.44     108436         Shenzhen          China
Alibaba               130.35     204891           Yuhang          China
Deutsche Telekom      112.00     205000             Bonn        Germany
Lenovo                 61.95      71500        Hong Kong      Hong Kong
Accenture              61.59     721000           Dublin        Ireland
Panasonic              61.90     233391            Osaka          Japan
Sony                   85.25     112994            Tokyo          Japan
Hitachi                80.39     322525            Tokyo          Japan
LG Electronics         64.95      74000            Seoul    South Korea
Samsung Electronics   234.13     270372            Suwon    South Korea
Foxconn               222.54     767062  New Taipei City         Taiwan
TSMC                   76.02      73090  New Taipei City         Taiwan
IBM                    60.53     303100           Armonk  United States
Apple                 394.33     164000        Cupertino  United States
AT&T                  122.40     149900           Dallas  United States
Meta                  116.61      86482       Menlo Park  United States
Alphabet              282.84     190234    Mountain View  United States
HP Inc.                62.98      53000        Palo Alto  United States
Microsoft             198.27     221000          Redmond  United States
Dell Technologies     102.30     133000       Round Rock  United States
Intel                  63.05     131900      Santa Clara  United States
Nvidia                 60.93      29600      Santa Clara  United States
Amazon                574.80    1525000          Seattle  United States
```

### Buscando máximos y mínimos { #max-min }

Al igual que veíamos [en el caso de las series](series.md#series-ops), podemos aplicar muchas de estas funciones de máximos y mínimos sobre un DataFrame de Pandas.

Podemos obtener los **valores mínimos y máximos de todas las columnas**:

```pycon
>>> df.min()
Revenue       60.53
Employees     29600
City         Armonk
Country       China
dtype: object

>>> df.max()
Revenue              574.8
Employees          1525000
City                Yuhang
Country      United States
dtype: object
```

También podría ser de utilidad saber **qué empresa tiene el valor mínimo o máximo** para una determinada columna:

```pycon
>>> df['Revenue'].idxmin()#(1)!
'IBM'

>>> df['Employees'].idxmax()#(2)!
'Amazon'
```
{ .annotate }

1.  - Empresa con menores ingresos.
    - Devuelve una cadena de texto con el nombre de la empresa porque así lo tenemos definido en el índice. En otro caso devolvería la posición (numérica) del índice.
2.  - Empresa con mayor números de empleados/as.
    - Devuelve una cadena de texto con el nombre de la empresa porque así lo tenemos definido en el índice. En otro caso devolvería la posición (numérica) del índice.

Si queremos acceder al **registro completo**, basta con acceder a través de la etiqueta devuelta:

```pycon
>>> company = df['Revenue'].idxmin()

>>> df.loc[company]
Revenue              60.53
Employees           303100
City                Armonk
Country      United States
Name: IBM, dtype: object
```

Otra de las operaciones muy usuales es encontrar los $n$ registros con mayores/menores valores. Supongamos que nos interesa conocer las **3 empresas con mayores ingresos y las 3 empresas con menor número de empleados/as**:

```pycon
>>> df['Revenue'].nlargest(3)#(1)!
Company
Amazon      574.80
Apple       394.33
Alphabet    282.84
Name: Revenue, dtype: float64

>>> df['Employees'].nsmallest(3)#(2)!
Company
Nvidia     29600
HP Inc.    53000
Lenovo     71500
Name: Employees, dtype: int64
```
{ .annotate }

1.  - Las tres empresas con mayores ingresos.
    - Si no se especifica una cantidad, la función `nlargest()` lo tiene definido en 5.
2.  - Las tres empresas con menor número de empleados/as.
    - Si no se especifica una cantidad, la función `nsmallest()` lo tiene definido en 5.

Si queremos acceder al **registro completo**, podemos aplicar estas funciones de otro modo:

```pycon
>>> df.nlargest(3, 'Revenue')
          Revenue  Employees           City        Country
Company
Amazon     574.80    1525000        Seattle  United States
Apple      394.33     164000      Cupertino  United States
Alphabet   282.84     190234  Mountain View  United States

>>> df.nsmallest(3, 'Employees')
         Revenue  Employees         City        Country
Company
Nvidia     60.93      29600  Santa Clara  United States
HP Inc.    62.98      53000    Palo Alto  United States
Lenovo     61.95      71500    Hong Kong      Hong Kong
```

!!! exercise "Ejercicio"

    Partiendo del conjunto de datos [`democan`](../files/pandas/democan.csv) encuentra las 3 islas con menor densidad de población incluyendo el resto de su información (en cada fila).

    Resultado esperado :material-arrow-right-bold: El Hierro, La Gomera y Fuerteventura.

    [:material-lightbulb: Solución](../files/pandas/smallest_density.py)

### Gestionando valores nulos { #null }

La limpieza de un «dataset» suele estar vinculado, en muchas ocasiones, a la gestión de los valores nulos. En este sentido, pandas ofrece varias funciones.

Para ejemplificar este apartado, vamos a hacer uso del siguiente DataFrame:

```pycon
>>> df
   A    B    C
0  1  4.0  7.0
1  2  NaN  8.0
2  3  6.0  NaN
```

Veamos distintas aproximaciones a la gestión de valores nulos:

=== "Detectar valores nulos"

    ```pycon
    >>> df.isna()#(1)!
           A      B      C
    0  False  False  False
    1  False   True  False
    2  False  False   True
    ```
    { .annotate }
    
    1. También existe la función `isnull()` que funciona de manera análoga a `isna()`[^5].

=== "Descartar registros"

    ```pycon
    >>> df.dropna()
       A    B    C
    0  1  4.0  7.0
    ```

=== "Rellenar valores nulos"

    ```pycon
    >>> df.fillna(0)
       A    B    C
    0  1  4.0  0.0
    1  2  0.0  0.0
    2  3  6.0  9.0
    ```

=== "Interpolar valores nulos"

    ```pycon
    >>> df.interpolate()
       A    B    C
    0  1  4.0  7.0
    1  2  5.0  8.0
    2  3  6.0  8.0
    ```

### Pivotando { #pivot }

En esta sección se verán las operaciones de **pivotar** y **apilar** que permiten reformar (remodelar) un DataFrame.

Seguimos utilizando el conjunto de datos de empresas tecnológicas aunque nos quedaremos únicamente con las 3 primeras filas a efectos didácticos:

```pycon
>>> df = df.reset_index()[:3]

>>> df
    Company  Revenue  Employees           City        Country
0    Amazon   574.80    1525000        Seattle  United States
1     Apple   394.33     164000      Cupertino  United States
2  Alphabet   282.84     190234  Mountain View  United States
```

=== "Pivotar"

    Típicamente existen dos maneras de presentar datos tabulares: formato ancho y formato largo. En **formato ancho** cada fila tiene múltiples columnas representando todas las variables de una misma observación. En **formato largo** cada fila tiene básicamente tres columnas: una que identifica la observación, otra que identifica la variable y otra que contiene el valor.

    Para pasar de formato ancho a formato largo usamos la función [`melt()`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html):

    ```pycon
    >>> df.melt(id_vars='Company')
         Company   variable          value
    0     Amazon    Revenue          574.8
    1      Apple    Revenue         394.33
    2   Alphabet    Revenue         282.84
    3     Amazon  Employees        1525000
    4      Apple  Employees         164000
    5   Alphabet  Employees         190234
    6     Amazon       City        Seattle
    7      Apple       City      Cupertino
    8   Alphabet       City  Mountain View
    9     Amazon    Country  United States
    10     Apple    Country  United States
    11  Alphabet    Country  United States
    ```

    Para pasar de formato largo a formato ancho usamos la función [`pivot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html):

    ```pycon
    >>> df_long = df.melt(id_vars='Company')

    >>> df_long.pivot(index='Company', columns='variable', values='value')#(1)!
    variable           City        Country Employees Revenue
    Company
    Alphabet  Mountain View  United States    190234  282.84
    Amazon          Seattle  United States   1525000   574.8
    Apple         Cupertino  United States    164000  394.33
    ```
    { .annotate }
    
    1. Si queremos obtener el DataFrame en formato ancho, tal y como estaba, tenemos que realizar alguna operación adicional :material-arrow-right-bold: `#!python df.rename_axis(columns = None).reset_index()`.

=== "Apilar"

    Las operaciones de apilado trabajan sobre los índices del DataFrame. Para comprobar su aplicabilidad, vamos a añadir la columna _Company_ como índice del «dataset» anterior:

    ```pycon
    >>> df.set_index('Company', inplace=True)
    >>> df
              Revenue  Employees           City        Country
    Company
    Amazon     574.80    1525000        Seattle  United States
    Apple      394.33     164000      Cupertino  United States
    Alphabet   282.84     190234  Mountain View  United States
    ```

    La función [`stack()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html) nos permite obtener un DataFrame con **índice multinivel** que incluye las columnas del DataFrame de origen y los valores agrupados:

    ```pycon
    >>> df_stacked = df.stack()

    >>> df_stacked#(1)!
    Company
    Amazon    Revenue              574.8
              Employees          1525000
              City               Seattle
              Country      United States
    Apple     Revenue             394.33
              Employees           164000
              City             Cupertino
              Country      United States
    Alphabet  Revenue             282.84
              Employees           190234
              City         Mountain View
              Country      United States
    dtype: object
    ```
    { .annotate }
    
    1. El índice contiene múltiples columnas:
        ```pycon
        >>> df_stacked.index
        MultiIndex([(  'Amazon',   'Revenue'),
                    (  'Amazon', 'Employees'),
                    (  'Amazon',      'City'),
                    (  'Amazon',   'Country'),
                    (   'Apple',   'Revenue'),
                    (   'Apple', 'Employees'),
                    (   'Apple',      'City'),
                    (   'Apple',   'Country'),
                    ('Alphabet',   'Revenue'),
                    ('Alphabet', 'Employees'),
                    ('Alphabet',      'City'),
                    ('Alphabet',   'Country')],
                   names=['Company', None])
        ```

    La función [`unstack()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html) realiza justo la operación contraria: convertir un DataFrame con índice multinivel en un Dataframe en formato ancho con índice sencillo. Se podría ver como una manera de aplanar el «dataset»:

    ```pycon
    >>> df_flat = df_stacked.unstack()

    >>> df_flat#(1)!
             Revenue Employees           City        Country
    Company
    Amazon     574.8   1525000        Seattle  United States
    Apple     394.33    164000      Cupertino  United States
    Alphabet  282.84    190234  Mountain View  United States
    ```
    1. El índice contiene una única columna:
        ```pycon
        >>> df_flat.index
        Index(['Amazon', 'Apple', 'Alphabet'], dtype='object', name='Company')
        ```

### Agrupando datos { #groupby }

Las operaciones de agregado son muy recurridas y nos permiten extraer información relevante, que, a simple vista, quizás no sea tan evidente.

Veamos un ejemplo en el que calculamos **la suma de los ingresos de las empresas, agrupados por país**:

```pycon
>>> df.groupby('Country')['Revenue'].sum()
Country
China             461.08
Germany           112.00
Hong Kong          61.95
Ireland            61.59
Japan             227.54
South Korea       299.08
Taiwan            298.56
United States    2039.04
Name: Revenue, dtype: float64
```

También es posible realizar la agrupación en varios niveles. En el siguiente ejemplo tendremos los **datos agrupados por país y ciudad**:

```pycon
>>> df.groupby(['Country', 'City'])['Revenue'].sum()#(1)!
Country        City
China          Beijing            152.80
               Shenzhen           177.93
               Yuhang             130.35
Germany        Bonn               112.00
Hong Kong      Hong Kong           61.95
Ireland        Dublin              61.59
Japan          Osaka               61.90
               Tokyo              165.64
South Korea    Seoul               64.95
               Suwon              234.13
Taiwan         New Taipei City    298.56
United States  Armonk              60.53
               Cupertino          394.33
               Dallas             122.40
               Menlo Park         116.61
               Mountain View      282.84
               Palo Alto           62.98
               Redmond            198.27
               Round Rock         102.30
               Santa Clara        123.98
               Seattle            574.80
Name: Revenue, dtype: float64
```
{ .annotate }

1. Cuando realizamos una agrupación por varias columnas, el resultado contiene un índice de múltiples niveles. Podemos aplanar el DataFrame usando [`unstack()`](https://aprendepython.es/pypi/datascience/pandas/#reformando-datos).

Incluso podemos aplicar distintas funciones de agregación a cada columna. Supongamos que necesitamos calcular **la media de los ingresos y la mediana del número de empleados/as, con las empresas agrupadas por país**:

```pycon
>>> df.groupby('Country').agg({'Revenue': 'mean', 'Employees': 'median'})#(1)!
                  Revenue  Employees
Country
China          115.270000   205945.5
Germany        112.000000   205000.0
Hong Kong       61.950000    71500.0
Ireland         61.590000   721000.0
Japan           75.846667   233391.0
South Korea    149.540000   172186.0
Taiwan         149.280000   420076.0
United States  185.367273   149900.0
```
{ .annotate }

1. Utilizamos la función `agg()` pasando un diccionario cuyas claves son nombres de columnas y cuyos valores son funciones a aplicar.

!!! exercise "Ejercicio"

    Calcula el porcentaje de población (en relación con el total) de cada provincia de las Islas Canarias en base al «dataset» [`democan`](../files/pandas/democan.csv).

    El resultado debería ser similar a:
    - Provincia de Las Palmas: 52%
    - Provincia de Santa Cruz de Tenerife: 48%

    [:material-lightbulb: Solución](../files/pandas/pop_percentage.py)

### Aplicando funciones { #apply }

Pandas permite la aplicación de funciones (tanto propias como «built-in») a filas y/o columnas de un DataFrame.

Numpy nos ofrece una [amplia gama de funciones matemáticas](https://numpy.org/doc/stable/reference/routines.math.html). Podemos hacer uso de cualquier de ellas aplicándola directamente a nuestro conjunto de datos.

Veamos un ejemplo en el que obtenemos el **máximo de cada columna**:

```pycon
>>> df.apply(np.max)#(1)!
Revenue              574.8
Employees          1525000
City                Yuhang
Country      United States
dtype: object
```
{ .annotate }

1. En este caso es equivalente a `df.max()`

Podemos aplicar funciones sobre determinadas columnas. Supongamos que queremos obtener el **logaritmo de la serie de ingresos**:

```pycon
>>> df['Revenue'].apply(np.log)
Company
Amazon                 6.354022
Apple                  5.977188
Alphabet               5.644881
Samsung Electronics    5.455877
Foxconn                5.405107
Microsoft              5.289630
Jingdong               5.029130
Alibaba                4.870223
AT&T                   4.807294
Meta                   4.758835
Deutsche Telekom       4.718499
Dell Technologies      4.627910
Huawei                 4.559022
Sony                   4.445588
Tencent                4.412071
Hitachi                4.386890
TSMC                   4.330996
LG Electronics         4.173618
Intel                  4.143928
HP Inc.                4.142817
Lenovo                 4.126328
Panasonic              4.125520
Accenture              4.120500
Nvidia                 4.109726
IBM                    4.103139
Name: Revenue, dtype: float64
```

Ahora imaginemos un escenario en el que **la normativa de Estados Unidos ha cambiado y obliga a sus empresas tecnológicas a aumentar un 5% el número de empleados/as que tienen**. Esto lo podríamos abordar escribiendo una función propia que gestione cada fila del «dataset» y devuelva el valor adecuado de empleados/as según las características de cada empresa:

```pycon
>>> def raise_employment(row):
...     num_employees = row['Employees']
...     if row['Country'] == 'United States':
...         return num_employees * 1.05
...     return num_employees
```

Ahora ya podemos aplicar esta función a nuestro DataFrame, teniendo en cuenta que debemos actuar sobre el **eje de filas** (`axis=1`):

```pycon
>>> df.apply(raise_employment, axis=1)
Company
Amazon                 1601250.0
Apple                   172200.0
Alphabet                199745.7
Samsung Electronics     270372.0
Foxconn                 767062.0
Microsoft               232050.0
Jingdong                310000.0
Alibaba                 204891.0
AT&T                    157395.0
Meta                     90806.1
Deutsche Telekom        205000.0
Dell Technologies       139650.0
Huawei                  207000.0
Sony                    112994.0
Tencent                 108436.0
Hitachi                 322525.0
TSMC                     73090.0
LG Electronics           74000.0
Intel                   138495.0
HP Inc.                  55650.0
Lenovo                   71500.0
Panasonic               233391.0
Accenture               721000.0
Nvidia                   31080.0
IBM                     318255.0
dtype: float64
```

El resultado es una serie que se podría incorporar al conjunto de datos, o bien, reemplazar la columna _Employees_ con estos valores.

!!! exercise "Ejercicio"

    Supongamos que el Gobierno de Canarias va a dar unas ayudas a cada isla en función de su superficie y su población, con las siguientes reglas:

    - Islas con menos de $1000km^2$ :material-arrow-right-bold: Ayuda del 30% de su población.
    - Islas con más de $1000km^2$ :material-arrow-right-bold: Ayuda del 20% de su población.

    Añade una nueva columna Grant al «dataset» [`democan`](../files/pandas/democan.csv) donde se contemplen estas ayudas. El DataFrame debería quedar así:

    ```pycon
                   Population     Area Province     Grant
    Island
    El Hierro           11423   268.71       TF    3426.9
    Fuerteventura      120021  1665.74       LP   24004.2
    Gran Canaria       853262  1560.10       LP  170652.4
    La Gomera           21798   369.76       TF    6539.4
    Lanzarote          156112   888.07       LP   46833.6
    La Palma            83439   708.32       TF   25031.7
    Tenerife           931646  2034.38       TF  186329.2
    ```

    [:material-lightbulb: Solución](../files/pandas/grants.py)

### Uniendo DataFrames { #merge }

En esta sección veremos dos técnicas: Una de ellas «fusiona» dos DataFrames mientras que la otra los «concatena».

=== "Fusión de DataFrames"

    Pandas proporciona la función [`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html) para mezclar dos DataFrames. El comportamiento de la función viene definido, entre otros, por el parámetro `how` que establece el método de «fusión»:

    ![Dark image](../images/pandas/pandas-merge-dark.svg#only-dark)
    ![Light image](../images/pandas/pandas-merge-light.svg#only-light)    

    En principio, si no establecemos ningún argumento adicional, «merge» tratará de vincular aquellas filas con columnas homónimas en ambos conjuntos de datos. Si queremos especificar que la mezcla se dirija por determinadas columnas, tenemos a disposición los parámetros `on`, `left_on` o `right_on`.

    !!! tip "Producto cartesiano"
    
        Existe la posibilidad de generar un [producto cartesiano](https://es.wikipedia.org/wiki/Producto_cartesiano) entre las filas de ambos DataFrames :material-arrow-right-bold: `#!python pd.merge(df1, df2, how='cross')`.

=== "Concatenación de DataFrames"

    Para concatenar dos DataFrames podemos utilizar la función [`concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html) que permite añadir las filas de un DataFrame a otro, o bien añadir las columnas de un DataFrame a otro.

    ![Dark image](../images/pandas/pandas-concat-dark.svg#only-dark)
    ![Light image](../images/pandas/pandas-concat-light.svg#only-light)

    Si queremos «reindexar» el DataFrame concatenado, la función `concat()` admite un parámetro `ignore_index` que podemos poner a `#!python True`. De esta forma tendremos un «dataset» resultante con índice desde 0 hasta N.

!!! exercise "Ejercicio"

    Extrae los datos de población y superficie de las comunidades autónomas españolas desde [esta url de Wikipedia](https://es.wikipedia.org/wiki/Comunidad_aut%C3%B3noma) en un único DataFrame con la siguiente estructura:

    ```pycon
                    Comunidad  Superficie  Población     Densidad
    0       Castilla y León       94226    2407650    25.551865
    1             Andalucía       87268    8379248    96.017418
    2   Casstilla-La Mancha       79463    2025510    25.489976
    ...
    ```

    Notas:

    - Utiliza la función `pd.read_html()` para acceder a las tablas. La tabla de superficie tiene el índice 3 y la tabla de población tiene el índice 4.
    - Elimina la última fila de totales en cada DataFrame y quédese sólo con las columnas que interesen.
    - Renombra las columnas según interese.
    - Reemplaza los valores de población y superficie para que sean números y convierta las columnas a entero.
    - Realiza la mezcla de población y superficie en un único DataFrame.
    - Calcula la densidad de población de cada comunidad autónoma.

    [:material-lightbulb: Solución](../files/pandas/comunidades.py)


[^1]: Datos capturados desde [Wikipedia](https://en.wikipedia.org/wiki/List_of_largest_technology_companies_by_revenue) en abril de 2025.
[^2]: Datos capturados desde [Wikipedia](https://es.wikipedia.org/wiki/Canarias) en abril de 2025.
[^3]: Un billón de dólares americanos equivale a 1.000.000.000$
[^4]: Exceso de tiempo de cómputacion, memoria o ancho de banda que son necesarios para realizar una tarea específica.
[^5]: Comparativa de ambas funciones en [StackExchange](https://datascience.stackexchange.com/a/37879).
