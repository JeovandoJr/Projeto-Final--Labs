from PIL import Image
import requests
import os

#Classe para fazer o Download da Imagem
class Download:
    def __init__(self, url, destino_arquivo):
        self.url = url
        self.destino_arquivo= destino_arquivo

    def download_file(self):
        try:
            resposta = requests.get(self.url)
            resposta.raise_for_status() #Verifica se houve algum erro na requisição

            with open(destino_arquivo, "wb") as file:
                file.write(resposta.content)
            
            print(f"Download Completo. Arquivo Salvo Em : {self.destino_arquivo}")
        
        except requests.exceptions.MissingSchema:
            print("URL Inválida. Certifique-se de fornecer uma URL válida.")

        except requests.exceptions.RequestException as e:
            print(f"Erro na Conexão: {e}")
        

