
#ARQUIVO = "Percentualdefrequencia.txt"
ARQUIVO = "Percentual_2018_2.TXT"
LIMITE = 80

class Aluno():
    def __init__(self,splitted):
        self.id = splitted[0]
        self.nome = splitted[1].replace("ADP", "ADP ").replace("MSI", "MSI ").replace("TGP", "TGP ").replace("OCP", "OCP ")
        self.sobrenome = splitted[2]
        self.percentualdefrequencia = splitted[-1].replace(",",".")
        self.disciplinas = []

    def __str__(self):
        return ("%s | Aluno: %s %s | frequencia: %s%%" %(self.id, self.nome, self.sobrenome, self.percentualdefrequencia))

    def esta_abaixo_limite(self):
        return float(self.percentualdefrequencia) < LIMITE


disciplinas=[]

if __name__ == '__main__':

    content = open(ARQUIVO, encoding = "ISO-8859-1")
    lines = content.readlines()
    cont=1
    aluno = None
    for line in lines[5:]:
        newline = line.strip().strip("\n")
        splitted = newline.split()

        if (splitted):
            id = splitted[0]
        else:
            id = ""
            
        if (id.isnumeric() and int(id) == cont):
            aluno = Aluno(splitted)
            if (aluno.esta_abaixo_limite()):
                print (aluno)
            cont+=1
        else:
            aluno.disciplinas.append(newline)

    print (aluno.disciplinas)
