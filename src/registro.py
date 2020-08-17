from pymongo import MongoClient
#String de conexão do banco de dados mongo
PATH_DEFAULT = " "

class Registro:
    def __init__(self, url = PATH_DEFAULT):
        self.server = MongoClient(url)
        self.db = self.server.Fatec


    def buscar(self, data="20/07/2020", hoursFinal=12, minutsFinal=20, hoursInicio=6, minutsInicio=10):
        lista=[]
        horarioInicio= str(hoursInicio)+'.'+str(minutsInicio)
        horarioFinal = str(hoursFinal) + '.' + str(minutsFinal)
        encontrados = self.db.registros.find({
            "date":data

        })
        for encontro in encontrados:
            convertendo = str(encontro['horas']) +'.'+str(encontro['minutos'])
            if float(horarioInicio) >= float(convertendo) or float(convertendo) <= float(horarioFinal):
               lista.append(encontro['codigo_user'])

            else:
                continue

        return lista
    #função para guarda todos os valores no banco de dados mongo
    def insertRegistro(self,cod,nome,hour,minu,sec,date,latitude,longitude):
        self.db.registros.insert_one({
            'codigo_user':cod,
            'nome':nome,
            'hour':hour,
            'min':minu,
            'sec':sec,
            'date':date,
            'latitude':latitude,
            'longitude':longitude
        })


print(Registro().buscar())