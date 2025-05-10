import pyomo.environ as pyo
import pyomo_version.mod.model_rule as mr
import pyomo_version.mod.cal_process as cp


class Modelling:
    def __init__(self):
        self.model = pyo.ConcreteModel()
        self.num_planets = 10
        self.pop = 280
        self.kinds = 7


    def build_var(self,model):
        model.planet = pyo.Set(initialize=range(0,self.num_planets))    #星球列表
        model.k = pyo.Set(initialize=range(0,self.kinds))


        model.ovr_workers = pyo.Var(model.planet,model.k,within=pyo.NonNegativeIntegers)
        model.ovr_actors = pyo.Var(model.planet,within=pyo.NonNegativeIntegers)
        model.ovr_staff = pyo.Var(model.planet,within=pyo.NonNegativeIntegers)
        model.ovr_prior = pyo.Var(model.planet,model.k,within=pyo.Binary)


    def build_pop_con(self,model):
        model.popc1 = pyo.Constraint(rule=mr.c1_rule)
        model.popc2 = pyo.Constraint(model.planet,rule=mr.c2_rule)
        model.popc3 = pyo.Constraint(model.planet,rule=mr.c3_rule)
        model.popc4 = pyo.Constraint(model.planet, rule=mr.c4_rule)
        model.popc5 = pyo.Constraint(model.planet, rule=mr.c5_rule)
        model.popc6 = pyo.Constraint(model.planet,rule=mr.c6_rule)




    def build_resources_con(self,model):

        cal_mod = cp.cal_process(model.ovr_workers,model.ovr_actors,model.ovr_staff,model.ovr_prior)
        cal_mod.ovr_cal_rule()

        model.resc1 = pyo.Constraint(expr = cal_mod.elec >= 100)
        model.resc2 = pyo.Constraint(expr = cal_mod.oar >= 100)
        model.resc3 = pyo.Constraint(expr = cal_mod.food >= 0)
        model.resc4 = pyo.Constraint(expr = cal_mod.grocery >= 0)
        model.resc5 = pyo.Constraint(expr = cal_mod.metal >= 30)
        model.resc6 = pyo.Constraint(expr = cal_mod.ningju >= 100)
        model.obj1 = pyo.Objective(expr = cal_mod.ningju + cal_mod.tech)





    def build_init(self,model):
        pass



    def main(self):
        self.build_var(self.model)
        self.build_pop_con(self.model)
        self.build_resources_con(self.model)

        solver = pyo.SolverFactory('ipopt')  # 调用非线性求解器IPOPT
        results = solver.solve(self.model)
        print(pyo.value(self.model.ovr_workers))  # 输出解
        print(pyo.value(self.model.ovr_actors))
        print(pyo.value(self.model.ovr_staff))
        print(pyo.value(self.model.ovr_prior))




        











