import pyomo.environ as pyo
from pyomo.core import summation
from stats import planet_stats as ps
import json
from stats import fixed_staff_stats as fs


#总人口原则
def c1_rule(model):
    return summation(model.ovr_workers) + summation(model.ovr_actors) + 3 * 10  <= 300

#单个星球人口限制
def c2_rule(model, i):
    p = ps.planet[i]
    fst = fs.total + fs.dec_doc(p.yiju)

    return sum(model.ovr_workers[i,j] for j in model.k) + model.ovr_actors[i] + fst  <= p.max_building * 2

#电力限制
def c3_rule(model, i):
    return model.ovr_workers[i,0] <= ps.planet[i].max_elec * 2

#矿产限制
def c4_rule(model, i):
    return model.ovr_workers[i,1] <= ps.planet[i].max_oar * 2

#食物限制
def c5_rule(model, i):
    return model.ovr_workers[i,2] <= ps.planet[i].max_food * 2

#优先级总和为1
def c6_rule(model, i):
    return sum(model.ovr_prior[i,j] for j in model.k) == 1



#定死演员个数
def c7_rule(model,i):
    with open('lin/data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    t = sum(model.ovr_workers[i,j] for j in model.k)
    yj = ps.planet[i].yiju
    ap = 50
    fst = fs.total + fs.dec_doc(ps.planet[i].yiju)

    return  t >= (t + fst + model.ovr_actors[i]) * data[yj][ap][0] + data[yj][ap][1] - 0.5


def c8_rule(model,i):
    with open('lin/data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    t = sum(model.ovr_workers[i,j] for j in model.k)
    yj = ps.planet[i].yiju
    ap = 50
    fst = fs.total + fs.dec_doc(ps.planet[i].yiju)

    return  t <= (t + fst + model.ovr_actors[i]) * data[yj][ap][0] + data[yj][ap][1] + 0.5
