class Item_Proc(object):
    """description of class"""
    on_use:bool
    #timer_lower
    #timer_upper
    timer:int = None
    proc_action:dict
    proc_stat:str 
    proc_uptime:int # seconds or number of times it hits
    def __init__(self):
        if self.on_use == True:
            self.timer
            self.timer_lower = self.timer
            self.timer_upper = self.timer
        else:
            self.timer_lower 
            self.timer_upper


