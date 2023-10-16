import random
cursos = [ ]

disciplinas = []

totalAlunos = []

class Aluno:
    def __init__(self, ra, nome, cpf,id_curso):
        self.ra = ra
        self.nome = nome
        self.cpf = cpf
        self.id_curso = id_curso
        self.imagem = ""
        self.disciplina = ""

class Curso:
    def __init__(self, id_curso, nome, duracao):
        self.id_curso = id_curso
        self.nome = nome
        self.duracao = duracao
        self.disciplinas = []
        self.alunosDoCurso = []

    def listarDisciplinas(self):
        listacomNomes = []
        for disciplina in self.disciplinas:
            nomeDoCurso = disciplina["Nome"]
            listacomNomes.append(nomeDoCurso)
        return listacomNomes



biologia = {"id" : 1,"Nome" : "Biologia"}
genetica = {"id" : 2,"Nome" : "Genetica"}
litRussa = {"id" : 2,"Nome" : "Literatura Russa"}

programacaoOrientadaObjetos = {"id" : 2,"Nome" : "Programacao Orientada a objetos"}

programacaoFuncional = {"id" : 3,"Nome" : "Programacao Funcional"}


def listarNomesDeCurso (cursos:list):
    listaComNomes = []
    for curso in cursos:
        nomeDOCurso = curso.nome
        listaComNomes.append(nomeDOCurso)
    return listaComNomes


def listarDisciplinas (curso):
    listacomNomes = []
    for disciplina in curso.disciplinas:
        nomeDoCurso = disciplina["Nome"]
        listacomNomes.append(nomeDoCurso)
    return listacomNomes




cursoDeCincias = Curso(1,"Ciencias Biologicas",4)
cursoDeCincias.disciplinas.append(biologia)
cursoDeCincias.disciplinas.append(genetica)
cursoDeInformatica = Curso("2","Ciencia da Computacao",4)
cursoDeInformatica.disciplinas.append(programacaoOrientadaObjetos)
cursoDeInformatica.disciplinas.append(programacaoFuncional)
cursoDeLetras = Curso(3,"Letras - Fefelech",3)
cursoDeLetras.disciplinas.append(litRussa)
cursos.append(cursoDeCincias)
cursos.append(cursoDeInformatica)
cursos.append(cursoDeLetras)