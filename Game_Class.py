class Game_Class(object):
    """description of class"""
    #TODO: Each Class will have a base spell_list and each spec will have spec_spell_list, the get_spell_list() function will return a joint list of spec and base spell lists
    #TODO add a set spec 
    import WoW_Requests
    class_name:str
    class_id:int
    class_specs:list
    current_spec:tuple = (1,2,3)
    #spec_primary_stat #TODO:type stat
    current_talent:list
    custom_talets:list
    specalisations:dict = {}
    spell_list:list
    def __init__(self, char_class):
        class_dict = {1: self.warrior_init,
                      2: self.paladin_init,
                      3: self.hunter_init,
                      4: self.rogue_init,
                      5: self.priest_init,
                      6: self.death_knight_init,
                      7: self.shaman_init,
                      8: self.mage_init,
                      9: self.warlock_init,
                      10: self.monk_init,
                      11: self.druid_init,
                      12: self.demon_hunter_init
                      }
        class_dict[char_class]()

    def death_knight_init(self):
        self.primary_stat = "Strength"
        self.specalisations[1] = "Unholy"
        self.specalisations[2] = "Frost"
        self.specalisations[3] = "Blood"
    def demon_hunter_init(self):
        self.primary_stat = "Agility"
        self.specalisations[1] = "Havoc"
        self.specalisations[2] = "Vengence"
    def druid_init(self):
        self.specalisations[1] = "Balance"
        self.specalisations[2] = "Feral"
        self.specalisations[3] = "Guardian"
        self.specalisations[4] = "Resto"
        self.primary_stat = "rollercoaster" #TODO
    def hunter_init(self):
        self.specalisations[1] = "Beast Mastery"
        self.specalisations[2] = "Marksmanship"
        self.specalisations[3] = "Survival"
        self.primary_stat = "Agiliy"
    def mage_init(self):
        self.specalisations[1] = "Arcane"
        self.specalisations[2] = "Frost"
        self.specalisations[3] = "Fire"
        self.primary_stat = "Intellect"
    def monk_init(self): 
        self.specalisations[1] = "Mistweaver"
        self.specalisations[2] = "Windwalker"
        self.specalisations[3] = "Brewmaster"
        self.primary_stat = "rollercoaster"#TODO
    def paladin_init(self):
        self.specalisations[1] = "Holy"
        self.specalisations[2] = "Protection"
        self.specalisations[3] = "Retrebution"
        self.primary_stat = "rollercoaster"#TODO
    def priest_init(self):
        self.specalisations[1] = "Holy"
        self.specalisations[2] = "Discapiline"
        self.specalisations[3] = "Shadow"
        self.primary_stat = "Intellect"
    def rogue_init(self):
        self.specalisations[1] = "Assassination"
        self.specalisations[2] = "Outlaw"
        self.specalisations[3] = "Subtilty"
        self.primary_stat = "Agility"
    def shaman_init(self):
        self.specalisations[1] = "Restoration"
        self.specalisations[2] = "Elemental"
        self.specalisations[3] = "Enhancement" 
        self.primary_stat = "rollercoaster"#TODO
    def warlock_init(self):
        #self.specalisations["Affliction"] 
        #self.specalisations["Demonology"]
        #self.specalisations["Destruction"]
        self.primary_stat = "Intellect"

    def warrior_init(self):
        self.specalisations[1] = "Arms"
        self.specalisations[2] = "Fury"
        self.specalisations[3] = "Protection"
        self.primary_stat = "Strength"


    def get_talent_setup(self, data):
        
        #wow_request.WoW_Requests.
        #return talent_set:list
        pass
    def save_custom_talent():
        #TODO: Save custom setup
        #return talent_set:list
        pass
