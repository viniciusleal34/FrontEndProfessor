# -*- coding: utf-8 -*-
import dlib
import cv2
import os
import glob
import pickle as cPickle
import datetime
import numpy as np
from datetime import datetime, date

PATH_RECONHECIMENTO = os.path.join(os.getcwd(), 'src','IA','dlib_face.dat')
PATH_DETECTOR = os.path.join(os.getcwd(), 'src','IA','shape.dat')
PATH_DESCRITOR = os.path.join(os.getcwd(),'src','Descritor','descritores.npy')
PATH_INDICE = os.path.join(os.getcwd(), 'src','Descritor','indices.pickel')
PATH_IMAGE = os.path.join(os.getcwd(), 'src','analisar')

class Reconhecimento:
    def __init__(self,indice=PATH_INDICE, descritorFace=PATH_DESCRITOR,caminho=PATH_IMAGE, formato="*.jpg",  limiar = 0.50, detectorPontos=PATH_DETECTOR, reconhecimentoFacial=PATH_RECONHECIMENTO):
        self.cont = 0
        self.detectorFace = dlib.get_frontal_face_detector()
        self.detectorPontos =  dlib.shape_predictor(detectorPontos)
        self.reconhecimentoFacial = dlib.face_recognition_model_v1(reconhecimentoFacial)
        self.indice = np.load(indice)
        self.descritoresFaciais= np.load(descritorFace)
        self.limiar = limiar
        self.caminho = caminho
        self.formato = formato




    def Reconhecer(self):
        lista =[]
        for arquivo in glob.glob(os.path.join(self.caminho, self.formato)):
            #Lendo as imagens
            imagem = cv2.imread(arquivo)
            #Gerando os descritores da face
            facesDetectadas = self.detectorFace(imagem,0)
            for face in facesDetectadas:
                e, t, d, b = (int(face.left()), int(face.top()), int(face.right()), int(face.bottom()))
                pontosFaciais = self.detectorPontos(imagem, face)
                descritorFacial = self.reconhecimentoFacial.compute_face_descriptor(imagem, pontosFaciais)
                listaDescritorFacial = [fd for fd in descritorFacial]
                #convertendo de uma lista comum de python para uma de numpy
                npArrayDescritorFacial = np.asarray(listaDescritorFacial, dtype=np.float64)
                npArrayDescritorFacial = npArrayDescritorFacial[np.newaxis, :]

                distancias = np.linalg.norm(npArrayDescritorFacial - self.descritoresFaciais, axis=1)
                minimo = np.argmin(distancias)
                distanciaMinima = distancias[minimo]

                if distanciaMinima <= self.limiar:
                    tempo = datetime.now()
                    codigo = os.path.split(self.indice[minimo])[1].split(".")[0]
                    nome= os.path.split(self.indice[minimo])[1].split(".")[1]
                    lista.append(codigo)
                    lista.append(nome)
                    
                else:
                    codigo = 'NA'
                    lista.append(codigo)
                    lista.append(codigo)
        return(lista)
