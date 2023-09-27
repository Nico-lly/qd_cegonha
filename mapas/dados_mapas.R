install.packages('raster')
install.packages('tmap')
install.packages('readr')
install.packages('datasus')
install.packages('tidyverse')
library(raster, tmap, readr, datasus, tidyverse)

install.packages("remotes")
remotes::install_github("curso-r/munifacil")

library(munifacil)
library(raster)
library(tmap)
library(readr)
library(datasus)
library(tidyr)
#https://smolski.github.io/livroavancado/producao-de-mapas.html

# Carregando o arquivo
meso <- shapefile("mesoregiao-ipeageo/mesoregiao.shp")

# Excluindo dados inconvenientes
MAPARS=MAPARS[MAPARS$CD_GEOCMU !="4300001" & MAPARS$CD_GEOCMU !="4300002",]

class(meso)
summary(meso)
head(meso@data)

plot(meso)

count_publicacoes <- readxl('../raw_data/count_cegonha.xlsx')
dados_meso <- readxl('regioes_geograficas-ibge.xlsx')
## Transformando em dados de mesorregiões

# ver quais são as colunas disponíveis
dplyr::glimpse(count_publicacoes)

# vamos limpar o nome das colunas
base_de_exemplo <- base_de_exemplo_bruta %>% 
  janitor::clean_names() %>%
  # buscar apenas linhas distintas segundo essas colunas
  dplyr::distinct(cidade_abrangida, codigo_do_ibge_cidade_abrangida, cidade_abrangida_uf)
dplyr::glimpse(base_de_exemplo)


#https://github.com/curso-r/munifacil
# Corrigindo o campo com o código do IBGE
names(RS2013)[3]="CD_GEOCMU" 
# Corrigindo os dados do código IBGE dos municípios
RS2013$CD_GEOCMU=substr(RS2013$CD_GEOCMU,1,6)
head(RS2013)

#Une a base de dados da planilha com o mapa pelo nome do município
RS2013MAPA=merge(MAPARS,RS2013,by="CD_GEOCMU", all.x=T) 
names(RS2013MAPA)
head(RS2013MAPA@data)


tm_shape(RS2013MAPA)+
  tm_fill("AREA_KM2", auto.palette.mapping=FALSE, 
          title="Área por município")+
  tm_format_Europe2()+
  tm_style_classic()+
  tm_legend(position=c("left","bottom"))+
  tm_compass()+
  tm_scale_bar()+
  tm_borders(alpha=.5)+
  tm_bubbles(size = 'PIB',col = '#b3de69', title.size='PIB') +
  tm_legend(legend.format = list(text.separator= "a"))

tm_shape(RS2013MAPA) +
  tm_polygons(c("PIB", "POPULACAO"), 
              style=c("kmeans","fixed"),
              palette=list("Reds", "Blues"),
              auto.palette.mapping=FALSE,
              breaks=list(quantile(RS2013MAPA$POPULACAO),
                          c(-Inf,100000,200000,Inf)),
              title=c("PIB", "População")) +
  tm_format_World() + 
  tm_style_grey()+
  tm_compass()+
  tm_scale_bar()+
  tm_legend(legend.format = list(text.separator= "a"))+
  tm_layout(legend.position = c("LEFT","BOTTOM"),
            legend.frame = FALSE, title = c("Mapa 1","Mapa 2"))

nascimentos=sinasc_nv_uf(uf = "rs",
                         periodo = c(2014:2016),
                         coluna = "Ano do nascimento")
head(nascimentos)

nascimentos=nascimentos[-1,]
nascimentos <- separate(nascimentos, `Município`, c("CD_GEOCMU", "NM_MUNICIP"), sep = 6)
head(nascimentos)

RS2013MAPAN=merge(RS2013MAPA,nascimentos,by="CD_GEOCMU", all.x=T) 
names(RS2013MAPAN)