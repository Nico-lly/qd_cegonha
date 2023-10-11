# 3° ciclo QD nas Universidades - Visualização da Rede Cegonha

## Sumário da documentação
1. [Contextualização do projeto](#contextualizacao)
2. [Bibliotecas importantes](#bibliotecas)
3. [Entenda este repositório](#entenda)

**- Contextualização do projeto**

<a name="contextualizacao"></a> 
Formalizada pelas Portarias n° 1.459 e 650 de 2011, a Rede Cegonha visou o repasse de recursos no intuito de criar mais Centros de Parto Normal e Casas de Gestantes, Bebês e Puérperas, a ampliação de exames pré-natal e doenças sexualmente transmissíveis visando diminuir as taxas de mortalidade materno-infantil nos municípios. Além de indicadores como mortalidade e cobertura vacinal, não há como mensurar a dimensão da adesão dos municípios a esse plano. O processamento de linguagem natural em textos de diários oficiais pode ser uma técnica promissora para ser usado conjuntamente a esses indicadores já consolidados na literatura de avaliação de políticas de saúde materno-infantil, especialmente para os municípios que são heterogêneos.  Nesse sentido, o estudo tem como objetivo comparar as técnicas de pré-processamento de linguagem natural (tokenização, stemming, taxonomia, remoção de stopwords, cortes de palavra baseado em frequência, N-grama, TF-IDF, bag-of-words, suavização e normalização) na extração de entidades nomeadas de diários oficiais dos municípios que possuem instituições incluídas na Rede Cegonha entre os anos de 2011 e 2021 (anos em que o Rede Cegonha teve vigência). Atualmente a Rede Cegonha está sendo substituída pela RAMI.

**- Algumas bibliotecas úteis para o projeto:**
<a name="bibliotecas"></a>

**[Bertopic](https://maartengr.github.io/BERTopic/getting_started/quickstart/quickstart.html)**, é uma biblioteca que podemos utilizar para fazer modelagem de tópicos utilizando língua portuguesa. Teve bons resultados no trabalho realizado pela UNIT.

**[Scrapy](https://docs.scrapy.org/en/latest/topics/spiders.html)** é uma biblioteca que permite extrair informações de websites. Alguns comandos básicos:

**[NLTK](https://www.nltk.org)** é uma plataforma para trabalhar com linguagem natural. É uma API robusta na qual é necessário acessar os [subpacotes](https://www.nltk.org/api/nltk.html) de sua estrutura para trabalhar com as diversas funcionalidades, tais como modelos de linguagem, pré-processamento, análise de sentimento, entre outros.

**[SpaCy](https://spacy.io/usage/spacy-101)** é uma biblioteca _open-source_ para trabalhar com Processamento de Linguagem Natural (PLN). Na documentação, é possível aprender sobre as _features_ do pacote, tais como pré-processamento de textos, modelos estatísticos incorporados, reconhecimento de entidades, entre outros.

O _corpus_, frequentemente mencionado no PLN, é uma coletânea de textos, sendo estes frequentemente o conjunto de dados linguístico em que será realizada a análise. Os pacotes que utilizam artifício da PLN possuem a capacidade de ler esse conjunto de dados e tranformá-los em _corpus_ que são possíveis de serem interpretados pela linguagem da máquina.

**_Alguns outros pacotes_**

**[Pandas](https://pandas.pydata.org/)**

### Entenda este repositório
<a name="entenda"></a>

Este projeto é fruto da iniciativa da [**Open Knowledge Brasil**](https://ok.org.br) com o lançamento da chamada de voluntários para trabalhar no âmbito do [Querido Diário nas Universidades](https://ok.org.br/noticia/querido-diario-nas-universidades/).

### Como utilizar este repositório

~~~Terminal
pip3 install requirements.txt
~~~

### Resultados
- [1° artigo]()
