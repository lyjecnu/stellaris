class info:   #1制度
    
    def __init__(self,**kwargs):
    
        self.ovr_consum = 1
        self.ovr_pro = 1
        self.labour_pro = 1
        self.expert_pro = 1
    
        self.capital = 0
        self.max_building = 20
        self.max_elec = 3
        self.max_oar = 4
        self.max_food = 5
   
    
        self.elec_pro = 1
        self.oar_pro = 1
        self.food_pro = 1
        self.grocery_pro = 1
        self.metal_pro = 1
        self.ningju_pro = 1
        self.tech_pro = 1
    
        self.elec_consum = 1
        self.oar_consum = 1
        self.food_consum = 1
        self.grocery_consum = 1
        self.metal_consum = 1
    
        self.comfort_pro = 1
        self.comfort_consum = 1
        self.comfort_change = 0
        
        
        self.rt_change = 0        #变化量
        self.rt_property = 1
        
        self.stable = 0    #变化量
        self.yiju = 100
        self.fanzui = 0    #变化量
        
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    
#对于每一个物质，给每一个星球进行优先性排序



    
    
    
