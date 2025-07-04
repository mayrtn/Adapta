import nltk
from nltk.corpus import wordnet, stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from googletrans import Translator
from abc import ABC, abstractmethod
import pyphen

#asegurarse de tener descargados los recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('stopwords')

translator = Translator()
diccionario_silabas = pyphen.Pyphen(lang='es')

#varible global lista de conectores, se inicia desde el main, unas sola vez cuando se inicia el programa
lista_conectores = []

def set_lista_conectores(nueva_lista):
    global lista_conectores  # le digo a Python que quiero modificar la variable global
    lista_conectores = nueva_lista


#decorador depuracion por consola
def log_transformacion(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Transformando texto con: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

#clase base (hice la clase abstracta MA)
class TextoOriginal(ABC):
    def __init__(self, texto):
        self.texto = texto

    def tokenizar(self):
        #tokenizar el texto
        tokens = word_tokenize(self.texto)
        return tokens
    
    @abstractmethod #metodo abstracto
    def adaptar(self):
        pass


#clase hija para dislexia.
class AdaptadorDislexia(TextoOriginal):

    def __init__(self, texto):
        super().__init__(texto)
        self.tokens = self.tokenizar() #tokeniza el texto automaticamente al instanciar la clase

#adaptar solo se ocupa de llamar a otros metodos en orden, y devolver el texto final
    def adaptar(self):
        texto_sinonimos = self.buscar_sinonimos(self.tokens)  
        texto_silabas = self.separar_silabas(texto_sinonimos)  
        texto_final_token = self.pausar_texto(texto_silabas) 
        texto_final = self.destokenizar(texto_final_token) 
        return texto_final

    # metodos auxiliares - procesan y devuelven listas de str
    

# BUSCAR SINONIMOS MAS CORTOS PARA PALABRAS LARGAS
    def buscar_sinonimos(self, palabras):  
        texto_sinonimos = []
        for p in palabras:
            if len(p) > 7:
                palabra = self.sinonimo_corto(p)  
            else:
                palabra = p
            texto_sinonimos.append(palabra)  
        return texto_sinonimos


    def sinonimo_corto(self, palabra):  
        sinonimos = []

        for syn in wordnet.synsets(palabra, lang="spa"):  
            for lemma in syn.lemma_names("spa"):
                if lemma != palabra:
                    sinonimos.append(lemma)

        if sinonimos == []:
            sinonimo = palabra
        else:
            palabra_mas_corta = sinonimos[0]
            for s in sinonimos:
                if len(s) < len(palabra_mas_corta):
                    palabra_mas_corta = s
            sinonimo = palabra_mas_corta

        return sinonimo
    
# SEPARAR EN SILABAS PALABRAS DE 5 CARACTERES O MAS / utiliza pyphen ya que NLTK no soporta silabeo en español
    def separar_silabas(self, palabras):
        texto_silabas = []
        
        for p in palabras:
            if len(p)>5: 
                palabra_separada = diccionario_silabas.inserted(p)
                texto_silabas.append(palabra_separada)
            else: 
                texto_silabas.append(p)

        return texto_silabas

# INSERTAR PAUSAS EN EL TEXTO PARA FACILITAR SU COMPRENSION Y EVITAR FRASES LARGAS
    def pausar_texto(self, texto_silabas):
        texto_pausado = []
        for palabra in texto_silabas:
            if palabra.lower() in lista_conectores:
                texto_pausado.append('|')
                texto_pausado.append(palabra)
            elif palabra.lower() == ",":
                texto_pausado.append(palabra)
                texto_pausado.append('   ') 
            elif palabra.lower() == ".":
                texto_pausado.append(palabra)
                texto_pausado.append('\n')
            else:
                texto_pausado.append(palabra)
        
        return texto_pausado

#DESTOKENIZAR -  TRANSFORMA UNA CADENA DE TOKENS EN UN TEXTO LEGIBLE 
    def destokenizar(self, tokens):
        texto_final = ''
        signos = {'.', ',', '|', '\n'}
        for i, token in enumerate(tokens):
            if i == 0:
                texto_final += token
            elif token in signos:
                texto_final += token
            else:
                texto_final += ' ' + token
        return texto_final

#FUNCION GLOBAL
#Genera una lista de conectores usando stopwords con pos tags de NLTK en ingles y luego traduciendolos al español
def generar_lista_conectores():
    
    # Obtener stopwords en inglés y taggearlas para luego poder filtrar resultados con esos POS tags
    stopwords_ingles = stopwords.words('english')
    palabras_etiquetadas = pos_tag(stopwords_ingles)

    etiquetas_conectores = {'CC', 'IN', 'RB', 'UH', 'RP', 'WRB'}

    conectores_ingles = []

    for palabra, etiqueta in palabras_etiquetadas:
        if etiqueta in etiquetas_conectores:
            conectores_ingles.append(palabra)

    # Traducir conectores al español 
    conectores_espanol = []

    for conector in conectores_ingles:
        try:
            traduccion = translator.translate(conector, src='en', dest='es')
            if traduccion is not None and traduccion.text is not None and len(traduccion.text.strip()) > 0:
                traducciones = traduccion.text.split(',')
                for t in traducciones:
                    palabra_traducida = t.strip().lower()
                    if palabra_traducida != '':
                        conectores_espanol.append(palabra_traducida)
        except Exception:
            # En caso de error con alguna palabra por no tener traduccion la ignoramos
            continue

    return conectores_espanol


   