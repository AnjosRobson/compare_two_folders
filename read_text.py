import os
import pandas as pd
import tkinter
from tkinter.filedialog import askdirectory
import sys
import csv
import subprocess


abrir = [None,None]   #matriz para guardar as informações das pasta dos arquivos
txt_erros = ' ' #variavel criada para poder elencar os erros/ diferenças encontradas
importados = ' '

# primeira_pasta = r'C:\Users\zhymb3c\Downloads\KAIZEN 2\KAIZEN\compare\ANTES'
# segunda_pasta = r'C:\Users\zhymb3c\Downloads\KAIZEN 2\KAIZEN\compare\DEPOIS'

# files_pasta_one = os.listdir(primeira_pasta)
# files_pasta_two = os.listdir(segunda_pasta)

# print ("Começar o Compare_one : \n")
# print(f'{primeira_pasta}'+ '\\'+ f'{files_pasta_one[3]}')
# print("acabou")
# compare_one = pd.read_csv((f'{primeira_pasta}'+ '\\' + files_pasta_one[0]), header=None, sep='\t', low_memory=False, encoding='latin')
# print(f"Primeiro {compare_one}") 
# print(f"segunda pasta: {segunda_pasta}")
# print (f"Procurar pelo {files_pasta_one[4]} no caminho {segunda_pasta}\n\n")
# print(f'{segunda_pasta}'+ '\\'+ f'{files_pasta_one[4]}')
# compare_two = pd.read_csv((f'{segunda_pasta}' + '\\' + files_pasta_one[0]), header=None, sep='\t', low_memory=False, encoding='latin')
# print(f"segundo: {compare_two}")

def abrirpasta(n): #função para abrir a pasta no botão
     caminho_do_arquivo = askdirectory(title='Selecione pasta')
     print(caminho_do_arquivo)
     abrir[n]=caminho_do_arquivo   #inclui o caminho_do_arquivo em uma lista
     print(abrir)
     print("\n\n caminhos da pasta 1: " + str(abrir[0]))
     print("\n\n caminhos da pasta 2: " + str(abrir[1]))
     
     
