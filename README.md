# Projeto Final Labs - Manipulação de Imagem em Python
O programa oferece a possibilidade de aplicar diferentes filtros na imagem selecionada.

Os filtros disponíveis são: Escala de Cinza, Preto e Branco, Filtro Cartoon, Modo Foto Negativa (inversão das cores da imagem), Modo Contorno e Modo Blurred. 

Para cada filtro aplicado, será gerada uma imagem resultante que será salva no diretório atual do programa.

### Classe Imagem:
Representa um arquivo de imagem, podendo ser .jpg ou .png.

### Classe Download:
Responsável por fazer o download dos arquivos de imagem.

### Classe Filtros:
Cada filtro disponível possui sua própria classe correspondente.
Essas classes contêm métodos para aplicar o filtro na imagem original e retornar a imagem filtrada.

### Classe Principal:

Representa o programa principal que faz a integração e coordena todas as classes. Essa classe exibe um menu interativo para o usuário com as seguintes opções:

1. Informar o caminho da imagem: Permite ao usuário inserir o caminho para a imagem de forma que o programa diferencie entre uma imagem local e uma imagem pública da Internet.

2. Escolher o filtro a ser aplicado: Permite ao usuário selecionar um dos filtros disponíveis.

3. Listar arquivos de imagens do diretório corrente: Apresenta uma lista dos arquivos de imagens (com extensão .jpg ou .png) encontrados no diretório atual.

4. SAIR: Encerra a execução do programa.