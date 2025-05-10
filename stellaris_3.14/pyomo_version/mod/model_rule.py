import pyomo.environ as pyo
from pyomo.core import summation
from pyomo_version.stats import planet_stats as ps




def c1_rule(model):
    return summation(model.ovr_workers) + summation(model.ovr_actors) + summation(model.ovr_staff) <= 280

def c2_rule(model, i):
    return sum(model.ovr_workers[i,j] for j in model.k) + model.ovr_actors[i] + model.ovr_staff[i] <= ps.planet[i].max_building * 2

def c3_rule(model, i):
    return model.ovr_workers[i,0] <= ps.planet[i].max_elec * 2

def c4_rule(model, i):
    return model.ovr_workers[i,1] <= ps.planet[i].max_oar * 2

def c5_rule(model, i):
    return model.ovr_workers[i,2] <= ps.planet[i].max_food * 2

def c6_rule(model, i):
    return sum(model.ovr_prior[i,j] for j in model.k) == 1