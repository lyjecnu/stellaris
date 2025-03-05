from planet import mod_max_score
import matplotlib.pyplot as plt
from planet_class import info
from scipy.stats import linregress
import numpy as np



def draw_linear(dict):
    x = list(dict.keys())
    y = list(dict.values())
    for i in range(len(x)):
        x[i] = int(x[i])
        
        
    slope,intercept,r_value,p_value,std_err = linregress(x,y)
    x_fit = np.linspace(10,60,100)
    y_fit = slope * x_fit + intercept
    return (slope,intercept)


    '''
    plt.scatter(x,y)
    plt.xlabel('workers')
    plt.ylabel('score')
    plt.plot(x_fit,y_fit,linestyle='--')
    #plt.show()
    '''


def linear_planet(p,avgpx):
    dict = {}
    d2 = {}
    d3 = {}


    for worker in range(10,60,1):
        t = mod_max_score(worker,avgpx,p)
        dict[str(worker)] = (worker + 2 + 2*(p.yiju < 100) + worker // 30+ t[0]) * t[1] / 100   #修改电
        d2[str(worker)] = worker + t[0]
        d3[str(worker)] = t[1]

    return (draw_linear(dict),draw_linear(d2))


p = info(yiju=70)
print(linear_planet(p,35))





