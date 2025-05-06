# Objetivo:
# Este script conecta-se ao Ollama localmente para gerar embeddings de múltiplos textos,
# usando o modelo "nomic-embed-text". Ele percorre uma lista de frases, envia cada uma
# para o servidor do Ollama e armazena os vetores gerados em um dicionário estruturado.
# No final, exibe o tamanho e os primeiros valores de cada vetor.

import requests
import json

# Lista de textos para gerar embeddings
textos = [
    "Ollama é uma ferramenta poderosa para executar modelos localmente.",
    "A inteligência artificial está transformando o mundo.",
    "Python é uma linguagem popular para ciência, análise e engenharia de dados.",
    "O futuro da computação envolve modelos cada vez mais eficientes. Devemos aprender a usá-los!!!",
]

# URL da API local do Ollama
url = "http://localhost:11434/api/embeddings"

# Dicionário para armazenar os resultados
resultados = {}

# Loop pelos textos
for i, texto in enumerate(textos, 1):
    print(f"\n🔹 Gerando embedding para a frase {i}: \"{texto}\"")

    # Envio da requisição ao Ollama com o modelo correto
    resposta = requests.post(
        url,
        json={
            "model": "nomic-embed-text",
            "prompt": texto
        }
    )

    # Verifica se a requisição foi bem-sucedida
    if resposta.status_code == 200:
        dados = resposta.json()
        vetor = dados["embedding"]

        # Armazena no dicionário com a frase como chave
        resultados[texto] = vetor

        # Exibe informações resumidas
        print(f"✅ Vetor gerado com {len(vetor)} dimensões.")
        print(f"📌 Primeiros 8 valores: {vetor[:8]}")
    else:
        print(f"❌ Erro ao gerar embedding: {resposta.status_code} - {resposta.text}")

# Finalização
print("\n✅ Todos os embeddings foram gerados com sucesso.")
