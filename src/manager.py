import os
import firebase_admin
from firebase_admin import credentials,db
from src.fire import Fire

PATH_IMAGE = os.path.join(os.getcwd(), 'src','analisar')
#credenciais do firebase .json
PATH_CRED = os.path.join(os.getcwd(), 'src'," ")


class Manager:  
    def __init__(self,data):
        self.cred=credentials.Certificate(PATH_CRED)
        #string do banco de dados do firebase
        self.firebase = firebase_admin.initialize_app(self.cred,{
    'databaseURL':" ",
    'databaseAuthVariableOverride': None,
     })
        self.data = str(data)
        self.lista = []
    #realiza o dowload das imagens referentes a data inserida
    def download(self):
        ref = db.reference('users').child(self.data).get()
        for key, val in ref.items():
            user = db.reference('users').child(self.data).child(key).get()
            Fire().download_arq(user['nome'],self.data)
            self.lista.append(str(key))
        return (self.lista)
        
    #busca os usuario cadastrados
    def dados(self, key, ra, nome):
        ref = db.reference('users').child(self.data).child(key).get()
        data = db.reference('registro')
        users_ref = data.child(self.data)
        id = str(ra)+key
        dados={
                'ra':str(ra),
                'nome':str(nome),
                'date':self.data,
                'hour':int(ref['hour']),
                'min':int(ref['min']),
                'sec':int(ref['sec']),
                'latitude':float(ref['latitude']),
                'longitude':float(ref['longitude'])
            }
        return dados