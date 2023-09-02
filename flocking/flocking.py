# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 19:22:44 2022

@author: Alejandro HF
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import time
import imageio
import os



def grafica(ave):
    plt.scatter(ave.posicion[0],ave.posicion[1], marker=ave.marker, c="black", s=40) 
    plt.axis('off') 


def distancia(a,b):
    return np.sqrt(np.sum((a-b)**2))

def encuentra_vecinos(bandada, d1, d2):
    len_ban = len(bandada)
    v_ali_coh = [ [] for _ in range(len_ban)]
    v_sep = [ [] for _ in range(len_ban)]
    for i in range(0, len_ban-1):
        a_pos = bandada[i].posicion
        for j in range(i+1, len_ban):
            x_pos = bandada[j].posicion
            dist = distancia(a_pos, x_pos)
            if dist <= d1 and dist >= d2:
                v_ali_coh[i].append(bandada[j])
                v_ali_coh[j].append(bandada[i])
            elif dist <= d2:
                v_sep[i].append(bandada[j])
                v_sep[j].append(bandada[i])
        bandada[i].v_ali_coh = v_ali_coh[i]
        bandada[i].v_sep = v_sep[i]
    bandada[-1].v_ali_coh = v_ali_coh[-1]
    bandada[-1].v_sep = v_sep[-1]
    
def crea_bandada(largo, ancho, n_nodos):
    bandada = []
    for _ in range(0, n_nodos):
        bandada.append(ave(largo=largo, ancho=ancho))
    return bandada

def normalize(v):
    """ Normalize a vector to length 1. """
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return np.array(v / norm, dtype=float)

class ave:
    def __init__(self,
               ancho=None,
               largo=None,
               v_sep=None,
               v_ali_coh=None,
               marker=None,
               bandada=None):
        self.velocidad = self.new_vel()
        self.posicion = self.new_pos(ancho, largo)
        self.v_ali_coh = v_ali_coh
        self.v_sep = v_sep
        self.marker = self.update_marcador()
    
    def new_vel(self):
        return normalize(np.random.uniform(low=-1, high=1, size=2))
    
    def new_pos(self, ancho, largo):
        return np.array([float(np.random.uniform(low=1, high=ancho-1)),
                         float(np.random.uniform(low=1, high=largo-1))])
    
    def update_vel(self, ancho, largo):
        """ aplica las reglas para cambiar velocidad"""
        vecinos = self.v_ali_coh 
        pos = self.posicion
        """Alignment rule, cohesion"""
        vel_alig = np.array([0., 0.])
        vel_cohe = np.array([0., 0.])
        if vecinos != []:
            for v in vecinos:
                vel_alig += v.velocidad
                vel_cohe += v.posicion
            vel_alig /= len(vecinos)
            vel_cohe /= len(vecinos)
            vel_cohe -= pos
        del vecinos
            
        
        """Separación"""
        vel_sep = np.array([0., 0.])
        vel = self.velocidad
        vecinos = self.v_sep
        if vecinos != []:
            for v in vecinos:
                vel_sep += (pos-v.posicion)/distancia(v.posicion, pos)
            vel_sep /= len(vecinos)
            
        # aplicamos el cambio de la velocidad y actualizamos posición    
        self.velocidad = normalize(vel+ 1*vel_alig + 0.5*vel_cohe + 1*vel_sep)
        self.marker = self.update_marcador()
        self.update_pos(ancho, largo)
        
    def update_pos(self, ancho, largo):
        """actualiza la posición dependiendo de la velocidad"""
        p_vel = 0.25
        vel = self.velocidad
        pos = self.posicion
        
        """para hacer del espacio un toro"""
        new_pos = (p_vel*vel + pos)% ancho
        
        """si se quiere poner bordes que repelen a los agentes"""
        if bordes:
            new_pos = p_vel*vel + pos
            if new_pos[0] < 0 or new_pos[0] > ancho:
                if new_pos[1] < 0 or new_pos[1] > largo:
                    self.velocidad = np.array([-vel[0], -vel[1]])
                    new_pos = p_vel*self.velocidad + pos
                    self.marker = self.update_marcador()
                else:
                    self.velocidad = np.array([-vel[0], vel[1]])
                    new_pos = p_vel*self.velocidad + pos
                    self.marker = self.update_marcador()
            elif new_pos[1] < 0 or new_pos[1] > largo:
                self.velocidad = np.array([vel[0], -vel[1]])
                new_pos = p_vel*self.velocidad + pos
                self.marker = self.update_marcador()
        
        # guarda la posición
        self.posicion = new_pos
        
    def update_marcador(self):
        """esta función actualiza el sentido de la flecha"""
        vel = self.velocidad
        i_v = np.array([1, 0])
        dot_product = np.dot(vel, i_v)
        t = mpl.markers.MarkerStyle(marker='$->$')
        angulo = np.arccos(dot_product)*180/math.pi
        t._transform = t.get_transform().rotate_deg(np.sign(vel[1])*angulo)
        return t

def flock(path, d1 = 3, d2 = 2, n_nodos = 250, guardar=True, bordes = False):
    global ancho, bordes
    ancho = 40 # ancho pantalla
    largo = 40 # largo pantalla      
    # n_nodos = 250 ## Numero de agentes, estable en 50, guardado 500
    # d1 = 3 # distancia de alineación y cohesión
    # d2 = 2 # distancia de separación
    bandada = crea_bandada(largo, ancho, n_nodos) #crea agentes
    
    """grafica"""
    plt.ion()
    fig = plt.figure()
    fig.subplots_adjust(wspace=0, hspace=0, top=1, bottom=0)
    fig.set_size_inches(18, 18)
    fig.set_dpi(300)
    plt.plot([]) 
    plt.clf()
    plt.axis('off')
    plt.xlim([0, ancho])
    plt.ylim([0, largo])
    
    
    
    time.sleep(1/24)
    #plt.scatter(100,50, marker=(3, 0, 0))
    
    for x in bandada:
        plt.scatter(x.posicion[0],x.posicion[1], marker=x.marker, c="black", s=40) 
        plt.axis('off')
            
    
    fig.canvas.draw()
    fig.canvas.flush_events()
    for i in range(0, 1000):  
        plt.clf()
        
        # t0 = time.time()
        """encuentra los vecinos de cada agente"""
        encuentra_vecinos(bandada, d1, d2)
        # t1 = time.time()    
        # total = t1-t0
        # print('vecinos', total)
        # t0 = time.time()
        """actualiza posciiones"""
        for x in bandada:
            x.update_vel(ancho, largo)
        # t1 = time.time()    
        # total = t1-t0
        # print('velocidades', total)
        
        # t0 = time.time()
        """grafica (es la función que tarda más)"""
        list(map(grafica, bandada))  
    
        # t1 = time.time()
        # total = t1-t0
        # print('plot', total)
    
        plt.xlim([0, ancho])
        plt.ylim([0, largo])
        fig.canvas.draw()
        fig.canvas.flush_events()
        if guardar:
            plt.savefig(os.path.join(path, str(i)+'.png')) 
        
    """para guardar"""
    if guardar:
        with imageio.get_writer('flocking.gif', mode='I') as writer:
            for i in range(0, 1000):
                image = imageio.imread(os.path.join(path, str(i)+'.png'))
                writer.append_data(image)
