import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

#asegurarse de tener descargados los recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('stopwords')

#decorador para registro de procesamiento
def log_transformacion(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Transformando texto con: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

#clase base
class AdaptadorTexto:
    def __init__(self, texto):
        self.texto = texto
    def adaptar(self):
        raise NotImplementedError("Este método debe ser implementado por subclases")

#clase hija para dislexia
class AdaptadorDislexia(AdaptadorTexto):
    @log_transformacion
    def adaptar(self):
        #tokenizar el texto
        tokens = word_tokenize(self.texto.lower())
        
        #filtrar signos de puntuación y stopwords para simplificación
        stop_words = set(stopwords.words('spanish'))
        tokens_filtrados = [t for t in tokens if t not in stop_words and t not in string.punctuation]

        #regla simple: separar sílabas con guiones para facilitar lectura
        adaptado = ' - '.join(tokens_filtrados)
        return adaptado