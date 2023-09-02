# Algoritmos Automátas celulares.

Se requiere instalar los paquetes

```{python}
!pip install cv2
!pip install numpy
```

Dentro de **"automatas.py"** podemos aplicar dos tipos de reglas para ejecutar automátas celulares.

```{python} Aut_Cell_2D(regla) # ejecutará el el juego de la vida según el valor de la regla

regla = 'juego de la vida' # Para el juego de la vida
regla = 'solidificación Neumann' # Para ejecutar solidificación de Neumann.  ```

El programa abrirá una ventana con rejillas blancas. Cada que presionemos con el mouse un espacio, si se encuentra de color blanco se cambiará a negro y viceversa. Esto generará la condición inicial del juego.

Luego se debe teclear la tecla *"ENTER"* para iniciar el juego con la condición inicial dispuesta y la regla señalada.

