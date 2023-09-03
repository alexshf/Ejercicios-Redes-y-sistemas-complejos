# Algoritmos Autómatas celulares.

## automatas.py

Se requiere instalar los paquetes

```{python}
!pip install cv2
!pip install numpy
```

Dentro de ***automatas.py*** podemos aplicar dos tipos de reglas para ejecutar autómatas celulares.

```{python}
Aut_Cell_2D(regla) # ejecutará el juego de la vida según el valor de la regla
regla = 'juego de la vida' # Para el juego de la vida
regla = 'solidificación Neumann' # Para ejecutar solidificación de Neumann.
```

El programa abrirá una ventana con rejillas blancas. Cada que presionemos con el mouse un espacio, si se encuentra de color blanco se cambiará a negro y viceversa. Esto generará la condición inicial del juego.

Luego se debe teclear la tecla *"ENTER"* para iniciar el juego con la condición inicial dispuesta y la regla señalada.

## a_c_elemental.py

Se requiere instalar los paquetes

```{python}
!pip install matplotlib
!pip install numpy
```

Dentro de ***a_c_elemental.py*** podemos aplicar las 256 reglas posibles de los autómatas celulares elementales con la función

```{python}
automata_celular_elemental(n) # ejecutará la n-ésima regla de los autómatas celulares elementales
''' n un número entre 0 y 255. Por default (si no elegimos n), se aplicará la regla 30 '''
```

Se graficará el resultado de la regla aplicada.


## codificar_decodificar_imagen.py

Se requiere instalar los paquetes

```{python}
!pip install matplotlib
!pip install numpy
```

Dentro de ***codificar_decodificar_imagen.py*** encontramos un programa que codifica y decodifica una imagen por medio de la aplicación de un autómata celular. Aplicando la función

```{python}
codificar(imagen) # codifica y decodifica la imagen guardando el resultado en un archivo imagen_salida.png
''' imagen = ruta de la imagen a codificar'''
```
![Ejemplo codificación-decodificación de imagen.](https://github.com/alexshf/Ejercicios-Redes-y-sistemas-complejos/blob/main/automatas/imagen_salida.png)
