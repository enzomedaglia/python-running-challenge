Python - Programa 2 (Tratamento básico de strings)

1) Vocês devem usar o material relativo a listas, strings e introdução a arquivos que estão na subseção "Strings / Listas / Funções e Arquivos"

2) Os dados contidos em "corrida-2023.gpx" consistem em dados capturados por um dispositivo móvel que registra coordenadas de latitude e longitute, informação de altitude e marca de tempo (time stamp) adquiridas por GPS durante um treino de corrida. Os dados são em formato de texto (representação de caracteres, que pode ser visto em um editor de textos).

Os dados, dispostos em linhas, estão identificados em "tags" (identificadores) denominados de trackpoints (pontos de coleta de informação), como exemplificado a seguir:
<trkpt lat="-30.0763177" lon="-51.1977167">
<ele>65.99767303466797</ele>
<time>2021-09-24T20:01:22Z</time>
</trkpt>

Onde "lat" e "lon" são dados de latitude e longitude em graus com fração decimal (não utliza a representação grau-minutos e segundos em separado).
A altitude ("ele") está expressa em metros, em relação ao nível do mar.

O registro de tempo contém a data e a hora expresso no meridiano zero (tempo Zulu ou GMT0).

O final de cada identificador é sinalizado com "/tag" entre os sinais de maior e menor. Por exemplo, cada identificador de tempo inicia com <time> e termina com </time>

A corrida é feita em várias etapas. Cada etapa está registrada em um "track segment" identificado pela tag <trkseg> (e finalizado pela tag </trkseg>)

(Sugestão: Visualize o conteúdo em um editor de texto comum para compreender a estrutura do arquivo).

3) A tarefa consiste em, a partir dos dados presentes em "corrida-2023.gpx":

3.1) Abrir o arquivo e colocar os dados em um string

3.1) Determinar o tempo total do percurso da segunda etapa da corrida (segundo <track segment) em mm:ss (minutos:segundos) e em hh,hhh (hora em formato decimal)

3.2) Informar o número total de trackpoints registrados no segmento analizado.

3.3) A diferença absoluta (sem sinal) da latitude e da longitude entre o primeiro e o último trackpoint da etapa.

O tratamento dos dados se dá através da procura dos tags específicos, usando propriedades dos trings, comparações de textos, conversão de tipos (string, inteiros e ponto flutuante) e comandos de iteração (por exemplo, veja as propriedades split, find e rfind e utilize os comandos for e/ou while)

Nota: Existem bibliotecas específicas para tratamento de arquivos xml (extensible markup language, que é o caso do gpx) e de bibliotecas de tratamento de arquivos gpx. Além de levar tempo para aprender a utilizá-las para um tratamento específico, estas bibliotecas não devem ser utilizadas neste exercício.

Coloque comentários no programa.py. Nos primeiros comentários indique todos os pacotes que deverão ser importados para o correto funcionamento do programa.

O prazo de entrega é até 04/12, mas pode ser entregue a qualquer momento.
