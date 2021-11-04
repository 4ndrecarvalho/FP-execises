# You throw a dart that hits coordinates (x, y) on a dartboard.
# Create a program that gives you the score.
# See:
#   https://en.wikipedia.org/wiki/Darts#Dartboard
#   https://www.dimensions.com/element/dartboard
#__________________________________________________
# andre.dc@ua.pt                         26/10/2021
#__________________________________________________

print("Enter the coordinates in milimeters from the center of the board.")
x = float(input("x? "))
y = float(input("y? "))

# Points of the sectors, clockwise from the top
# Example: the sector right from the center is POINTS[5] == 6.
POINTS = (20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5)

# COMPLETE...
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches

def printBoard(x, y, score, points): 
    """
    Desenha o tabuleiro e a posição do dardo
    """
    inner_bullseye = plt.Circle((0, 0), 12.5, color = 'r', zorder = 2)
    outer_bullseye = plt.Circle((0, 0), 32, color = 'g', zorder = 2)
    triple_ring = plt.Circle((0,0), 99, color = 'r', fill=False, zorder = 2)
    triple_ring1 = plt.Circle((0,0), 107, color = 'r', fill=False, zorder = 2)
    double_ring = plt.Circle((0,0), 162, color = 'g', fill=False, zorder = 2)
    double_ring1 = plt.Circle((0,0), 170, color = 'g', fill=False, zorder = 2)
    out = plt.Circle((0,0), 225, color = 'black', linewidth = 2.5, fill=False, zorder = 2)
    numbers = matplotlib.patches.Wedge((0,0), 225, 0, 360, width = 55,  color = 'black', zorder = 0)
    dart = plt.Circle((x,y), 8, color = 'orange', ec='black', zorder = 2)

    fig, ax = plt.subplots()
    plt.axis('equal')
    ax.set_xlim((-260,260))
    ax.set_ylim((-260,260))

    n = 20
    ang = np.linspace(np.pi/2, (5*np.pi)/2, n+1)
    xi = 225 * np.cos(ang + (9 / (180 / math.pi)))
    yi = 225 * np.sin(ang + (9 / (180 / math.pi)))
    # Posição das labels das zonas
    x0 = 190 * np.cos(ang)
    y0 = 190 * np.sin(ang)

    # Dividir circulo em 20 partes iguais e pintar zonas
    for k in range(0, len(xi)-1):
        plt.plot([0 ,xi[k]], [0 , yi[k]], color = 'black', zorder=1)
        if k % 2:
            out_num = matplotlib.patches.Wedge((0,0), 162, 9 + ang[k] * (180/math.pi), 9 + ang[k+1] * (180/math.pi), width = 130,  color = 'black', zorder = 0)
            mid_triple = matplotlib.patches.Wedge((0,0), 107, 9 + ang[k] * (180/math.pi), 9 + ang[k+1] * (180/math.pi), width = 8,  color = 'red', zorder = 0 )
            mid_double = matplotlib.patches.Wedge((0,0), 170, 9 + ang[k] * (180/math.pi), 9 + ang[k+1] * (180/math.pi), width = 8,  color = 'red', zorder = 0 )
            ax.add_patch(out_num)
            ax.add_patch(mid_double)
            ax.add_patch(mid_triple)
        else:
            mid_triple2 = matplotlib.patches.Wedge((0,0), 107, 9 + ang[k] * (180/math.pi), 9 + ang[k+1] * (180/math.pi), width = 8,  color = 'g', zorder = 0)
            mid_double2 = matplotlib.patches.Wedge((0,0), 170, 9 + ang[k] * (180/math.pi), 9 + ang[k+1] * (180/math.pi), width = 8,  color = 'g', zorder = 0)
            ax.add_patch(mid_double2)
            ax.add_patch(mid_triple2)
    # Labels
        x_disp = -20 if xi[k] < 0 else -10
        y_disp = -20 if yi[k] < 0 else 0
        plt.text(x0[k] + x_disp, y0[k] + y_disp, points[-k], color = 'white', fontsize = 15)

    ax.add_patch(outer_bullseye)
    ax.add_patch(inner_bullseye)
    ax.add_patch(triple_ring)
    ax.add_patch(double_ring)
    ax.add_patch(triple_ring1)
    ax.add_patch(double_ring1)
    ax.add_patch(numbers)
    ax.add_patch(out)
    ax.add_patch(dart)
    plt.title("SCORE: {}{}".format(score, "\nOut of bounds!!!" if score == 0 else ""))
    plt.show()

def dartScore(circ_area):
    x = lambda circ_area, bottom_limit, upper_limit : (circ_area > (bottom_limit ** 2) and circ_area <= (upper_limit ** 2))
    score = 50 if x(c_area, 0, 12.5) else 25 if x(c_area, 12.5, 32) else POINTS[m_angle] if x(c_area, 32, 99) else 3*POINTS[m_angle] if x(c_area, 99, 107) else POINTS[m_angle] if x(c_area, 107, 162) else 2*POINTS[m_angle] if x(c_area, 162, 170) else 0
    return score

def recToPolar(x,y):
    p = np.array([x,y])
    norm = np.linalg.norm(p)
    p_norm = p / norm
    vector = (p_norm[1]) 
    angle = math.acos(vector) * 180 / math.pi
    return vector, angle

# Cálculos inerentes à posição do dardo
vec, ang = recToPolar(x, y)
# cada triangulo tem uma variação de 18º, esta variável serve para definir qual o indice de POINTS a usar.
m_angle = int((ang + 9) / 18)     
# neste caso o programa é agnóstico para angulos superiores a 180º é preciso diferenciar os quadrantes.
m_angle = -m_angle if x <= 0 else m_angle
# area correspondente à circunferência ou anel
c_area = (x ** 2 + y ** 2)     
score = dartScore(c_area)

print("SCORE: {}{}".format(score, "\nOut of bounds!!!" if score == 0 else ""))
printBoard(x, y, score, POINTS)
