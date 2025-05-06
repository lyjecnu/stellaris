import planet as score
import pulp
import numpy as np
import planet_stats as stats
import linear
import efficiency
from math import floor as fl
import ovr_func
import copy


kinds = 7
pop = 340
num_planets = 10
avgpx = 50
elec = 0
oar = 0
food = 0
grocery = 0
metal = 0
ningju = 0
tech = 0

prob = pulp.LpProblem(name='Findhigestscore', sense=pulp.LpMaximize)






def process(planet,vec,eff,actors):
    
    p = copy.deepcopy(planet)
    prior = ovr_func.create_array(vec)
    
    politicians = 2
    doctors = 0
        
    if p.yiju < 100:
        p.yiju = p.yiju + 5
        doctors = doctors + 2
        
    pro = 1 - (100 - p.yiju) / 200
    con = 1 + (100 - p.yiju) / 100
    
    
    elec = elec + vec[0] * eff * p.elec_pro * (1 +  0.25 * prior[0].varValue) * efficiency.elec_pro * pro
    oar = oar + vec[1] * eff * p.oar_pro * (1 +  0.25 * prior[1].varValue) * efficiency.oar_pro * pro
    food = food + vec[2] * eff * p.food_pro * (1 +  0.25 * prior[2].varValue) * efficiency.food_pro * pro
    
    grocery = grocery + vec[3] * eff * p.grocery_pro * pro
    metal = metal + vec[4] * eff * p.metal_pro * pro
    ningju = ningju + vec[5] * eff * p.ningju_pro * (1 + 0.1 * prior[5].varValue) * pro
    tech = tech + vec[6] * eff * p.tech_pro * pro
    
    oar = oar - vec[3] * p.oar_consum * (1 - 0.2 * prior[3].varValue) * efficiency.oar_consum * con
    oar = oar - vec[4] * p.oar_consum * (1 - 0.2 * prior[4].varValue) * efficiency.oar_consum * con
    grocery = grocery - vec[5] * (1 - 0.1 * prior[5].varValue) * p.grocery_consum * efficiency.grocery_consum2 * con
    grocery = grocery - vec[6] * (1 - 0.2 * prior[6].varValue) * p.grocery_consum * efficiency.grocery_consum3 * con
    
    grocery = grocery - actors * 1.0
    grocery = grocery - doctors * 2.0
    grocery = grocery - politicians * 3.0
    
    
    






def main():
    
    linear_info = [] * num_planets
    distribute_pop = [] * num_planets

    for i in range(num_planets):
        linear_info[i] = linear.linear_planet(stats.planet[i],avgpx)


    for i in range(num_planets):
        distribute_pop[i] = pulp.LpVariable(name="planet"+str(i),lowBound=0,upBound=60,cat="LpInteger")
    
    prob += pulp.lpSum([distribute_pop[i] for i in range(num_planets)]) <= pop


    for i in range(num_planets):
        
        p = copy.deepcopy(stats.planet[i])
        
        worker_lin = linear_info[i][0]
        production_lin = linear_info[i][1]
        efficiency_lin = linear_info[i][2]
    
    
        workers = distribute_pop[i] * worker_lin[0] + worker_lin[1]
        production = distribute_pop[i] * production_lin[0] + production_lin[1]
        worker_efficiency = distribute_pop[i] * efficiency_lin[0] + efficiency_lin[1]
        
        vec = [pulp.LpVariable(name=f'x{i}',lowBound=0,upBound=100) for i in range(kinds)]
        prob += (vec[0] <= p.max_elec * 2)
        prob += (vec[1] <= p.max_oar * 2)
        prob += (vec[2] <= p.max_food * 2)
        prob += 
         
        
        process(stats.planet[i],vec,worker_efficiency,distribute_pop[i]-workers)

  


    






