# -*- coding: utf-8 -*-
"""
Created on Wed Dec 03 13:56:14 2014

@author: fcunha

Realizar simulação do exercício-desafio no slide 40 de Gerenciamento de Memória. 
	Pode ser desenvolvido em qualquer linguagem e programação, desde que realize
      todas as operações conforme o enunciado
	Deverá ser apresentado ao professor e a avaliação será imediata
	Máximo 3 componentes da equipe
	Entrega para dia 5/12/2014

particoes = 10,4,20,18,7,9,12,15
"""



from Tkinter import *

class Aplicacao(Frame):
    def __init__(self):
        Frame.__init__(self)
        #self.lGreeting = Label(self.master, text = 'Bem-Vindo').grid(row = 0 ,column= 4)
        self.create_widgets()
        self.particoes = [[10,0],[4,0],[20,0],[18,0],[7,0],[9,0],[12,0],[15,0]]
    def create_widgets(self):
        
        self.lpart1 = Label(self.master, text = '10' )
        self.lpart1.grid(row = 1, column= 1)
        
        self.lpart2 = Label(self.master, text = '4')
        self.lpart2.grid(row = 1, column = 2 )
        
        self.lpart3 = Label(self.master, text = '20')
        self.lpart3.grid(row = 1 , column = 3)

        self.lpart4 = Label(self.master, text = '18')
        self.lpart4.grid(row = 1 , column = 4)

        self.lpart5 = Label(self.master, text = '7')
        self.lpart5.grid(row = 1 , column = 5)
        
        self.lpart6 = Label(self.master, text = '9')
        self.lpart6.grid(row = 1 , column = 6)
    
        self.lpart7 = Label(self.master, text = '12')
        self.lpart7.grid(row = 1 , column = 7)

        self.lpart8 = Label(self.master, text = '15')
        self.lpart8.grid(row = 1 , column = 8)         

        ############ Rotulo ##################################
        self.lparticao = Label(self.master, text = 'Partições')
        self.lparticao.grid(row = 1 ,column = 0)
            
        ############### REsultados ###############################    
        self.epart1 = Entry(self.master,width = 2)
        self.epart1.grid(row = 2, column =1, sticky = N)
        
        
        self.epart2 = Entry(self.master, width = 2)
        self.epart2.grid(row = 2, column =2, sticky = N)
        
        
        self.epart3 = Entry(self.master, width = 2)
        self.epart3.grid(row = 2, column =3, sticky = N)
        
        
        self.epart4 = Entry(self.master, width = 2)
        self.epart4.grid(row = 2, column =4, sticky = N)
        
        
        self.epart5 = Entry(self.master, width = 2)
        self.epart5.grid(row = 2, column =5, sticky = N)
        
        
        self.epart6 = Entry(self.master, width = 2)
        self.epart6.grid(row = 2, column =6, sticky = N)
        
        
        self.epart7 = Entry(self.master, width = 2)
        self.epart7.grid(row = 2, column =7, sticky = N)
        
        
        self.epart8 = Entry(self.master, width = 2)
        self.epart8.grid(row = 2, column =8, sticky = N)        
        
        self.bttn1 = Button(self.master, text = "Best", command = self.bestFit)
        self.bttn1.grid(row = 5,column = 4)

        self.bttn2 = Button(self.master,text = 'Worst', command = self.worstFit)
        self.bttn2.grid(row = 5, column = 5)  
        
        
        self.bttn3 = Button(self.master,text = 'Next',command = self.nextFit)
        self.bttn3.grid(row = 6, column = 4)  
        
        
        self.bttn4 = Button(self.master,text = 'First',command = self.firstFit)
        self.bttn4.grid(row = 6, column = 5)  
        #self.bttn4.bind('<buttonrelease-1>',self.bestfit())        
                
        self.valor1 = IntVar()
        self.valor2 = IntVar()
        self.valor3 = IntVar()
        self.valor4 = IntVar()
        self.valor5 = IntVar()
        self.valor6 = IntVar()
        self.valor7 = IntVar()
        self.valor8 = IntVar()
        
       
        self.lparticao = Label(self.master, text = 'Partições')
        self.lparticao.grid(row = 1 ,column = 0)
            
        self.eValor1 = Entry(self.master,textvariable = self.valor1 ,width = 2)
        self.eValor1.grid(row = 2, column =1, sticky = N)
                
        self.eValor2 = Entry(self.master,textvariable = self.valor2, width = 2)
        self.eValor2.grid(row = 2, column =2, sticky = N)
                
        self.eValor3 = Entry(self.master,textvariable = self.valor3,width = 2)
        self.eValor3.grid(row = 2, column =3, sticky = N)
                
        self.eValor4 = Entry(self.master,textvariable = self.valor4, width = 2)
        self.eValor4.grid(row = 2, column =4, sticky = N)
                
        self.eValor5 = Entry(self.master,textvariable = self.valor5, width = 2)
        self.eValor5.grid(row = 2, column =5, sticky = N)
        
        
        self.eValor6 = Entry(self.master,textvariable = self.valor6,width = 2)
        self.eValor6.grid(row = 2, column =6, sticky = N)
                
        self.eValor7 = Entry(self.master,textvariable = self.valor7,width = 2)
        self.eValor7.grid(row = 2, column =7, sticky = N)
        
        self.eValor8 = Entry(self.master,textvariable = self.valor8,width = 2)
        self.eValor8.grid(row = 2, column =8, sticky = N)
        
        self.valores = Label(self.master,text = 'Valores')
        self.valores.grid(row = 4,column=0)
        
        self.v1 = IntVar()
        self.v2 = IntVar()
        self.v3 = IntVar()
        
        self.entrada1 = Entry(self.master,textvariable = self.v1, width = 5)
        self.entrada1.grid(row=5,column=0)
        
        self.entrada2 = Entry(self.master,textvariable = self.v2, width = 5)
        self.entrada2.grid(row=6,column=0)

        self.entrada3 = Entry(self.master,textvariable = self.v3, width = 5)
        self.entrada3.grid(row=7,column=0)
        
    def getValues(self):
        a = self.v1.get()
        b = self.v2.get()
        c = self.v3.get()
        valores = [a,b,c]
        
        self.entrada1.delete(0,END)
        self.entrada2.delete(0,END)
        self.entrada3.delete(0,END)
        
        self.entrada1.insert(0,0)
        self.entrada2.insert(0,0)
        self.entrada3.insert(0,0)
        return valores

    def worstFit(self):
        self.zerar()
        valores = self.getValues()
        vetoraux= []
        for i in range(len(valores)):
            for j in range(len(self.particoes)):
                if self.particoes[j][0] >= valores[i] and self.particoes[j][1]== 0 :
                    if self.particoes[j][0] not in vetoraux:
                        vetoraux.append(self.particoes[j][0])
            maior = max(vetoraux)
            if maior >= valores[i]:
                for k in range(len(self.particoes)):
                    if self.particoes[k][0] == maior and self.particoes[k][1] == 0:
                        self.particoes[k][1]= valores[i]
                        vetoraux = []
                        
        self.valor1.set(self.particoes[0][1])
        self.valor2.set(self.particoes[1][1])
        self.valor3.set(self.particoes[2][1])
        self.valor4.set(self.particoes[3][1])
        self.valor5.set(self.particoes[4][1])
        self.valor6.set(self.particoes[5][1])
        self.valor7.set(self.particoes[6][1])
        self.valor8.set(self.particoes[7][1])
         
                 
    def firstFit(self):
        self.zerar()
        aplicacao = self.getValues()
        for i in range(len((aplicacao))):
           for j in range(len(self.particoes)):
               if self.particoes[j][0] >= aplicacao[i] and self.particoes[j][1] == 0:
                   self.particoes[j][1] = aplicacao[i]
                   break
        self.valor1.set(self.particoes[0][1])
        self.valor2.set(self.particoes[1][1])
        self.valor3.set(self.particoes[2][1])
        self.valor4.set(self.particoes[3][1])
        self.valor5.set(self.particoes[4][1])
        self.valor6.set(self.particoes[5][1])
        self.valor7.set(self.particoes[6][1])
        self.valor8.set(self.particoes[7][1])
         
    def guarda(self,valor):
        self.indice = valor
        return self.indice
    def mostra(self):
        #retorna o vetor com as particoes
        return self.particoes
    def zerar(self):
        for i in range(len(self.particoes)):
            if self.particoes[i][1] != 0:
                self.particoes[i][1] = 0
        return self.mostra()

    def bestFit(self):
        self.zerar()
        valores = self.getValues()
        valores = self.organiza(valores)
        vetoraux =[]
        for i in range(len(valores)):
            for j in range(len(self.particoes)):
                if self.particoes[j][0] >= valores[i] and self.particoes[j][1]== 0 :
                    if self.particoes[j][0] not in vetoraux:
                        vetoraux.append(self.particoes[j][0])
            menor = min(vetoraux)
            if menor >= valores[i]:
                for k in range(len(self.particoes)):
                    if self.particoes[k][0] == menor and self.particoes[k][1] == 0:
                        self.particoes[k][1]= valores[i]
                        vetoraux =[]
                        
                    #vetoraux.remove(menorPart)
        #vetoraux = []
        self.valor1.set(self.particoes[0][1])
        self.valor2.set(self.particoes[1][1])
        self.valor3.set(self.particoes[2][1])
        self.valor4.set(self.particoes[3][1])
        self.valor5.set(self.particoes[4][1])
        self.valor6.set(self.particoes[5][1])
        self.valor7.set(self.particoes[6][1])
        self.valor8.set(self.particoes[7][1])
        
    def organiza(self,vetor):
        for i in range(len(vetor)):
            for j in range(len(vetor)-1):
                if vetor[j] > vetor[j+1]:
                    aux = vetor[j]
                    vetor[j] = vetor[j+1]
                    vetor[j+1] = aux
        return vetor
        
    def nextFit(self):
        aplicacao = self.getValues()
        self.zerar()
        ultimo = 0        
        for i in range(len(aplicacao)):
            for j in range(ultimo,len(self.particoes)):
                if self.particoes[j][0] >= aplicacao[i] and self.particoes[j][1] == 0:
                    self.particoes[j][1] = aplicacao[i]
                    ultimo = j
                    break
        
        self.valor1.set(self.particoes[0][1])
        self.valor2.set(self.particoes[1][1])
        self.valor3.set(self.particoes[2][1])
        self.valor4.set(self.particoes[3][1])
        self.valor5.set(self.particoes[4][1])
        self.valor6.set(self.particoes[5][1])
        self.valor7.set(self.particoes[6][1])
        self.valor8.set(self.particoes[7][1])
app = Aplicacao()
app.mainloop()
app.getValues()
        
        
