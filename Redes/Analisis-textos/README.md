# Análisis texto (el Padrino).

Se requiere instalar los paquetes

```{python}
!pip install pandas
!pip install matplotlib
!pip install networkx
!pip install numpy
```

Dentro de ***red_libro.py*** se gace un análisis de conexiones entre los personajes principales que aparecen en el libro *El padrino*, a través de redes matemáticas. El archivo puede ser modificado fácilmente para un análisis de cualquier libro, actualizando los nombres y las posiciones de los nodos de red.

```{python}
analisis_texto(Ruta, libro) # ejecutará el análisis del texto, retornando una red de conexiones dirigidas.
ruta = ruta-libro # ruta donde se encuentra el libro en formato .txt
libro = nombre-libro #nombre del libro con extensión.
```
El archivo pdf contiene un análisis más detallado del libro de acuerdo con los resultados obtenidos.
