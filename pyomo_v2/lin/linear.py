import copy
import json
from lin.basic_func import mod_max_score
import matplotlib.pyplot as plt
from stats.planet_class import info
from scipy.stats import linregress
import numpy as np



def draw_linear(dict):
    x = list(dict.keys())
    y = list(dict.values())
    for i in range(len(x)):
        x[i] = int(x[i])
        
        
    slope,intercept,r_value,p_value,std_err = linregress(x,y)

    '''
    plt.scatter(x,y)
    plt.xlabel('overall')
    plt.ylabel('score')
    plt.show()
    '''

    return (slope,intercept)




def linear_planet(p,avgpx):
    #dict = {}
    d2 = {}
    d1 = {}
    d3 = {}


    for ovr in range(20,60,1):
        t = mod_max_score(ovr,avgpx,p)
        d1[ovr] = t[0]      #求出工作人数与总人口的线性关系
        #d2[ovr] = t[1]      #求出实际产销与总人数的线性关系
        d3[ovr] = t[2]      #求出产销与工作人数比值 和 总人数 的线性关系

    t = draw_linear(d1)
    return (t[0],t[1],draw_linear(d3)[1])


def one_cal(p,avgpx):
    planet = copy.deepcopy(p)
    #print(linear_planet(planet,avgpx))
    return linear_planet(planet,avgpx)



def main():

    data = [ [ tuple() for _ in range(105)] for _ in range(105)]


    for yj in range(50,101,5):

        for avgpx in range(20,101,1):

            p = info(yiju=yj)
            ap = avgpx
            data[yj][ap] = one_cal(p,avgpx)


    #print(data)



    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f,indent=2)  # indent美化格式





if __name__ == '__main__':
    main()



































