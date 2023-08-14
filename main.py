import entidades
import filtros
import utilidades
import os

class Principal:
    def menu(self):
        print("---------------- MENU ----------------")
        print("1. Informar o caminho da imagem")
        print("2. Aplicar filtro na imagem")
        print("3. Listar arquivos de imagem do diretório atual")
        print("4. Sair")

    def menu_filtros(self):
        print("\nEscolha um filtro para ser aplicado:")
        print("1. Escala de Cinza")
        print("2. Preto e Branco")
        print("3. Cartoon")
        print("4. Negativo")
        print("5. Contorno")
        print("6. Blurred")

    def excutar(self):
        utilidades1 = utilidades.Util()
        app_principal = utilidades.Main(utilidades1)

        while True:
            escolhas = Principal()
            escolhas.menu()
            
            opcao = int(input("Selecione uma opção(1-4): "))

            if opcao == 1:
                caminho_imagem = input("\nInforme o caminho da imagem: ")
                nome_imagem = input("Informe o nome da imagem: ")

                imagem1 = app_principal.cria_imagem(caminho_imagem)
                
                nome_original, extencao = os.path.splitext(os.path.basename(caminho_imagem))
                
                
            
            elif opcao == 2:
                if imagem1:
                    escolhas_filtros = Principal()
                    escolhas_filtros.menu_filtros()
                    opcao_filtro = int(input("Selecione um filtro (1-6): "))

                    if opcao_filtro == 1:
                        app_principal.aplica_filtro_escala_de_cinza(imagem1, nome_imagem, extencao)
                    elif opcao_filtro == 2:
                        app_principal.aplica_filtro_preto_e_branco(imagem1, nome_imagem, extencao)
                    elif opcao_filtro == 3:
                        app_principal.aplica_filtro_cartoon(imagem1, nome_imagem, extencao)
                    elif opcao_filtro == 4:
                        app_principal.aplica_filtro_negativo(imagem1, nome_imagem, extencao)
                    elif opcao_filtro == 5:
                        app_principal.aplica_filtro_contorno(imagem1, nome_imagem, extencao)
                    elif opcao_filtro == 6:
                        app_principal.aplica_filtro_blurred(imagem1, nome_imagem, extencao)
                    else:
                        print("Opção Inválida.")
                else:
                    print("Irfome o caminho da imagem antes de escolher o filtro.")
            
            elif opcao == 3:
                for elemento in app_principal.listar_conteudo():
                    print(elemento)
            elif opcao == 4:
                print("Programa Encerrado.")
                break
            else:
                print("Opção Inválida.")

aplicacao = Principal()
aplicacao.excutar()
 