import numpy as np
from stats.planet_class import info
import copy
from stats import fixed_staff_stats as fs




'''
#干活的人，演绎人员，商业区，警署,医院
'''


'''
def generate_distributions(n,m):
    combinations = []
    
    def dfs(remaining, path, depth):
        if depth == m-1:  # 到达第五个盒子时，将剩余球数分配
            combo = path.copy()
            combo.append(remaining)
            combinations.append(combo)
            return
        for i in range(remaining + 1):
            dfs(remaining - i, path + [i], depth + 1)
    
    dfs(n, [], 0)
    return combinations


def c2h(pro,real):
    if real > 0:
        a = int(20 * real / (pro - real))
        return min(20,a)
    else:
        a = int(200 * real / (pro-real) / 3)
        return max(-50,a)


def fixed_staff(p):

    planet = copy.deepcopy(p)

    robots = fs.robots
    doctors = 0
    politician = fs.politician
    police = fs.police

    
    if planet.yiju < 100:
        planet.yiju = planet.yiju + 5
        doctors += 2
    

    return [robots,doctors,politician,police]




def raw_score(combo,avgpx):
    #干活的人，演绎人员，商业区，警署,
    
        
    provided_comfort = 7 + combo[1] * 10 + combo[2] * 4
    comfort_each = 0.92
    comfort = provided_comfort - comfort_each * n - 5
    rt = avgpx + c2h(provided_comfort,comfort)
    stable = 50
    
    
    if rt > 50:
        stable = 50 + (rt-50) * 0.6 + combo[3]
    else:
        stable = 50 - (50-rt) + combo[3]
        
    addition = 0
    if stable > 50:
        addition = (stable - 50) / 2
    else:
        addition = stable - 50
        
    if combo[3] * 25 < (2*(1-rt/100)) * n:
        return -1000    
        

    trade = 4 * combo[2] * (1 + addition / 100)
    
    
    print("stable: %f" % (stable))
    print("rentong: %f" %(rt))
    print("comfort: %f" %(comfort))
    print("provided_comfort: %f" %(provided_comfort))
    
    return combo[0] * (1 + addition/100)  + trade / 10
'''



def c2h(pro,real):
    if real > 0:
        a = int(20 * real / (pro - real))
        return min(20,a)
    else:
        a = int(200 * real / (pro-real) / 3)
        return max(-50,a)
 
 
def mod_score_actor(worker,actor,avgpx,p):     #求出指定工作人数与演员，产生的等效工作人口
    
    #干活的人，演绎人员
    
    planet = copy.deepcopy(p)


    robots = fs.robots
    doctors = fs.dec_doc(p.yiju)
    politician = fs.politician
    police = fs.police

    n = worker + actor + robots + doctors + politician + police
    
       
    provided_comfort = (5 + 3 * politician + actor * 10 + doctors * 5 + planet.comfort_change) * planet.comfort_pro
    comfort_each = 1 * planet.comfort_consum * (1+(1-planet.yiju/100))
    comfort = provided_comfort - comfort_each * n - 5
        
    rt = (avgpx + c2h(provided_comfort,comfort) + planet.rt_change) * planet.rt_property
    
    
    stable = 50
    if rt > 50:
        stable = 50 + (rt-50) * 0.6 + planet.stable + police
    else:
        stable = 50 - (50-rt) + planet.stable + police
        
    addition = 0
    if stable > 50:
        addition = (stable - 50) / 200
    else:
        addition = (stable - 50) / 100
        
    
    score = 0
    addition = addition * (1 - (100 - planet.yiju)/200)
    score = worker * (1+addition)
    #+ (1 * actor * (1+addition)) / 4 - 0.25 * actor
    #score = score * 100 / n
    

    return score
    
    
def mod_max_score(ovr,avgpx,p):   #给每个星球分配一定的人口，求出最高效率的工人数

    planet = copy.deepcopy(p)
    max_score = 0
    perfect_worker = 0
    efficiency = 0
    
    for worker in range(ovr - fs.total - fs.dec_doc(planet)+1):     #总人口不变，求出最高等效工作人口的情况

        t = mod_score_actor(worker, ovr - worker - fs.total - fs.dec_doc(planet), avgpx, planet)
        if t > max_score:
            max_score = t
            perfect_worker = worker
            
            if perfect_worker > 0:
                efficiency = max_score / perfect_worker



    return (perfect_worker,max_score,efficiency)   #最佳工人数，在这种情况下的最佳产能
    
    
    

def main():
    p = info(yiju=100)
    avgpx = 50

    dict = {}


    for ovr in range(10,50):
        t = mod_max_score(ovr,avgpx,p)
        dict[str(ovr)] = t[0]
    
    print(dict)  




if __name__ == '__main__':
    main()
    
    


'''
n = int(input())
m = 4
distributions = generate_distributions(n,m)
largest = -10000
res = []


px = [0,143,0,0,107,80,0,0,0,0,0]
avgpx = 0
for i in range(0,11):
    avgpx = avgpx + px[i] * i * 10
        
           
avgpx = avgpx / sum(px) + 7

print(avgpx)
'''


'''
for dist in distributions:

    if raw_score(dist,avgpx) > largest:
        res = dist
        largest = raw_score(dist,avgpx)



print(res)
print(largest)
'''
    

