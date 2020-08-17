import PySimpleGUI as sg
import numpy as np
import os
from src.read_planilha import Planilha
from src.registro import Registro

PATH_INDICE = os.path.join(os.getcwd(), 'src','Descritor','indices.pickel')
indice = np.load(PATH_INDICE)

class ChamadaView:
    def __init__(self):
    #inicializando
        layout = [
            [
             sg.Text('Ra', size=(15, 1)), 
             sg.Text('Nome', size=(15, 1)),
             sg.Text('Data', size=(15, 1)),
             sg.Text('Horario', size=(15, 1)), 
             sg.Text('Presenças', size=(15, 1))
             ]
        ]
        self.alunos =[]
        achou = False
        planilha = Planilha('users.xls', '2', '0').open()
        #Percorrendo indice de alunos cadastrados
        #para adicionar os nomes na tela de presentes
        for i in range(len(indice)):
            #percorrendo arquivo indice para encontra o nome e ra de todos alunos
            if (int(os.path.split(indice[i])[1].split(".")[2]) == 0):
                #retirando o ra e o nome dos alunos do arquivo do indice
                codigo = os.path.split(indice[i])[1].split(".")[0]
                nome = os.path.split(indice[i])[1].split(".")[1]
                achou= False
                #percorrendo a planilha do excel que foi identificado os alunos
                #presentes
                for chave in range(len(planilha)):
                    #Analisando se codigo encontrado, bate com o indice
                    if (str(planilha[chave][0]) == str(codigo)):
                    #Criando a wigets das telas, se caso alunos está presente
                        layout.append([
                            sg.Text(codigo, size=(15, 1)), 
                            sg.Text(nome, size=(15, 1)), 
                            sg.Text(str(planilha[chave][4]), size=(15, 1)),
                            sg.Text(str(planilha[chave][2])+":"+
                            str(int(planilha[chave][3])), size=(15, 1)),
                            sg.Checkbox(' ',default=True, key='presenca')
                            ])
                        #Guardado dados de alunos reconhecidos
                        self.alunos.append(planilha[chave])
                        achou = True
                    
                if achou != True:   
                #Criando as wigets na tela dos alunos não presentes
                    layout.append([
                        sg.Text(codigo, size=(15, 1)), 
                        sg.Text(nome, size=(15, 1)), 
                        sg.Text(str(planilha[0][4]), size=(15, 1)),
                        sg.Text(str(planilha[0][2])+":"+str(int(planilha[0][3])), 
                        size=(15, 1)),
                        sg.Checkbox(' ',default=False, key='presenca')
                        ]) 
                #guarando dados dos alunos não reconhecidos, setando valores default
                
                    self.alunos.append([
                    str(codigo),
                    str(nome),
                    int(planilha[0][2]),
                    int(planilha[0][3]),
                    str(planilha[0][4]),
                    float(planilha[0][5]),
                    float(planilha[0][6]),
                    ]
                    )
                
        layout.append([sg.Button('Enviar')])
                

        janela = sg.Window("Presentes").layout(layout)
        self.button, self.values = janela.Read()
    def Iniciar(self):
        cont=0
        #Pegando nome do key que fala se aluno esta presente ou não
        for valor in self.values:
            #verificando se valor é True para saber se o aluno está presente
            if(self.values[str(valor)] == True):
                #Inserindo alunos presentes no banco de dados
                #0 codigo, 1 nome, 2 hour, 3 min, 4 sec, 5 date, 6 lat, 7 long
                Registro().insertRegistro(
                    self.alunos[cont][0],
                    self.alunos[cont][1],
                    self.alunos[cont][2],
                    self.alunos[cont][3],
                    0,
                    self.alunos[cont][4],
                    self.alunos[cont][6],
                    self.alunos[cont][5]
                )
            cont=cont+1
               


