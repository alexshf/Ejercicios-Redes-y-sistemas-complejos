# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 21:35:10 2022

@author: Alejandro HF
"""
import numpy as np
import matplotlib.pyplot as plt
import os
import imageio.v2 as imageio
import mpl_toolkits.axes_grid1 as axes_grid1
import time


def reglas_reacciondifusion(celdas, df):
    porc_dif = [[.2, [[0, 1], [1, 0], [1, 2], [2, 1]]],
                [.05, [[0, 0], [0, 2], [2, 0], [2, 2]]]] ## aporte por vecinos
    celda_sal = 0 
    for i in porc_dif:
        for j in i[1]:
            celda_sal += df*i[0]*celdas[j[0], j[1]]
    return celda_sal

def matriz_nueva(matriz_entrada):
    s = (np.size(matriz_entrada, 0), np.size(matriz_entrada, 1))
    matriz_inicial = np.zeros((s[0]+2, s[1]+2))
    matriz_inicial[1:-1, 1:-1] = matriz_entrada
    # condiciones de frontera
    matriz_inicial[1:-1,0] = 0
    matriz_inicial[1:-1,-1] = 0
    matriz_inicial[0] = 0                              
    matriz_inicial[-1] = 0  
    return matriz_inicial

def aplicar_reglas(A, B, dfA, dfB, f, r, k, dt):
    s = (np.size(A, 0), np.size(A, 1))
    # creamos una matriz pegando fronteras
    A1 =  matriz_nueva(A)
    B1 =  matriz_nueva(B)
    # matriz donde guardamos datos                          
    A_sal = np.zeros(s)
    B_sal = np.zeros(s)
    ## para cada celda aplicamos las reglas, dependiendo qué regla
    for i in range(0, s[0]):
        for j in range(0, s[1]):
            aporteA = reglas_reacciondifusion(A1[i :i + 3, j :j + 3], dfA)
            DeltaA = aporteA - (dfA*A[i, j])    
            aporteB = reglas_reacciondifusion(B1[i :i + 3, j :j + 3], dfB)
            DeltaB = aporteB - (dfB*B[i, j])
            A_sal[i, j] = A[i, j] + (DeltaA + (f*(1- A[i, j])) \
                - (r * A[i, j] * ((B[i, j])**2)))*dt
            B_sal[i, j] = B[i, j] + (DeltaB - k*B[i,j] + (r*A[i, j]*((B[i,j])**2)))*dt
    return [A_sal, B_sal]

def image_salida(A, B):
    return B/(A+B)
######### función 

def patrones(path, tam = 101, dA = 1., dB = .5, f = 0.034, k = 0.095, r = 1, dt = 1):
    A = np.ones((tam, tam), dtype=float) ## difusión
    B = np.zeros((tam, tam), dtype=float) ## Reaccion
    index = [int(tam/2),int(tam/2)]

    B[index[0]-5:index[0]+6, index[0]-5:index[0]+6] = 1 #condicion inicial

    ## dibujamos la imagen con rejilla y esperamos a que se dé una condición inicial
    fig = plt.figure()

    ind = 0
    for i in range(3500):
        if i % 30 == 0:
            plt.clf()
            matriz_im = image_salida(A, B)
            grid = axes_grid1.AxesGrid(fig, 111, nrows_ncols=(1,1), 
                                        axes_pad = 0.5, cbar_location = "right",
                                        cbar_mode="each", cbar_size="15%", cbar_pad="5%",)
            im0 = grid[0].imshow(matriz_im, cmap='plasma')
            grid[0].set_title(f'iteracion {i}')
            grid.cbar_axes[0].colorbar(im0)
            grid.cbar_axes[0].set_yticks([])
            
            fig.canvas.draw()
            fig.canvas.flush_events()
            plt.savefig(os.path.join(path, str(ind)+'.png')) 
            time.sleep(1)
            ind += 1
        [A, B] = aplicar_reglas(A, B, dA, dB, f, r, k, dt)
   

    fps=20
    ind -= 1
    """para guardar"""
    with imageio.get_writer('patrones.gif', mode='I', fps=fps, subrectangles=True) as writer:
        for i in range(0, ind):
            image = imageio.imread(os.path.join(path, str(i)+'.png'))
            writer.append_data(image)

        writer.close()
