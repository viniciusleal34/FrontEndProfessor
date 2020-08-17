#encoding: utf-8
import xlrd
import os
PATH_LOCAL = os.path.join(os.getcwd(),'users.xls') 
class Planilha:
    def __init__(self, local, inicio, colunas):
        self.local = local
        #linha para iniciar a analise
        self.inicio = inicio
        #coluna para iniciar a analise
        self.colunas = colunas

    def open(self):
        #setando onde irá começa e o local da planilha
        work = xlrd.open_workbook(self.local)
        worksheet = work.sheet_by_index(0)
        lista = []
        #lendo todos os dados da planilha do excel
        for row_num in range(worksheet.nrows):
            if row_num < int(self.inicio) - 1:
                continue
            for indice in self.colunas:
                row = worksheet.row_values(row_num)
                lista.append(row)

        return lista
