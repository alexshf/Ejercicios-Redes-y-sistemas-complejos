# Redes

## Analisis-textos

Esta carpeta contiene un proyecto que permite analizar un texto utilizando redes.

## erdos_renyi.py

Dentro de ***erdos_renyi.py*** podemos construir una red de tipo Erdos-Renyi de $n$ nodos aplicando el proceso markoviano montecarlo.

```{python}
Erdos_Renyi_graph(guardar, path, n) # ejecutará el juego de la vida según el valor de la regla
# guardar (type boolean, default=False) -> variable que indica si guardar o no el proceso de aproximación a la red.
# path (type str, defualt=None) -> variable que indica la ruta donde guardar imágenes.
# n (type int, default=30) -> variable que indica la cantidad de nodos de la red.
```

Si se acepta guardar, se guardará una carpeta con imagenes que se utilizarán para crear un gif que también se guardará.
