# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 14:21:17 2022

@author: Alejandro HF
"""
import numpy as np
import matplotlib.pyplot as plt
import time
    
def renglon2dec(renglon):
    rep = len(renglon) // 8
    reng_sal = np.zeros(rep, dtype=int)
    for i in range(0, rep):
        exp = 7
        dec = 0
        for j in range(0,8):
            dec += int(renglon[(i*8)+j]*(2**exp))
            exp -= 1
        reng_sal[i] = dec
    return reng_sal
    
def imgbin2dec(imagen, T):
    img_cif = np.zeros((len(imagen), len(imagen[0])// 8, 3), dtype=int)
    for i in range(0, len(imagen)):
        for rgb in range(0, 3):
            img_cif[i,:,rgb] = renglon2dec(imagen[i,:,rgb])
    return img_cif
        
    
def automata_cifrar(C_inicial, T, l):
    R_salida = np.zeros((T+2, len(C_inicial[0])), dtype=int)
    R_salida[0] = list(map(int,C_inicial[0]))
    R_salida[1] = list(map(int,C_inicial[1]))
    indices = np.arange(0, len(C_inicial[0])+1)
    indices[-1] = 0
    for t in range(2, T+2):
        for i in range(0, len(C_inicial[0])):
            R_salida[t, i] = (l[0]*R_salida[t-1, i-1]+l[1]*R_salida[t-1, i]+\
                l[2]*R_salida[t-1, indices[i+1]] + R_salida[t-2, i]) % 2
    C_salida = R_salida[-2:,:]
    return C_salida

def automata_descifrar(C_inicial, T, l):
    R_salida = np.zeros((T+2, len(C_inicial[0])), dtype=int)
    R_salida[-2] = list(map(int,C_inicial[0]))
    R_salida[-1] = list(map(int,C_inicial[1]))
    indices = np.arange(0, len(C_inicial[0])+1)
    indices[-1] = 0
    for t in range(T-1,-1,-1):
        for i in range(0, len(C_inicial[0])):
            R_salida[t, i] = (l[0]*R_salida[t+1, i-1]+l[1]*R_salida[t+1, i]+\
                l[2]*R_salida[t+1, indices[i+1]] + R_salida[t+2, i]) % 2    
    C_salida = R_salida[:2]
    return C_salida

def ceros_rest(n):
    return '0' * n

def dec2bin(n):
    binario = bin(n)
    ceros = ceros_rest(8-len(binario)+2)
    return binario.replace("0b", ceros)

def convertir_imagen_to_bin(imagen, T, l, clave='codificar'):
    if len(imagen)%2 != 0:
        img_cif = np.zeros((len(imagen)+1, len(imagen[0]), 3), dtype=int)
    else:
        img_cif = np.zeros((len(imagen), len(imagen[0]), 3), dtype=int)

    
    for rgb in range(0, 3):
        for i in range(0, len(imagen)):
            if i % 2 == 0:
                imagen_bin = ['','']
                img_cif_bin = np.zeros((2, len(imagen[0])*8), dtype=int)
            for j in range(0, len(imagen[0])):
                imagen_bin[i%2] +=  dec2bin(imagen[i,j, rgb])
            if i % 2 == 1:
                if clave == 'codificar':
                    img_cif_bin = automata_cifrar(imagen_bin, T, l)
                elif clave == 'decodificar':
                    img_cif_bin = automata_descifrar(imagen_bin, T, l)
                    
                img_cif[i-1,:,rgb] = renglon2dec(img_cif_bin[0])
                img_cif[i,:,rgb] = renglon2dec(img_cif_bin[1])
            if len(imagen)%2 != 0 and i==len(imagen)-1:
                for j in range(0, len(imagen[0])):
                    binario = dec2bin(imagen[0,j, rgb])
                    ind = 0
                    for b in range(0,8):
                        if b >= 8-len(binario):
                            imagen_bin[1, (j*8)+b] = int(binario[ind])
                            ind += 1
                if clave == 'codificar':
                    img_cif_bin = automata_cifrar(imagen_bin, T, l)
                elif clave == 'decodificar':
                    img_cif_bin = automata_descifrar(imagen_bin, T, l)
                img_cif[-2,:,rgb] = renglon2dec(img_cif_bin[0,:,rgb])
                img_cif[-1,:,rgb] = renglon2dec(img_cif_bin[1,:,rgb])
    return img_cif



def codificar(nombre):
    imagen = plt.imread(nombre)
    T = 5
    l = [1, 0, 1]
    img_cif = convertir_imagen_to_bin(imagen, T, l)
    img_dec = convertir_imagen_to_bin(img_cif, T, l, clave='decodificar')
    fig, ax = plt.subplots(3)
    ax[0].imshow(imagen)
    ax[0].axis('off')
    ax[0].set_title('Original')
    ax[1].imshow(img_cif)
    ax[1].axis('off')
    ax[1].set_title('Codificada')
    ax[2].imshow(img_dec)
    ax[2].axis('off')
    ax[2].set_title('Deodificada')

    plt.savefig('imagen_salida.png', dpi=300)
