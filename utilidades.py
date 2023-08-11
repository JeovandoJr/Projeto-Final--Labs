'''
Esse arquivo o professor utilizou para:
    -Verificar a url da imagem
    -Obter o caminho da imagem
    -Listar as imagens do diretório atual
    
'''
import entidades
import filtros
import os
import time
from urllib.parse import urlparse

class Util:
  def extrair_nome_extensao_url(self,url):
    parsed_url = urlparse(url)
    caminho_arquivo = parsed_url.path
    nome_arquivo, extensao = os.path.splitext(os.path.basename(caminho_arquivo))
    return nome_arquivo, extensao

  def wait_for_file(self, caminho, intervalo=1):
      print('Aguarde...')
      while not os.path.exists(caminho):
        time.sleep(intervalo)
        intervalo = intervalo + 1
        print(".", end=" ")
        
class Main:
  def __init__(self, utilidades):
    self.utilidades = utilidades

  def cria_imagem(self, minha_url):
    try:
      print(f'URL: {minha_url}')
      nome_arquivo, extensao_arquivo = self.utilidades.extrair_nome_extensao_url(minha_url)
      arquivo = nome_arquivo + extensao_arquivo
      print(f'Arquivo: {arquivo}')
      meu_download = entidades.Download(url=minha_url, path_arquivo=arquivo)
      print(f'Inicia download...')
      if meu_download.download_file():
        print(f'Download concluído!')
      else:
        print('Erro durante o download!')
      
      #Para reproduzir a imagem  
      imagem = entidades.Imagem(id=1, nome_arquivo=arquivo, path_arquivo=arquivo)
      print(imagem)
      return imagem.conteudo()
    except Exception as ex:
      print(f'Erro ao criar imagem: {str(ex)}')

  def aplica_filtro(self,minha_imagem, nome, extensao, filtro):
    try:
        print('Aplicando filtro')
        # Aplicar o filtro
        imagem = filtro.apply_filter(minha_imagem)
        # Salvar a imagem
        nome = nome + '_imagem.'+ extensao
        imagem.save(nome)
        print(f'Filtro grayscale aplicado com sucesso! Arquivo salvo em {nome}')
    except Exception as ex:
      print(f'Erro ao aplicar filtro: {str(ex)}')
     
     
  def listar_conteudo(self):
    diretorio = "."
    files = os.listdir(diretorio)
    jpeg_files = [file for file in files if file.lower().endswith(".jpeg") or file.lower().endswith(".jpg")]
    png_files = [file for file in files if file.lower().endswith(".png")]
    lista_imagens = jpeg_files + png_files
    
    return lista_imagens
  