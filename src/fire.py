import pyrebase
import os
#string de conexão do firebase
config = {
    
}
PATH_IMAGE = os.path.join(os.getcwd(),'analisar')

class Fire:
    def __init__(self, config=config, caminho=PATH_IMAGE):
        self.firebase = pyrebase.initialize_app(config)
        self.storage = self.firebase.storage()
        self.caminho = caminho

    def download_arq(self, name, date):
        try:
            caminho_image= os.path.join(os.getcwd(), 'src','analisar',name+".jpg" ) 
            self.storage.child(date +"/"+name+".jpg").download(caminho_image)
        except:
            print('Download Failed')
                
        
        return ("Recebido com sucesso")

