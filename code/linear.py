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
    x_fit = np.linspace(20,60,100)
    y_fit = slope * x_fit + intercept

    plt.scatter(x,y)
    plt.xlabel('overall')
    plt.ylabel('score')
    plt.plot(x_fit,y_fit,linestyle='--')
    plt.show()
    
    return (slope,intercept)




def linear_planet(p,avgpx):
    #dict = {}
    d2 = {}
    d1 = {}
    d3 = {}


    for ovr in range(10,60,1):
        t = mod_max_score(ovr,avgpx,p)
        d1[ovr] = t[0]      #求出工作人数与总人数的线性关系
        d2[ovr] = t[1]      #求出实际产销与总人数的线性关系
        d3[ovr] = t[2]      #求出产销与工作人数比值 和 总人数 的线性关系

    return (draw_linear(d1),draw_linear(d2),draw_linear(d3))


p = info(yiju=20)
print(linear_planet(p,50))





