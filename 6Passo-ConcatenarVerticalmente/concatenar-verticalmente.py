"""
Propósito: concatenar verticalmente as imagens em ordem crescente
Autor original: Alexandre Nassar de Peder
Atualizado para o padrão de páginas inteiras
"""

from PIL import Image
import os
import re

pasta_imagens = "inteiras"  # Alterado para a pasta correta mostrada no ls
pasta_saida = "."
os.makedirs(pasta_saida, exist_ok=True)

# Função para extrair o número da página e ordenar numericamente de forma crescente
def get_sort_key(nome_arquivo):
    # Extrai apenas o número da página antes de .png
    numero = int(re.search(r'(\d+)', nome_arquivo).group(1))
    return numero

# Pegar e ordenar as imagens corretamente em ordem crescente
arquivos = [f for f in os.listdir(pasta_imagens) if f.endswith('.png')]
arquivos.sort(key=get_sort_key)

# Abrir todas as imagens na ordem correta
imagens = []
for arquivo in arquivos:
    caminho = os.path.join(pasta_imagens, arquivo)
    imagens.append(Image.open(caminho))
    print(f"Adicionando: {arquivo}")  # Para verificar a ordem

# Encontrar a largura máxima
largura_max = max(img.width for img in imagens)

# Concatenar verticalmente
altura_total = sum(img.height for img in imagens)
imagem_final = Image.new('RGB', (largura_max, altura_total))

y = 0
for img in imagens:
    imagem_final.paste(img, (0, y))
    y += img.height

# Salvar
imagem_final.save(os.path.join(pasta_saida, 'colunas_concatenadas_verticalmente.png'))
print("Imagens concatenadas na ordem correta!")
print(f"Ordem dos arquivos: {arquivos}")