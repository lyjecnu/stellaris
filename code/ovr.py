import planet as score
import pulp
import numpy as np
import planet_stats as stats
import linear
from math import floor as fl



pop = 340
num_planets = 10
avgpx = 50

prob = pulp.LpProblem(name='Findhigestscore', sense=pulp.LpMaximize)
linear_info = [] * num_planets


for i in range(num_planets):
    linear_info[i] = linear.linear_planet(stats.planet[i],avgpx)
    
    


worker = np.zeros((num_planets,7))
for i in range(num_planets):
    worker[i][0] = pulp.LpVariable(lower_bound=0,upper_bound=stats.planet[i].max_elec * 2,cat='Integer') #电
    worker[i][1] = pulp.LpVariable(lower_bound=0,upper_bound=stats.planet[i].max_oar * 2,cat='Integer')  #矿
    worker[i][2] = pulp.LpVariable(lower_bound=0,upper_bound=stats.planet[i].food * 2,cat='Integer')     #食物
    worker[i][3] = pulp.LpVariable(lower_bound=0,upper_bound=stats.planet[i].max_building * 2,cat='Integer')  #消费品
    worker[i][4] = pulp.LpVariable(lower_bound=0,upper_bound=stats.planet[i].max_building * 2,cat='Integer')  #合金
    worker[i][5] = pulp.LpVariable(lower_bound=0,upper_bound=stats.planet[i].max_building * 2,cat='Integer')  #凝聚力
    worker[i][6] = pulp.LpVariable(lower_bound=0,upper_bound=stats.planet[i].max_building * 2,cat='Integer')  #科技
    

for i in range(num_planets):
    
    t = worker[i]
    p = stats.planet[i]
    
    actors = int(pulp.lpSum(t) * linear_info[i][1][0] + linear_info[i][1][1] - pulp.lpSum(t) + 0.5)
    quhua = (pulp.lpSum(t[:3]) + 1) // 2
    building = fl(t[3]/p.grocery_per_building) + fl(t[4]/p.metal_per_building) + fl(t[5]/p.officer_per_building) + fl(t[6]/p.tech_per_building)
    building = building + fl(actors/p.actor_per_building)
    building = building + (p.yiju < 100) + 1
    
    prob =+ building <= 12
    prob =+ building - 2 + quhua <= p.max_building
  







