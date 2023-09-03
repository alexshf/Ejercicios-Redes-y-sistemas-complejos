# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 11:36:15 2022

@author: Alejandro HF
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
import random 
import math
import os
import imageio
#############################
############################
######### PUNTO 1 ###########
#############################
############################

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)




#############################
############################
######### PUNTOS > 1 ###########
#############################
############################

def distribucion_grado(n, conexiones):
    m = len(conexiones)
    grados = np.zeros(n)
    for i in range(0, n):
        for c in conexiones:
            if i == c[0] or i == c[1]:
                grados[i] += 1
    
    distr = np.zeros(n-1)
    for i in range(1, n):
        for g in grados:
            if g == i:
                distr[i-1] += 1
    distr = distr/n
        
    n_p = (n*(n-1))/2
    pc = m / n_p
    binom = np.array([nCr(n-1, k)*(pc**k)*((1-pc)**(n-1-k)) for k in range(0, n-1)])
    z = 2*m/n
    # poiss = np.array([math.exp(z)*((z**k))/ math.factorial(k) for k in range(0, n-1)])
    
    return [distr, binom]
    

def proceso_markov_montecarlo(indices_edges):
    rand_arist = np.array(random.sample(comb, 1)[0], dtype=int) # Elegimos al azar un par de vértices
    indices_pos = [] 
    agrega = True
    signo = -1
    for x in indices_edges:
        if (rand_arist[0] != x[0]) or (rand_arist[1] != x[1]):
            indices_pos.append(x)
        else:
            agrega = False
            signo = 1
    if agrega:
        indices_pos.append(rand_arist)
        indices_pos = np.array(indices_pos, dtype=int)
    else:
        indices_pos = np.array(indices_pos, dtype=int)
    
    r = np.random.uniform() # elegimos r al azar en [0,1]
    if r <=  (math.exp(signo*theta)): 
        ## cambiamos a 0 si era 1, y a uno si era 0
        valor_nuevo = int(1 - M_adyacencia[rand_arist[1], rand_arist[0]])
        M_adyacencia[rand_arist[0], rand_arist[1]] = valor_nuevo
        M_adyacencia[rand_arist[1], rand_arist[0]] = valor_nuevo
        if valor_nuevo:
            G.add_edge(*rand_arist)
        else:
            G.remove_edge(*rand_arist)
        # print('casi_salida', indices_pos)
        del indices_edges
        indices_edges = indices_pos
    
    return indices_edges

def Erdos_Renyi_graph(guardar=True, path=None, n=30)
# n - nodos

    M_adyacencia =  np.zeros((n, n), dtype=int) # matriz de adyacencia sin aristas
    # gráfica python
    G = nx.Graph() # Creamos gráfica
    nodos = np.arange(0, n) # etiquetamos nodos con números
    G.add_nodes_from(nodos) # Agregamos nodos a la red
    
    """Agregamos aristas aleatoriamente"""
    comb = list(combinations(nodos, 2)) # todas las posibles de aristas
    total_comb = len(comb)
    N = np.random.randint(0, total_comb, dtype=int) # cantidad de aristas iniciales
    indices_edges = np.array(random.sample(comb, N)) # elegimos al azar las aristas
    
    Em = int(total_comb*1/3)  # aristas promedio
    theta = math.log(((n*(n-1))/(2*Em)) - 1)  # valor de theta
    n_p = (n*(n-1))/2
    pc = Em / n_p
    binom_esp = np.array([nCr(n-1, k)*(pc**k)*((1-pc)**(n-1-k)) for k in range(0, n-1)])
    
    for i in indices_edges: #actualizamos matriz con aristas
        M_adyacencia[i[0], i[1]] = 1
        M_adyacencia[i[1], i[0]] = 1
    # crea aristas en red 
    G.add_edges_from(indices_edges)
    
    [distr, binom] = distribucion_grado(n, indices_edges)
    x = np.arange(1, n)
    
    
    path = 'G:/Mi unidad/maestria/materias/Redes y sistemas complejos/tareas/imagenes' # para guardar
    fig = plt.figure(figsize=(10, 10))
    repeticiones = 2000
    m_G = [len(indices_edges)]
    ind = 0
    for i in range(repeticiones):
        axes1 = fig.add_axes([0.001, 0.1, (1/2)-0.01, 1-0.2])
        nx.draw_circular(G, ax=axes1)
        axes1.set_title('Gráfica $G(t_i)$')
        
        axes2 = fig.add_axes([1/2+0.1, 1/6, 1/2-0.2, 1/4])
        axes2.plot(np.arange(0, len(m_G)), m_G, 'b-')
        axes2.plot(np.arange(0, len(m_G)), np.ones(len(m_G))*Em, 'r-')
        axes2.set_xlim(left=0, right=repeticiones)
        axes2.set_ylim(bottom=0, top=max(m_G[0], 2*Em))
        axes2.set_title(f'$m(G(t_i)) = {G.number_of_edges()}$ \n $<m> = {Em}$')
        axes2.set_xlabel('Iteración ($t_i$)')
        axes2.set_ylabel('#Vértices ($m(G(t_i))$)') 
        
        axes3 = fig.add_axes([1/2+0.1, 4/6, 1/2-0.2, 1/4])
        axes3.bar(x, distr, color='b', label='Distribución Real')
        axes3.plot(x, binom, 'b-', label='Ajuste binomial')
        axes3.plot(x, binom_esp, 'r-', label='Distribución esperada')
        axes3.set_ylim(bottom=0, top=0.65)
        axes3.set_title('Distribución de grado $P(k)$')
        axes3.set_xlabel('grado k')
        axes3.set_ylabel('$P(k)$') 
        plt.legend(loc='upper left')
        fig.canvas.draw() ## dibuja nuevo eje en figura
        fig.canvas.flush_events() ## dibuja nuevo eje en figura
        if i % 32 == 0 and guardar:
            plt.savefig(os.path.join(path, str(ind)+'.png')) # para guardar
            ind += 1
        # nuevo paso
        indices_edges = proceso_markov_montecarlo(indices_edges)
        if G.number_of_edges() != len(indices_edges):
            print(G.number_of_edges(), len(indices_edges))
        m_G.append(len(indices_edges))
        [distr, binom] = distribucion_grado(n, indices_edges)
        plt.clf() #borra el dibujo en la figura
        
    ind -= 1
    
    """para guardar"""
    if guardar:
        with imageio.get_writer('Erdos_Renyi_MM.gif', mode='I', 
                                fps=int(ind/20), subrectangles=True) as writer:
            for i in range(0, ind):
                image = imageio.imread(os.path.join(path, str(i)+'.png'))
                writer.append_data(image)
    
