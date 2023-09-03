# Agentes

## automatas.py

Se requiere instalar los paquetes

```{python}
!pip install matplotlib
!pip install imageio
!pip install numpy
```

Dentro de ***flocking.py*** podemos impliementar un algoritmo basado en agentes para modelar el vuelo de parvadas. De acuerdo con los parámetros podemos cambiar distancia de alineación y cohesion, distancia de alejamiento y número de agentes. Así mismo, podemos elegir si los bordes funcionan como muro o continuan como si estuvieran pegados con su extremo opuesto y, por último, si se quiere guardar un gif y las imagenes para crearlo y la ruta.


```{python}
flock(path, d1, d2 n_agentes, guardar, bordes) # con esta función iniciamos el algoritmo
# path -> str  # ruta de guardado de imagenes
# n_nodos -> type int ## Numero de agentes, recomendable para visualización en tiempo real 50, límite para guardado 500, default = 250
# d1 -> type int  # distancia de alineación y cohesión, default 3
# d2  -> type int  # distancia de separación default 2.
# guardar -> boolean #default = True. Para guardar o no el gif e imagenes
# bordes > boolean #default = False. Variable que indica si los agentes chocan con los bordes (TRUE) o continuan por el lado opuesto pegando en forma de Toro (False) 
```

