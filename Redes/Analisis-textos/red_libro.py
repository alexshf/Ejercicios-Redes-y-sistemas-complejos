# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import os
import networkx as nx
import matplotlib.pyplot as plt



def nombres():
    nombres = [['Vito', 'Don_Corleone', 'Don_Vito'], ['Michael'], ['Tom', 'Hagen'],
               ['Santino', "Sonny"], ['Clemenza', 'Peter'],
               ['Tessio', 'Salvatore'], ['Johnny', 'Fontane'],
               ['Kay', 'Adams'], ['Virgil', 'Sollozzo', 'Turco'],
               ['Constanzia', "Connie"], 
               ['Emilio', 'Don_Emilio', 'Don_Barzini', 'Barzini'],
               ['Phillip', 'Don_Tattaglia', 'Don_Phillip', 'Tattaglia'], 
               ['Frederico', "Fredo", 'Freddie'],
               ['Carlo', 'Rizzi'], ['Lucy', 'Mancini'],
               ['Nino', 'Valenti'], ['Jack', 'Woltz'],
               ['Capitán', 'Marc', 'McCluskey'],
               ['Carmella','Mamá'], ['Jules', 'Segal'],
               ['Albert', 'Neri'], ['Luca', 'Brasi'],
               ['Amerigo', 'Bonasera'], ['Rocco', 'Lampone'], 
               ['Genco', 'Abbandando'], ['Bruno'],
               ['Paulie', 'Gatto'], ['Massimo', 'Fanucci'],
               ['Moe', 'Greene'], ['Virginia'], 
               ['Apollonia', 'Vitelli'], ['Don_Tommasino'],
               ['Calo'], ['Fabrizzio'], ['Margot', 'Asthon'],
               ['Coppola'], ['Deanna', 'Dunn'],
               ['Joseph', 'Zaluchi'], ['Tramonti'],
               ['Frank', 'Falcone'], ['Molinari'],
               ['Vincent', 'Florenza', 'Don_Vincent']]
    return nombres
    
def positions():
    pos = dict({'Vito': (50, 100), 'Michael' : (5, 85), 'Tom': (50, 75),
               'Santino': (95, 85), 'Clemenza': (75, 70),
               'Tessio': (25, 70), 'Johnny': (55, 120), 'Nino': (65, 110),
               'Kay': (20, 120), 'Virgil': (5, 15),
               'Constanzia': (14, 101), 'Emilio': (30, 45),
               'Phillip': (60, 30), 'Frederico': (58, 63),
               'Carlo': (36, 117), 'Lucy': (90, 117),
                'Jack': (57, 112),
               'Capitán': (15, 60), 'Carmella': (35, 89), 
               'Jules': (81, 105), 'Albert': (0, 45), 
               'Luca': (90, 45) , 'Amerigo': (35, 101), 
               'Rocco': (81, 21), 'Genco': (48, 106), 
               'Bruno': (25, 15), 'Paulie': (86, 65),
               'Massimo': (35, 75), 'Moe': (15, 65), 
               'Virginia': (47, 113), 'Apollonia': (0, 120), 
               'Don_Tommasino': (5, 110), 'Calo': (12, 107), 
               'Fabrizzio': (7, 103), 'Margot': (65, 120),
               'Coppola': (75, 15), 'Deanna': (65, 117),
               'Joseph': (52, 111), 'Tramonti': (10, 10),
               'Frank': (20, 10), 'Molinari': (30, 10),  
               'Vincent': (40, 10)})
    return pos
    
def limpiar(string):
    str_limp = string.replace('.','')
    str_limp = str_limp.replace(',','')
    str_limp = str_limp.replace(':','')
    str_limp = str_limp.replace(';','')
    str_limp = str_limp.replace('-','')
    str_limp = str_limp.replace('—','')
    str_limp = str_limp.replace('?','')
    str_limp = str_limp.replace('¿','')
    str_limp = str_limp.replace('¡','')
    str_limp = str_limp.replace('!','')
    str_limp = str_limp.replace('(','')
    str_limp = str_limp.replace(')','')
    str_limp = str_limp.replace('"','')
    return str_limp
    
    
def leertxt(libro):
    l=[]
    with open(libro,'r', encoding='utf-8') as f:
        linea = []
        for line in f:
            sucio = line.split()
            limpio = []
            for i in range(0, len(sucio)):
                limpio.append(limpiar(sucio[i]))                
            linea.extend(limpio)
        l.extend(linea)
        
    text_salida = []
    i = 0
    for _ in range(0, len(l)):
        if 'Don' in l[i]:
            text_salida.append(l[i] + '_' + l[i+1])
            i += 1
        else:
            text_salida.append(l[i])
            i += 1
        if i == len(l)-1:
            break
    return text_salida

def contar_nombres(texto_tabla, len_conexion):
    nombre = nombres()
    pos_coin = []
    pos_nom = []
    i = 0
    while i < len(texto_tabla):
        encontrado= False
        for n in nombre:
            for ap in n:
                if ap == texto_tabla[i]:
                    pos_coin.append(i)
                    encontrado = True
                    if texto_tabla[i+1] in n:
                        i += 1
                    if texto_tabla[i+2] in n:
                        i += 1
                    break
            if encontrado:
                pos_nom.append(n[0])
                break
        i += 1
        
    d = {'Ocurrencia': pos_coin, 'nombre': pos_nom}
    df = pd.DataFrame(data=d)

    return df    

def crea_red(df, rango):
    G = nx.DiGraph()
    nombre = nombres()
    contadores = df['nombre'].value_counts()
    for n in nombre:
        G.add_node(n[0], tam=contadores.loc[n[0]]+30)
    del nombre
    

    conexiones = []
    tam_arr = []
    for i in  range(0, len(df)-1):
        j = i + 1 
        while (df.iloc[j,0]-df.iloc[i,0] <= rango) and (j<len(df)-1):
            if df.iloc[i, 1] != df.iloc[j, 1]:
                try:
                    tam_arr[conexiones.index((df.iloc[i, 1], df.iloc[j, 1]))] += 1
                except:
                    conexiones.append((df.iloc[i, 1], df.iloc[j, 1]))
                    tam_arr.append(1)
            j += 1
                    
    
    G.add_weighted_edges_from([(a[0], a[1], t) for a, t in zip(conexiones,tam_arr)]) 

    return G


def analisis_texto(Ruta, libro):
    nombre = os.path.join(Ruta, libro)
    texto_tabla = leertxt(libro)
    len_conexion = 15
    df = contar_nombres(texto_tabla, len_conexion)
    G = crea_red(df, len_conexion)

    arr_tam = [x[2].get('weight') for x in G.edges.data()]
    arr_col = [(0, 0, 0, (9*(x-min(arr_tam))/(10*max(arr_tam)))+(1/10)) for x in arr_tam]
    nodo_tam = [x.get('tam') for x in np.array(G.nodes.data())[:, 1]]
    subax1 = plt.subplot(111)
    nx.draw_networkx(G, pos= positions(), with_labels=True, font_weight='bold', arrows=True,
                      node_size=nodo_tam, arrowsize=arr_tam, 
                      font_color=(.8, 0, 0), font_size=11, edge_color=arr_col)
    plt.show()

