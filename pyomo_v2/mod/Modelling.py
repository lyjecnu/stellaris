import pyomo.environ as pyo
from pulp import initialize
from pyomo.common.enums import maximize

import mod.model_rule as mr
import mod.cal_process as cp
import json



class Modelling:
    def __init__(self):
        self.model = pyo.ConcreteModel()
        self.num_planets = 10
        self.pop = 300
        self.kinds = 7
        with open('lin/data.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)



    def build_var(self,model):
        model.planet = pyo.Set(initialize=range(0,self.num_planets))    #星球列表
        model.k = pyo.Set(initialize=range(0,self.kinds))


        model.ovr_workers = pyo.Var(model.planet,model.k,within=pyo.NonNegativeIntegers,initialize=3)
        model.ovr_actors = pyo.Var(model.planet,within=pyo.NonNegativeIntegers,initialize=4)
        model.ovr_prior = pyo.Var(model.planet,model.k,within=pyo.Binary)


    def build_pop_con(self,model):
        model.popc1 = pyo.Constraint(rule=mr.c1_rule)
        model.popc2 = pyo.Constraint(model.planet,rule=mr.c2_rule)
        model.popc3 = pyo.Constraint(model.planet,rule=mr.c3_rule)
        model.popc4 = pyo.Constraint(model.planet, rule=mr.c4_rule)
        model.popc5 = pyo.Constraint(model.planet, rule=mr.c5_rule)
        model.popc6 = pyo.Constraint(model.planet,rule=mr.c6_rule)
        model.popc7 = pyo.Constraint(model.planet, rule=mr.c7_rule)
        model.popc8 = pyo.Constraint(model.planet, rule=mr.c8_rule)




    def build_resources_con(self,model):

        cal_mod = cp.cal_process(model.ovr_workers,model.ovr_actors,model.ovr_prior)
        cal_mod.ovr_cal_rule()

        model.resc1 = pyo.Constraint(expr = cal_mod.elec >= 100)
        model.resc2 = pyo.Constraint(expr = cal_mod.oar >= 100)
        model.resc3 = pyo.Constraint(expr = cal_mod.food >= 0)
        model.resc4 = pyo.Constraint(expr = cal_mod.grocery >= 0)
        model.resc5 = pyo.Constraint(expr = cal_mod.metal >= 30)
        model.resc6 = pyo.Constraint(expr = cal_mod.ningju >= 100)
        model.obj1 = pyo.Objective(expr = cal_mod.ningju + cal_mod.tech,sense = maximize)





    def build_init(self,model):
        pass



    def main(self):
        self.build_var(self.model)
        self.build_pop_con(self.model)
        self.build_resources_con(self.model)

        solver = pyo.SolverFactory('ipopt',executable='C:\\Ipopt-3.14.17-win64-msvs2022-md\\bin\\ipopt.exe')  # 调用非线性求解器IPOPT
        solver.options['print_level'] = 5
        results = solver.solve(self.model)

        '''
        print(pyo.value(self.model.ovr_workers))  # 输出解
        print(pyo.value(self.model.ovr_actors))
        print(pyo.value(self.model.ovr_prior))
        '''

        '''
        res = cp.cal_process(self.model.ovr_workers,self.model.ovr_actors,self.model.ovr_prior)
        res.ovr_cal_rule()
        print(res.tech)
        print(res.ningju)
        '''



        