def comparar():
     global txt_erros
     global importados
     txt_erros = ''
     print("\n \n Declaração de pastas: doing \n \n")
     pasta1 = os.listdir(abrir[0])   #variavel onde guarda as informações de todos os arquivos da pasta1
     print(pasta1)
     pasta2 = os.listdir(abrir[1])  #variavel onde guarda as informações de todos os arquivos da pasta2
     print (abrir[0][1])
     print("\n pasta 2: " + str(pasta1) + "\n")

     all_dir = []
     all_dir.extend(pasta1)
     all_dir.extend(pasta2)
     all_dir = list(dict.fromkeys(all_dir))
     print("Todos os diretórios: " + str(all_dir))
     
     error = []  #lista para receber os erros 
     print("\n --------- entrou na comparação -----------\n")
     for file in range(0, len(all_dir)):        #mostra a quantidade de arquivos da pasta 
          # print("\n \n  ---------file: " + str(pasta1(file)) + "\n \n ------------------------") 
          # print(pasta1[file]) 
          print("Directory: " +all_dir[file])   

          print(all_dir[file])
          print(pasta2.__contains__(all_dir[file]))
          print(pasta1.__contains__(all_dir[file]))
          if(pasta2.__contains__(all_dir[file]) and pasta1.__contains__(all_dir[file])):   #esta comparando os dois arquivos 
               print("\n Compare One \n")
               compare_one = pd.read_csv((f'{abrir[0]}' + '/'+ all_dir[file]), header=None, sep='\t', low_memory=False, encoding='latin')
               print("começar compare_two")
               compare_two = pd.read_csv((f'{abrir[1]}' + '/'+ all_dir[file]), header=None, sep='\t', low_memory=False, encoding='latin') #lê os arquivos da pasta 2
               print("terminado compare_two")
               
               for lines in range(0, len(compare_one)):  #lê linha por linha dos arquivos
                    print("começou a comparar")
                    if lines >= 999:
                          print("Quebrou" + str(lines))
                          importados = "O arquivo " + str(pasta1[file]) + " passou das 999 linhas. \n"
                          break
                    for columns in range(0, len(compare_one.columns)): #lê coluna por coluna dos arquivos
                         # print(str(compare_one[columns][lines]) + " & " + str(compare_two[columns][lines]))
                         
                         if(str(compare_one[columns][lines]).strip() != str(compare_two[columns][lines]).strip() and str(compare_one[columns][lines]).strip() != "nan"):   #compara as linhas e colunas dos arquivos 1 e 2
                              error.append(["erro em:" + str(compare_one[columns][lines]).strip()+ " & " + str(compare_two[columns][lines]).strip() + ", no arquivo " + str(all_dir[file]) + " na linha " + str((lines +1)) + " e coluna " + str((columns+1))])
                              print(str(compare_one[columns][lines]))
                              # print("entrou em erro")
                         # print("coluna: ", columns)

                    # print("lines", lines)
                    
               for erro in error:  # lista o que está errado
                    print(erro)
                    txt_erros = str(erro) + '\n'+txt_erros 

          elif (pasta1.__contains__(all_dir[file]) == False ):
               txt_erros = f'{txt_erros} \n Não contém o arquivo {all_dir[file]} na pasta 1 escolhida.'
          
          elif (pasta2.__contains__(all_dir[file]) == False):
               txt_erros = f'{txt_erros} \n Não contém o arquivo {all_dir[file]} na pasta 2 escolhida.'
          
               
     if (len(error) == 0 and txt_erros == ' '): # quando não encontrar erros no arquivos vai aparecer essa msg
          importados = "Nenhum erro encontrado!"
     elif (len(error) > 0 or txt_erros != ' '):
          with open("Erros encontrados.txt", "w") as output_file:
               output_file.write("\n" + txt_erros)
               importados = "Arquivo de comparação exportado!"
     
           
     
     
                  
                         
     botao3 = tkinter.Label(janela, text='Erros Encontrados: \n'+ importados, width=80, height=25, borderwidth=1, relief='solid').place(x=125, y=200) 


janela = tkinter.Tk() 
janela.geometry ('800x600')  #tamanho da caixa
botao1 = tkinter.Button(janela, justify='center', text='Clique aqui e inclua a pasta 1', command=lambda: abrirpasta(0)).place(x=310, y=50) #botão para puxar a pasta1
botao2 = tkinter.Button(janela, justify='center', text='Clique aqui e inclua a pasta 2', command=lambda: abrirpasta(1)).place(x=310, y=100) #botão para puxar a pasta1
botao_comp = tkinter.Button (janela, justify='center', text='Clique aqui para comparar', command=comparar).place(x=315, y=150) #botão para comparar as duas pastas
botao3 = tkinter.Label(janela, justify='center', text='Erros Encontrados: ' + importados, width=80, height=25, borderwidth=1, relief='solid').place(x=125, y=200) #botao para aparecer a caixa com os erros
janela.title ('Comparação de Arquivos')  #titulo da caixa 
tkinter.mainloop()  









     # pasta1 = os.listdir(abrir[0])   #variavel onde guarda as informações de todos os arquivos da pasta1
     # print("\n pasta 1: " + pasta1 + "\n")
     # pasta2 = os.listdir(abrir[1])  #variavel onde guarda as informações de todos os arquivos da pasta2



# import pandas as pd
# import os

# pasta1 = os.listdir(r'C:\Users\QB72WF9\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\KAIZEN 2\KAIZEN\teste')   #variavel onde guarda as informações de todos os arquivos da pasta
# pasta2 = os.listdir(r'C:\Users\QB72WF9\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\KAIZEN 2\KAIZEN\teste2')  #variavel onde guarda as informações de todos os arquivos da pasta

