# FrontEndProfessor
Automação de chamada de alunos em uma Universidade, com a utilização de bibliotecas de processamento de imagens

### Requisitos(Windows)

 - [Anaconda](https://www.anaconda.com/products/individual)
 - [Python](https://www.python.org/downloads/) 
 - [Build tools for visual studio 2019](https://visualstudio.microsoft.com/pt-br/downloads/)
    (Selecionar C++ build Tools => Windows 10 SDK e ferramentas de compilação MSVC v142 x64 / x86)

 
### Iniciando instalações de dependência (WINDOWS)
```
$ conda install -c conda-forge dlib
```
```
$ conda install -c conda-forge opencv
```
```
$ conda install -c conda-forge pillow
```

### Iniciando instalações de dependência (UBUNTU)
```
$ sudo apt-get update
```
```
$ sudo apt-get upgrade
```
```
$ sudo apt-get install build-essential cmake pkg-config
```
```
$ sudo apt-get install libx11-dev libatlas-base-dev
```
```
$ sudo apt-get install libgtk-3-dev libboost-python-dev
```
```
$ sudo apt-get install python-opencv
```
```
$ sudo python3 -m pip install dlib
```
### Iniciando Projeto
```
$ git clone https://github.com/viniciusleal34/FrontEndProfessor.git
```
```
$ cd FrontEndProfessor
```
```
$ python3 -m pip install -r requirements.txt
```
```
$ python app.py
```

### ATENÇÃO

- Verificar se todas as configurações do banco de dados, foram adicionados corretamente
- Verificar se os arquivos de treinamento, estão na pasta src/Descritor(indices.pickel, descritores.npy)


### Pontos a melhorar/recomendações

- Otimização no algoritmo de reconhecimento
- Adicionar funcionalidade após os usuários serem adicionados ao banco de dados, excluir as imagens salvas


## Projetos relacionados
- [Treinamento](https://github.com/viniciusleal34/Treinamento-Reconhecimento-Facial)
- [Projeto mobile](https://github.com/viniciusleal34/front-end-aluno)
- [API](https://github.com/viniciusleal34/api-flask)

## Autores

* **Vinicius Leal**

## Licença
 
 - Fatec

## Agradecimentos

* Dilermando Piva Jr
* Fatec ITU
