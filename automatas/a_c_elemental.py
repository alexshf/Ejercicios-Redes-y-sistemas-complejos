import numpy as np
from matplotlib import pyplot as plt


def aplicar_reglas_aut(t, regla):
    ## convertimos a binario y agregamos ceros para completar los 8 estados
    if (regla >= 0 and regla <= 255) and isinstance(regla, int):
        regla = str(bin(regla).replace("0b", ""))[::-1]
        for _ in range(0, 8 - len(regla)):
            regla += "0"
        regla = regla[::-1]
    else:
        print("No existe esa regla :C")

    ## estos son los estados posibles
    estados = [[1, 1, 1], [1, 1, 0], [1, 0, 1],
               [1, 0, 0], [0, 1, 1], [0, 1, 0],
               [0, 0, 1], [0, 0, 0]]
    mod = len(t)
    # recorremos de 3 en 3 comparando t con los estados y devolviendo lo indicado por la regla
    t_n = []
    for i in range(0, len(t)):
        e_inicial = [t[i - 1], t[i], t[(i + 1) % mod]]
        for j in range(0, len(estados)):
            if e_inicial == estados[j]:
                t_n.append(int(regla[j]))
                break
    return t_n

def automata_celular_elemental(regla = 256)
    ancho = 1200
    largo = 500
    punto_medio = (ancho//2) + (ancho % 2)

    ## estado inicial en el punto medio
    t_0 = np.ndarray.tolist(np.zeros(ancho, dtype=int))
    t_0[punto_medio] = 1

    t_n = [t_0]
    for _ in range(0, largo):
        t_n.append(aplicar_reglas_aut(t_n[-1], regla))

    fig = plt.figure()
    fig.set_size_inches((10, 5))
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(t_n, cmap='PRGn')

    # estado inicial aleatorio
    rng = np.random.default_rng()
    t_0_rand = rng.integers(low=0, high=2, size=ancho)
    t_n_rand = [t_0_rand]
    for _ in range(0, largo):
        t_n_rand.append(aplicar_reglas_aut(t_n_rand[-1], regla))

    fig2 = plt.figure()
    fig2.set_size_inches((10, 5))
    ax2 = plt.Axes(fig2, [0., 0., 1., 1.])
    ax2.set_axis_off()
    fig2.add_axes(ax2)
    ax2.imshow(t_n_rand, cmap='PRGn')

    plt.show()