# error = []             #matriz para receber os dados em colunas e linhas 
# for file in range(0, len(pasta1)):        #mostra a quantidade de arquivos da pasta 
#      print(file) 
#      print(pasta1[file])
#      compare_one = pd.read_csv((r'C:\Users\QB72WF9\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\KAIZEN 2\KAIZEN\teste/'+ pasta1[file]), header=None, delimiter='\s+')     #compara 
#      if(pasta2.__contains__(pasta1[file])):   #esta comparando os dois arquivos 
#         compare_two = pd.read_csv((r'C:\Users\QB72WF9\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\KAIZEN 2\KAIZEN\teste2/' + pasta2[file]), header=None, delimiter='\s+')

#         for lines in range(0, len(compare_one)):
#             # print("começou a comparar")
#             for columns in range(0, len(compare_one.columns)):
#                 print(str(compare_one[columns][lines]) + " & " + str(compare_two[columns][lines]))
#                 if(str(compare_one[columns][lines]) != str(compare_two[columns][lines]) and str(compare_one[columns][lines]) != "nan"):
#                     error.append(["erro em:" + str(compare_one[columns][lines])+ " & " + str(compare_two[columns][lines]) + ", no arquivo " + str(pasta1[file]) + " na linha " + str((lines +1)) + " e coluna " + str((columns+1))])
#                     print(str(compare_one[columns][lines]))
#                     print("entrou em erro")
#                 print("coluna: ", columns)


#             print("lines", lines)

# for erro in error:
#    print(erro)


# read_file = pd.read_csv("./teste/SAFX48_Antes (1).txt", header=None, delimiter='\s+')
#
# read_file.to_csv("teste123.csv",header=None)
# print(read_file)
# print(read_file[2][0])
# print(len(read_file.columns))
# print(len(read_file))



# lines1 = []

# path_loop = 1

# num = 1

# for path in pasta1:
#     arquivos = open(path).read()
#     print(path)
#     print(arquivos)

#     with open(path) as f1:
#         content1 = f1.read()     #content é o arquivo txt em branco que lê o file1 
#         content1 = content1.split("\n")  #content1 é o arquivo file1 dividido em linha
#         for line1 in content1:   
#             lines1.append(line1)  #pega a lista e acrescenta as linhas e coloca na ordem (sempre na ultima posição)
#             if num == 10 or num == len(content1):  #se o arquivo tem 1000 linhas ou a qtidade de linhas total do arquivo num sempre que vai pelo loop aumenta 1
#                 num = 1  #quando o num chegar na condição, ex 1000 ele volta a ser valor 1     
#                 break

#             num = num + 1  #acrescenta no contador (vira 1, 2, 3 quando passa no loop ex: 1 == 1000, depois 2 == 1000)
#     path_loop = path_loop + 1

# with open("file1.txt") as f1:
#     content1 = f1.read()     #content é o arquivo txt em branco que lê o file1 
#     content1 = content1.split("\n")  #content1 é o arquivo file1 dividido em linhas

# with open("file2.txt") as f2:
#     content2 = f2.read()
#     content2 = content2.split("\n")

# lines1 = []   #criou as listas
# lines2 = []
# num = 1       #foi criado para ser um contador - variavel inicial


# for line1 in content1:   
#     lines1.append(line1)  #pega a lista e acrescenta as linhas e coloca na ordem (sempre na ultima posição)
#     if num == 10 or num == len(content1):  #se o arquivo tem 1000 linhas ou a qtidade de linhas total do arquivo num sempre que vai pelo loop aumenta 1
#         num = 1  #quando o num chegar na condição, ex 1000 ele volta a ser valor 1     
#         break

#     num = num + 1  #acrescenta no contador (vira 1, 2, 3 quando passa no loop ex: 1 == 1000, depois 2 == 1000)

# for line2 in content2:
#     lines2.append(line2)
#     if num == 10 or num == len(content2):
#         num = 1
#         break

#     num = num + 1

# loop = 0
# erros = 0
# for line in line1:
#     if line == line2[loop]:
#         erros = erros + 1
#     loop = loop +1

# print("erros", erros)

# print(lines1)
