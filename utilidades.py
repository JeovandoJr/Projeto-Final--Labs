
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
      # print(f'URL: {minha_url}')

      nome_arquivo, extensao_arquivo = self.utilidades.extrair_nome_extensao_url(minha_url)
      arquivo = nome_arquivo + extensao_arquivo

      # print(f'Arquivo: {arquivo}')
      meu_download = entidades.Download(url=minha_url, destino_arquivo=arquivo)

      if meu_download.download_file():
        print(f'Download concluído!')
      else:
        print('Erro durante o download!')

      imagem = entidades.Imagem(id=1, nome_arquivo=arquivo, destino_arquivo=arquivo)
      # print(imagem)
      return imagem.conteudo()

    except Exception as ex:
      print(f'Erro ao criar imagem: {str(ex)}')

  # Filtros:
  def aplica_filtro_escala_de_cinza (self, minha_imagem, nome, extencao):
    try:
      escalaDeCinza_filtro = filtros.EscalaDeCinza()
      filtro_EscalaDeCinza_aplicado = escalaDeCinza_filtro.aplicar_filtro(minha_imagem)
      nome1 = nome + "_escala_de_cinza" + extencao
      filtro_EscalaDeCinza_aplicado.save(nome1)
      print(f'Filtro Escala de Cinza aplicado com sucesso!\n')
    except Exception as ex:
      print(f"Erro ao aplicar filtro escala de cinza: {str(ex)}")

  def aplica_filtro_preto_e_branco (self, minha_imagem, nome, extencao):
    try:
      pretoEBranco_filtro = filtros.PretoEBranco()
      filtro_PretoEBranco_aplicado = pretoEBranco_filtro.aplicar_filtro(minha_imagem)
      nome1 = nome + "_preto_e_branco" + extencao
      filtro_PretoEBranco_aplicado.save(nome1)
      print(f'Filtro Preto e Branco aplicado com sucesso!\n')
    except Exception as ex:
      print(f"Erro ao aplicar filtro Preto e Branco: {str(ex)}")

  def aplica_filtro_cartoon (self, minha_imagem, nome, extencao):
    try:
      cartoon_filtro = filtros.Cartoon()
      filtro_Cartoon_aplicado = cartoon_filtro.aplicar_filtro(minha_imagem)
      nome1 = nome +  "_cartoon" + extencao
      filtro_Cartoon_aplicado.save(nome1)
      print(f'Filtro Cartoon aplicado com sucesso!\n')
    except Exception as ex:
      print(f"Erro ao aplicar filtro Cartoon: {str(ex)}")

  def aplica_filtro_negativo (self, minha_imagem, nome, extencao):
    try:
      negativo_filtro = filtros.Negativo()
      filtro_Negativo_aplicado = negativo_filtro.aplicar_filtro(minha_imagem)
      nome1 = nome + "_negativo" + extencao
      filtro_Negativo_aplicado.save(nome1)
      print(f'Filtro Negativo aplicado com sucesso!')
    except Exception as ex:
      print(f"Erro ao aplicar filtro Negativo: {str(ex)}")
      

  def aplica_filtro_contorno (self, minha_imagem, nome, extencao):
    try:
      contorno_filtro = filtros.Contorno()
      filtro_Contorno_aplicado = contorno_filtro.aplicar_filtro(minha_imagem)
      nome1 = nome + "_contorno" + extencao
      filtro_Contorno_aplicado.save(nome1)
      print(f'Filtro Contorno aplicado com sucesso!')
    except Exception as ex:
      print(f"Erro ao aplicar filtro Contorno: {str(ex)}")

  def aplica_filtro_blurred (self, minha_imagem, nome, extencao):
    try:
      blurred_filtro = filtros.Blurred()
      filtro_Blurred_aplicado = blurred_filtro.aplicar_filtro(minha_imagem)
      nome1 = nome + "_blurred" + extencao
      filtro_Blurred_aplicado.save(nome1)
      print(f'Filtro Blurred aplicado com sucesso!')
    except Exception as ex:
      print(f"Erro ao aplicar filtro Blurred: {str(ex)}")
    
  def listar_conteudo(self):
    diretorio = "."
    files = os.listdir(diretorio)
    jpeg_files = [file for file in files if file.lower().endswith(".jpeg") or file.lower().endswith(".jpg")]
    png_files = [file for file in files if file.lower().endswith(".png")]
    lista_imagens = jpeg_files + png_files
    return lista_imagens