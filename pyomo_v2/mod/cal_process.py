from pyomo.environ import *
import copy
import stats.fixed_staff_stats as fs
import stats.efficiency as ef
import stats.planet_stats as ps
import json



class cal_process:

    def __init__(self,ovr_workers,ovr_actors,ovr_prior):
        self.kinds = 7
        self.num_planets = 10
        self.avgpx = 50

        with open('lin/data.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)

        self.elec = 0
        self.oar = 0
        self.food = 0
        self.grocery = 0
        self.metal = 0
        self.ningju = 0
        self.tech = 0

        self.workers = ovr_workers  #二维数组
        self.actors = ovr_actors    #一维数组
        self.prior = ovr_prior      #二维数组


    '''
    def c2h(self,pro,real):
        if real > 0:
            a = 20 * real / (pro - real)
            return min(20,a)
        else:
            a = 200 * real / (pro - real)
            return max(-50,a)
    '''





    ''''
    def stability(self,planet,num_workers,actors,staff):
        p = copy.deepcopy(planet)

        robots = fs.robots
        doctors = 0
        politicians = fs.politician
        police = 1

        if p.yiju < 100:
            doctors = doctors + 2
            p.yiju = p.yiju + doctors * 2.5

        n = num_workers + actors + robots + doctors + politicians + police

        provided_comfort = (5 + politicians * 3 + actors * 10 + doctors * 5 + p.comfort_change) * p.comfort_pro
        comfort_each = 1 * p.comfort_consum * (1 + (1 - p.yiju / 100))
        comfort = provided_comfort - comfort_each * n - 5

        rt = (self.avgpx + self.c2h(provided_comfort, comfort) + p.rt_change) * p.rt_property

        stable = 50
        if rt > 50:
            stable = 50 + (rt - 50) * 0.6 + p.stable + police
        else:
            stable = 50 - (50 - rt) + p.stable + police

        return stable
    '''




    def one_planet_cal_rules(self,planet,vec,actors,prior):

        with open('lin/data.json','r',encoding='utf-8') as f:
            data = json.load(f)

        p = copy.deepcopy(planet)

        robots = fs.robots
        doctors = fs.dec_doc(p.yiju)
        politicians = fs.politician
        police = fs.police


        pro = 1 - (100 - p.yiju) / 200
        con = 1 + (100 - p.yiju) / 100

        eff = self.data[p.yiju][self.avgpx][2]


        self.elec += vec[0] * eff * (1 + 0.25 * prior[0]) * pro * ef.elec_pro * p.elec_pro
        self.oar += vec[1] * eff * (1 + 0.25 * prior[1]) * pro * ef.oar_pro * p.oar_pro
        self.food += vec[2] * eff  * (1 + 0.25 * prior[2]) * pro * ef.food_pro * p.food_pro

        self.grocery += vec[3] * eff * pro * p.grocery_pro
        self.metal += vec[4] * eff * p.metal_pro * pro
        self.ningju += vec[5] * eff * (1 + 0.1 * prior[5]) * pro * p.ningju_pro
        self.tech += vec[6] * eff * pro * p.tech_pro

        self.oar -= vec[3] * (1 - 0.2 * prior[3]) * con * ef.oar_consum * p.oar_consum
        self.oar -= vec[4]  * (1 - 0.2 * prior[4]) * con * ef.oar_consum * p.oar_consum
        self.grocery -= vec[5] * (1 - 0.1 * prior[5]) * ef.grocery_consum2 * con * p.grocery_consum
        self.grocery -= vec[6] * (1 - 0.2 * prior[6]) * ef.grocery_consum3 * con * p.grocery_consum

        self.grocery -= actors * 1.0
        self.grocery -= doctors * 2.0
        self.grocery -= politicians * 3.0
        self.ningju += actors * 1.0
        self.metal -= robots * 5.0


    def ovr_cal_rule(self):

        for i in range(self.num_planets):

            w = []
            for j in range(self.kinds):
                w.append(self.workers[i,j])

            pr = []
            for j in range(self.kinds):
                pr.append(self.prior[i,j])


            self.one_planet_cal_rules(ps.planet[i],w,self.actors[i],pr)

    