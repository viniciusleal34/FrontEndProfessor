import PySimpleGUI as sg
from src.manager import Manager
from src.reconhecimento import Reconhecimento
from src.registro import Registro
import time
import xlwt
import os
from chamada_view import ChamadaView

class TelaPython:
    def __init__(self):
        #Gerando a telinha para o Usuario
        layout = [
            [sg.Text('Dia', size=(15, 1)), sg.InputText()],
            [sg.Text('EXEMPLO INSERÇÃO DE MES: 7')],
            [sg.Text('Mês', size=(15, 1)), sg.InputText()],
            [sg.Text('Ano', size=(15, 1)), sg.InputText()],
            
            [sg.Text('Descitor',size=(15, 1)), sg.InputText() ,
            sg.FileBrowse(file_types=(("Descritor Files", "*.npy"),))],
            [sg.Text('Indice',  size=(15, 1)), sg.InputText(),
            sg.FileBrowse(file_types=(("Indice Files", "*.pickel"),))],
            [sg.Button('Iniciar')]
        ]


        #Chamando telinha
        janela = sg.Window("CHAMADA").layout(layout)
        #lendo as informações do input e buttons
        self.button, self.values = janela.Read()

    def Iniciar(self):
        argumentos =self.values
        data= argumentos[0]+"-"+argumentos[1]+"-"+argumentos[2]
        lista =[]
        try:

            m = Manager(str(data))
            #Baixando todas as imagens referentes a data inserida
            key = m.download()
            #Reconhencendo todas as imagens presentes na pasta Analisar
            ra = Reconhecimento(argumentos[4], argumentos[3]).Reconhecer()
            #indice para percorrer a variavel de reconhecimento "ra"
            cont=0
            #Inicializando a linha do excel na primeira
            row=1
            #Inicializando a coluna do excel na 0
            column=0
            #Permitindo o uso de acento...
            book = xlwt.Workbook(encoding="utf-8")
            #Gerando a panilha do execel 
            sheet1 = book.add_sheet("Sheet 1", cell_overwrite_ok=True)
            
            #Percorrendo o nome de todas as imagens
            for valor in key:
                if(ra[cont]!="NA"):
                    #Buscando todas as informações das imagens reconhecidas
                    dados= m.dados(str(valor),str(ra[cont]),str(ra[cont+1]))

                    #Inserindo dados dentro de uma planilha
                    sheet1.write(row, column,str(dados['ra']))
                    sheet1.write(row, column +1, str(dados['nome']))
                    sheet1.write(row, column +2, str(dados['hour']))
                    sheet1.write(row, column +3, str(dados['min']))
                    sheet1.write(row, column +4, str(dados['date']))
                    sheet1.write(row, column +5, str(dados['longitude']))
                    sheet1.write(row, column +6, str(dados['latitude']))
                    
                    #pulando uma linha na planilha do excel
                    row=row+1
                    #Registro().insertRegistro(dados['ra'],dados['nome'],dados['hour'],dados['min'], dados['sec'], dados['date'], dados['latitude'], dados['longitude'])
                
                cont=cont+2

            #Salvando as informações inseridas na planilha
            book.save("users.xls")
            tela=ChamadaView()
            tela.Iniciar()
            #sg.popup(f"Enviado com sucesso")
            
        except:
            sg.popup(f"Erro ao enviar!")
            
tela = TelaPython()
tela.Iniciar()