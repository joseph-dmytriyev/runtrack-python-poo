class Part:
    def __init__(self,name,material):
        self.name = name
        self.material = material
    def change_material(self,new_material):
        self.material = new_material
        
    def __str__(self):
        return f"part: {self.name}, material: {self.material}"
    
class ship:
    def __init__(self,name):
        self.name = name
        self.__parts = {}
    
    def  add_part(self,part):
        self.__parts[part.name] = part
    
    def display_state(self):
        for part_name,part in self.__parts.items():
            print(part)
            
    def replace_part(self,part_name,new_part):
        if part_name in self.__parts:
            self.__parts[part_name] = new_part
        else:
            print(f"Part {part_name} n'est pas sur le bateau")
    
    def change_part(self,part_name,new_material):
        if part_name in self.__parts:
            self.__parts[part_name].change_material(new_material)
        else:
            print("Part {part_name} pas trouvé")
    
    def __str__(self):
        return f"Bateau: {self.name}"
    
    
    
    