import os
from datetime import datetime
import re


def ler_arquivo_gpx(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados_gpx = arquivo.read()
        return dados_gpx
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None


def tempo_total_segunda_etapa(dados_gpx):
    # Encontrar a posição inicial e final da segunda etapa
    inicio_segunda_etapa = dados_gpx.find("<trkseg>", dados_gpx.find("<trkseg>") + 1)
    fim_segunda_etapa = dados_gpx.find("</trkseg>", inicio_segunda_etapa)

    # Extrair a parte da string correspondente à segunda etapa
    segunda_etapa_str = dados_gpx[inicio_segunda_etapa:fim_segunda_etapa]

    # Inicializar variáveis para o tempo total em segundos
    tempo_total_segundos = 0

    # Encontrar todos os pontos de tempo dentro da segunda etapa
    pontos_tempo = segunda_etapa_str.split("<time>")
    for ponto_tempo in pontos_tempo[1:]:  # Ignorar o primeiro elemento vazio
        # Extrair a data e hora, remover a tag e o sufixo
        tempo_str = ponto_tempo.split("</time>")[0]

        # Converter o tempo para um objeto datetime
        tempo = datetime.strptime(tempo_str, "%Y-%m-%dT%H:%M:%SZ")

        # Calcular o tempo total em segundos
        tempo_total_segundos += tempo.hour * 3600 + tempo.minute * 60 + tempo.second

    # Converter o tempo total para minutos e horas
    tempo_total_minutos = tempo_total_segundos // 60
    tempo_total_horas = tempo_total_segundos / 3600

    # Retornar o tempo total em formato mm:ss e hh,hhh
    return f"{tempo_total_minutos:02}:{tempo_total_segundos % 60:02}", f"{tempo_total_horas:.3f}"


def diferenca_absoluta_latitude_longitude(dados_gpx):
    # Encontrar a posição inicial e final da segunda etapa
    inicio_segunda_etapa = dados_gpx.find("<trkseg>", dados_gpx.find("<trkseg>") + 1)
    fim_segunda_etapa = dados_gpx.find("</trkseg>", inicio_segunda_etapa)

    # Extrair a parte da string correspondente à segunda etapa
    segunda_etapa_str = dados_gpx[inicio_segunda_etapa:fim_segunda_etapa]

    # Encontrar as coordenadas dos primeiros e últimos trackpoints
    primeiro_trackpoint = segunda_etapa_str.find("<trkpt")
    ultimo_trackpoint = segunda_etapa_str.rfind("<trkpt")

    # Extrair as latitudes e longitudes dos primeiros e últimos trackpoints
    latitudes = re.findall(r'lat="(-?\d+\.\d+)"', segunda_etapa_str[primeiro_trackpoint:ultimo_trackpoint + 8])
    longitudes = re.findall(r'lon="(-?\d+\.\d+)"', segunda_etapa_str[primeiro_trackpoint:ultimo_trackpoint + 8])

    # Calcular a diferença absoluta entre a primeira e a última latitude e longitude
    diferenca_latitude = abs(float(latitudes[-1]) - float(latitudes[0]))
    diferenca_longitude = abs(float(longitudes[-1]) - float(longitudes[0]))

    return diferenca_latitude, diferenca_longitude


# Bonus
def calcular_ganho_elevacao(dados_gpx):
    try:
        # Encontrar todas as ocorrências da tag <ele>
        elevacoes_str = re.findall(r'<ele>(.*?)</ele>', dados_gpx)

        # Converter as elevações para floats
        elevacoes = [float(ele) for ele in elevacoes_str]

        # Inicializar variáveis
        ganho_elevacao = 0
        elevacao_anterior = elevacoes[0]

        # Calcular o ganho de elevação
        for elevacao in elevacoes[1:]:
            diferenca_elevacao = elevacao - elevacao_anterior
            if diferenca_elevacao > 0:
                ganho_elevacao += diferenca_elevacao
            elevacao_anterior = elevacao

        return ganho_elevacao
    except Exception as e:
        print(f"Ocorreu um erro ao calcular o ganho de elevação: {e}")
        return None


if __name__ == "__main__":
    print("Question 3.1:")
    print("Loading Data:")
    # Chamar a função para ler os dados do arquivo GPX
    nome_arquivo_gpx = "corrida-2023.xml"  # "caminho/do/seu/arquivo/corrida-2023.gpx"
    dados_gpx = ler_arquivo_gpx(nome_arquivo_gpx)

    # Verificar se os dados foram lidos com sucesso
    if dados_gpx is not None:
        print("Dados do arquivo GPX:")
        print(dados_gpx[:500])  # Exibindo os primeiros 500 caracteres como exemplo

    print("\nQuestion 3.2:")
    # Chamar a função com os dados do arquivo GPX
    tempo_mmss, tempo_hhhh = tempo_total_segunda_etapa(dados_gpx)

    # Exibir resultados
    print("Tempo total da segunda etapa em mm:ss:", tempo_mmss)
    print("Tempo total da segunda etapa em hh,hhh:", tempo_hhhh)

    print("\nQuestion 3.3:")

    # Chamar a função com os dados do arquivo GPX
    diferenca_lat, diferenca_lon = diferenca_absoluta_latitude_longitude(dados_gpx)

    # Exibir o resultado
    print("Diferença absoluta da latitude:", diferenca_lat)
    print("Diferença absoluta da longitude:", diferenca_lon)

    # Bonus
    print('\nBonus Questions:')
    # Chamar a função para calcular o ganho de elevação
    ganho_elevacao = calcular_ganho_elevacao(dados_gpx)

    # Verificar se o ganho de elevação foi calculado com sucesso
    if ganho_elevacao is not None:
        print(f"Ganho de elevação total: {ganho_elevacao} metros")
