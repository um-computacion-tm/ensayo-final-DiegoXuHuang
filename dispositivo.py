class Dispositivo:
    def __init__(self,_id=None,nombre=None,marca=None,tipo=None,dispositivo=None,diccionario=None):
        if dispositivo:
            self.id = dispositivo.get("id")
            self.nombre = dispositivo.get("nombre") 
            self.marca = dispositivo.get("marca") 
            self.tipo = dispositivo.get("tipo") 
        elif diccionario:
            self.id = diccionario.get("id")
            self.nombre = diccionario.get("nombre") 
            self.marca = diccionario.get("marca") 
            self.tipo = diccionario.get("tipo") 
        else:
            self.id = _id
            self.nombre = nombre
            self.marca = marca
            self.tipo = tipo
            