'''
Aqui temos um esboço dos filtros que o professor quer.
    -Precisamos refazer os filtros: Cartoon, Negativa e Contorno
'''
from PIL import ImageFilter

class EscalaDeCinza:
    def aplly_filter(self, image):
        # Converte a imagem para Escala de Cinza
        escala_de_cinza = image.convert("L")

        return escala_de_cinza

# Teste: Coloacando primeiro colocando cinza depois o preto
class PretoEBranco:
    def aplly_filter(self, image):
        # Converte a imagem para Escala de Cinza
        escala_de_cinza = image.convert("L")

        # Converte de Escala de Cinza para Preto e Branco
        preto_e_branco = escala_de_cinza.convert("1")

        return preto_e_branco
    
# Teste do Filtro Cartoon
class Cartoon:
    def aplly_filter(self, image):
        # Aplica o filtro de Contorno
        imagem_contorno = image.filter(ImageFilter.EDGE_ENHANCE)

        # Aplica o filtro de Escala de Cinza
        imagem_cinza = imagem_contorno.convert("L")

        # Aplica o filtro de Suavização
        imagem_suavizada = imagem_cinza.filter(ImageFilter.SMOOTH)

        return imagem_suavizada

#Teste Modo Foto Negativa
class Negativo:
    def aplly_filter(self, image):
        # Aplica o filtro de Modo Foto Negativa
        imagem_negativa = image.filter(lambda p: 255 - p)

        return imagem_negativa

# Teste de Modo Contorno
class Contorno:
    def aplly_filter(self, image):
        # Aplica o filtro de Contorno
        imagem_contorno = image.filter(ImageFilter.EDGE_ENHANCE)

        return imagem_contorno

# Teste de Modo Blurred
class Blurred:
    def aplly_filter(self, image):
        # Aplica o filtro de Blurred
        imagem_blurred = image.filter(ImageFilter.BLUR)

        return imagem_blurred
