


class GerenciaMemoria():
    particoes = [[10,0],[4,0],[20,0],[18,0],[7,0],[9,0],[12,0],[15,0]]
    ## acho que retirando/matando isso vai ajudar
    """esta ficando todos os valores no vetor aux""" 
    ##aplicacao = 0
    #Best Fit
    @classmethod
    def bestFit(self,valor):
        vetoraux = []
        aplicacao = valor
        ## verifica as particoes na qual a processo se encaixa
        ## e insere no vetor aux
        for i in range(len(self.particoes)):
            if self.particoes[i][0] >= aplicacao and self.particoes[i][1]==0 :
                vetoraux.insert(i,self.particoes[i][0])
        ## verifica o menor valor no vetor aux
        menorPart = min(vetoraux)
        ## adiciona o processo no vetor com o menor valor "particao"
        for i in range(len(self.particoes)):
            if self.particoes[i][0] == menorPart:
                self.particoes[i][1]= aplicacao
        del vetoraux
    def worstFit(self,valor):
        vetoraux = []
        aplicacao = valor
        ## verifica as particoes na qual a processo se encaixa
        ## e insere no vetor aux
        for i in range(len(self.particoes)):
            if self.particoes[i][0] >= aplicacao and self.particoes[i][1] == 0:
                vetoraux.insert(i,self.particoes[i][0])
        ## verifica o menor valor no vetor aux
        menorPart = max(vetoraux)
        ## adiciona o processo no vetor com o menor valor "particao"
        for i in range(len(self.particoes)):
            if self.particoes[i][0] == menorPart:
                self.particoes[i][1]= aplicacao
        del vetoraux
    
    def netxFit(self,valor):
        aplicacao = valor

        ## verifica as particoes na qual a processo se encaixa
        ## e insere no vetor aux
        for i in range(len(self.particoes)):
            if self.particoes[i][0] >= aplicacao and self.particoes[i][1] <= 0:
                self.particoes[i][1] = aplicacao
                indice = i+1
                self.indice = indice
                break
        

        ## verifica o menor valor no vetor aux
        '''menorPart = min(vetoraux)
        ## adiciona o processo no vetor com o menor valor "particao"
        for j in range(len(self.particoes)):
            if self.particoes[j][0] == menorPart:
                self.particoes[j][1]= aplicacao
                ultimo = j
                break
        del vetoraux'''
        
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

    #Fist Fit

a = GerenciaMemoria()
b = GerenciaMemoria()
c = GerenciaMemoria()
c.netxFit(3)
print c.mostra()
#print 'indice',c.indice
print c.indice

d = GerenciaMemoria()
d.netxFit(4)
print d.mostra()
print d.indice

e = GerenciaMemoria()
