# script para nomear as imagens do dataset de ônibus de brinquedo de forma padrão

import os

diretorio = r"C:\Users\mmart\Documents\ic\Repositorio\src\data\dataset_toy_bus"
prefixo = "bus"
extensao = ".jpg" 

arquivos = [f for f in os.listdir(diretorio) if f.lower().endswith(extensao)]

arquivos.sort()

for i, nome_original in enumerate(arquivos, start=1):
    novo_nome = f"{prefixo}_{i:03d}{extensao}"
    caminho_antigo = os.path.join(diretorio, nome_original)
    caminho_novo = os.path.join(diretorio, novo_nome)
    os.rename(caminho_antigo, caminho_novo)

