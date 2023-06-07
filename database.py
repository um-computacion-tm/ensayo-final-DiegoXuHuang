from dispositivo import Dispositivo

class Database:
    def __init__(self,lista_dispositivos):
        self.database = []
        for dispositivo  in lista_dispositivos.get("dispositivos"):
            self.database.append(Dispositivo(dispositivo=dispositivo))
        
    
    def add_dispositivo(self,dispositivo=None,diccionario=None):
        if dispositivo:
            self.database.append(dispositivo)
        else:
            self.database.append(Dispositivo(diccionario=diccionario))
    
    def delete_by_id(self,id=None):
        database = self.database.copy()
        for index in range(len(self.database)):
            dispositivo = self.database[index]
            if dispositivo.id == id:
                database.pop(index)
                break
        self.database = database