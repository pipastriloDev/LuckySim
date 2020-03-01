class Character(object):
    """description of class"""
    import Game_Class
    import Game_Race
    import Slot
    import requests
    import WoW_Requests
    #game_class:Game_Class # TODO: Custom Game_Class class 
    game_level:int #TODO: force int to be between range 1-120
    #game_race #TODO:Custom Race abstract Class
    game_item_sets:list
    
    def __init__(self, client_id, client_secret, realm, character_name, region = "eu"):
        #TODO remove hard coded client_id and secret
        self.gear:dict= {}
        self.spell_list:list = []
        self.wow_requests = self.WoW_Requests.WoW_Requests(region, client_id, client_secret)
        self.get_character_profile(realm, character_name)
        self.game_class = self.Game_Class.Game_Class(self.class_id)
        test = self.get_talent_profile(realm, character_name)
        self.stats ={}
        #self.gear = self.get_current_gear(realm, character_name)
        self.get_stats(region, realm,character_name)
    def get_item_set():
        #TODO: Get /data/wow/item-set{itemSetId}
        pass

    def get_character_profile(self, realm:str, char_name:str, locals = "en_US"):
        import json
        ##/wow/character/:realm/:characterName
        ##'{"lastModified":1582829990000,"name":"Pipasstd","realm":"Twisting Nether","battlegroup":"Sturmangriff / Charge","class":9,"race":8,"gender":0,"level":120,"achievementPoints":17090,"thumbnail":"twisting-nether/195/144827587-avatar.jpg","calcClass":"V","faction":1,"totalHonorableKills":2982,"id":144827587}'
        realm = realm.strip()
        realm = realm.replace(" ", "-") # realm name replaces space with -
        suffix = f"/wow/character/{realm}/{char_name}?locale={locals}"
        data = self.wow_requests.request_data(suffix)
        self.class_id = json.loads(data.text)["class"]
        self.char_race = json.loads(data.text)["race"]
        self.char_level = json.loads(data.text)["level"]
        class_dict = {1:"Warrior",
                      2:"Paladin",
                      3:"Hunter",
                      4:"Rogue",
                      5:"Priest",
                      6:"Death Knight",
                      7:"Shaman",
                      8:"Mage",
                      9:"Warlock",
                      10:"Monk",
                      11:"Druid",
                      12:"Demon Hunter"
                      }
        race_dict = {0:"Unknown",
                      1:"Unknown",
                      2:"Unknown",
                      3:"Unknown",
                      4:"Unknown",
                      5:"Unknown",
                      6:"Tauren",
                      7:"Unknown",
                      8:"Troll",
                      9:"Goblin",
                      10:"Blood Elf"
                      }
    def get_talent_profile(self, realm:str, char_name:str, locals = "en_US"):
        import json
        #https://eu.api.blizzard.com/wow/character/twisting%20nether/pipasstd?fields=talents&locale=en_US&access_token=USRBfL0w3xx8OxU8u7gIwc3iLD7yAAtz13
        #'https://eu.api.blizzard.com/wow/character/twisting-nether/pipasstd/fields=talents&en_US&access_token=EU7lmDJrVK2syebJZk6RF4HzlIhJN47399'
        realm = realm.strip()
        realm = realm.replace(" ", "%20") # realm name replaces space with -
        suffix= f"/wow/character/{realm}/{char_name}?fields=talents&{locals}"
        data = self.wow_requests.request_data(suffix)
        json_data = json.loads(data.text)
        current_spec = ""
        talents_json_data = json_data["talents"]
        for entry in talents_json_data : 
            if entry["selected"] == True:
                spec_data = entry['spec']
                current_spec = spec_data["name"]
                talents_data = entry["talents"]
                for item in talents_data:
                    spell_data = item["spell"]
                    self.spell_list.append((spell_data["id"], spell_data["name"]))
                break
    def get_current_gear(self,  realm:str, char_name:str, locals = "en_US"):
        #/wow/character/twisting%20nether/pipasstd?fields=items&locale=en_US
        import json
        realm = realm.strip()
        realm = realm.replace(" ", "%20")
        suffix = f"/wow/character/{realm}/{char_name}?fields=items&locale={locals}"
        data = self.wow_requests.request_data(suffix)
        json_data = json.loads(data.text)
        items_data=json_data["items"]
        
        item = {"id":items_data["head"]["id"],
                "name":items_data["head"]["name"], 
                "ilvl": items_data["head"]["itemLevel"], 
                "stats": items_data["head"]["stats"], 
                }
        self.gear["head"] = item
        item = {"id":items_data["neck"]["id"],
                "name":items_data["neck"]["name"], 
        	    "ilvl": items_data["neck"]["itemLevel"], 
        	    "stats": items_data["neck"]["stats"], 
        	    }
        self.gear["neck"] = item

        item = {"id":items_data["shoulder"]["id"],
        	    "name":items_data["shoulder"]["name"], 
        	    "ilvl": items_data["shoulder"]["itemLevel"], 
        	    "stats": items_data["shoulder"]["stats"], 
        	}
        self.gear["shoulder"] = item

        item = {"id":items_data["back"]["id"],
            	"name":items_data["back"]["name"], 
            	"ilvl": items_data["back"]["itemLevel"], 
            	"stats": items_data["back"]["stats"], 
        	}
        self.gear["back"] = item

        item = {"id":items_data["chest"]["id"],
        	    "name":items_data["chest"]["name"], 
        	    "ilvl": items_data["chest"]["itemLevel"], 
        	    "stats": items_data["chest"]["stats"], 
        	}
        self.gear["chest"] = item
        
        item = {"id":items_data["wrist"]["id"],
        	    "name":items_data["wrist"]["name"], 
        	    "ilvl": items_data["wrist"]["itemLevel"], 
        	    "stats": items_data["wrist"]["stats"], 
        	}
        self.gear["wrist"] = item

        item = {"id":items_data["hands"]["id"],
        	    "name":items_data["hands"]["name"], 
        	    "ilvl": items_data["hands"]["itemLevel"], 
        	    "stats": items_data["hands"]["stats"], 
        	}
        self.gear["hands"] = item
        
        item = {"id":items_data["waist"]["id"],
        	    "name":items_data["waist"]["name"], 
        	    "ilvl": items_data["waist"]["itemLevel"], 
        	    "stats": items_data["waist"]["stats"], 
        	}
        self.gear["waist"] = item
        item = {"id":items_data["legs"]["id"],
        	    "name":items_data["legs"]["name"], 
        	    "ilvl": items_data["legs"]["itemLevel"], 
        	    "stats": items_data["legs"]["stats"], 
        	}
        self.gear["legs"] = item
        item = {"id":items_data["feet"]["id"],
        	    "name":items_data["feet"]["name"], 
        	    "ilvl": items_data["feet"]["itemLevel"], 
        	    "stats": items_data["feet"]["stats"], 
        	}
        self.gear["feet"] = item
        item = {"id":items_data["finger1"]["id"],
        	    "name":items_data["finger1"]["name"], 
        	    "ilvl": items_data["finger1"]["itemLevel"], 
        	    "stats": items_data["finger1"]["stats"], 
        	}
        self.gear["finger1"] = item
        item = {"id":items_data["finger2"]["id"],
        	    "name":items_data["finger2"]["name"], 
        	    "ilvl": items_data["finger2"]["itemLevel"], 
        	    "stats": items_data["finger2"]["stats"], 
        	}
        self.gear["finger2"] = item
        item = {"id":items_data["trinket1"]["id"],
        	    "name":items_data["trinket1"]["name"], 
        	    "ilvl": items_data["trinket1"]["itemLevel"], 
        	    "stats": items_data["trinket1"]["stats"], 
        	}
        self.gear["trinket1"] = item
        item = {"id":items_data["trinket2"]["id"],
        	    "name":items_data["trinket2"]["name"], 
        	    "ilvl": items_data["trinket2"]["itemLevel"], 
        	    "stats": items_data["trinket2"]["stats"], 
        	}
        item = {"id":items_data["mainHand"]["id"],
        	    "name":items_data["mainHand"]["name"], 
        	    "ilvl": items_data["mainHand"]["itemLevel"], 
        	    "stats": items_data["mainHand"]["stats"],
                "weaponInfo": items_data["mainHand"]["weaponInfo"],
                "weaponSpeed": items_data["mainHand"]["weaponSpeed"]
        	}
        self.gear["mainHand"] = item
        item = {"id":items_data["offHand"]["id"],
        	    "name":items_data["offHand"]["name"], 
        	    "ilvl": items_data["offHand"]["itemLevel"], 
        	    "stats": items_data["offHand"]["stats"], 
        	}
        self.gear["offHand"] = item

        print("")


    def get_item(self, data, slot:str):
        item = {"id":data[slot]["id"],
                "name":data[slot]["name"],
                "ilvl": data[slot]["itemLevel"],
                "armor": data[slot]["armor"],
                "stats":data[slot]["stats"] #TODO expand out stats to specific stats
                }

        if slot == "mainHand" or slot == "offHand":
            pass #todo 
        if slot == "finger1" or slot == "finger2":
            item["enchant"] = data[slot]["enchant"]#todo

    def get_stats(self, region:str, realm:str, char_name:str, locals = "en_US"):
        #https://eu.api.blizzard.com/profile/wow/character/twisting-nether/pipasstd/statistics?namespace=profile-eu&locale=en_US&access_token=US3RPuYtT3Fm5muNVF8QYGDiUzJKlLSCRl
        import json
        realm = realm.strip()
        realm = realm.replace(" ", "-")
        namespace = f"profile-{region}"
        suffix = f"/profile/wow/character/{realm}/{char_name}/statistics?namespace={namespace}&locale={locals}"
        data = self.wow_requests.request_data(suffix)
        json_data = json.loads(data.text)
        self.stats["speed"] = json_data["speed"]["rating"]
        self.stats["strength"] = json_data["strength"]["effective"]
        self.stats["agility"] = json_data["agility"]["effective"]
        self.stats["intellect"] = json_data["intellect"]["effective"]
        self.stats["stamina"] = json_data["stamina"]["effective"]
        self.stats["melee_crit"] = json_data["melee_crit"]["value"]
        self.stats["melee_haste"] = json_data["melee_haste"]["value"]
        self.stats["mastery"] = json_data["mastery"]["value"]
        self.stats["bonus_armor"] = json_data["bonus_armor"]
        self.stats["leech"] = json_data["lifesteal"]["value"]
        self.stats["versatility"] = json_data["versatility"]
        self.stats["attack_power"] = json_data["attack_power"]
        self.stats["main_hand_damage"] = (json_data["main_hand_damage_min"], json_data["main_hand_damage_max"])
        self.stats["main_hand_speed"] = json_data["main_hand_speed"]
        self.stats["main_hand_damage"] = (json_data["main_hand_damage_min"], json_data["main_hand_damage_max"])
        self.stats["main_hand_speed"] = json_data["main_hand_speed"]
        self.stats["off_hand_damage"] = (json_data["off_hand_damage_min"], json_data["main_hand_damage_max"])
        self.stats["off_hand_speed"] = json_data["off_hand_speed"]
        self.stats["spell_power"] = json_data["spell_power"]
        self.stats["spell_penetration"] = json_data["spell_penetration"]
        self.stats["spell_crit"] =json_data["spell_crit"]["value"]
        self.stats["mana_regen"] = (json_data["mana_regen"], json_data["mana_regen_combat"])
        self.stats["armor "] = json_data["armor"]["effective"]
        self.stats["dodge"] = json_data["dodge"]["value"]
        self.stats["parry"] = json_data["parry"]["value"]
        self.stats["block"] = json_data["block"]["value"]
        self.stats["ranged_crit"]= json_data["ranged_crit"]["value"]
        self.stats["ranged_haste"] = json_data["ranged_haste"]["value"]
        self.stats["spell_haste"] = json_data["spell_haste"]["value"]
        print(")")


