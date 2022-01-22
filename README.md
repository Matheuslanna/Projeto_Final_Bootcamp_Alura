# Prevendo a necessidade de internação para pacientes com COVID-19
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=flat-square&logo=Jupyter)](https://jupyter.org/try) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg?style=flat-square)](https://github.com/PedroHCAlmeida/analise_temporal_COVID_Brasil/edit/main/LICENSE)

![Alt](https://github.com/Matheuslanna/Projeto_Final_Bootcamp_Alura/blob/main/Imagens/banner.png?raw=true)

# Sumário
<!--ts-->
   * [Resumo](#res)
   * [Contexto](#cont)
   * [Estrutura do projeto](#estru)
   * [Modelos](#model)
   * [Bibliotecas utilizadas](#bibli)
   * [Referências](#ref)
   <!--te-->
   
<a name="res"></a>
# Resumo

O projeto teve como objetivo criar modelos de previsão da necessidade de um paciente recém admitido de ser internado ou não na UTI em decorrência de COVID-19. O modelo usará dados obtidos nas duas primeiras horas desde a admissão do paciente, disponilizados no [kaggle](https://www.kaggle.com/S%C3%ADrio-Libanes/covid19) pelo Hospital Sírio-Libanês.

O modelo criado ajudaria a melhorar a logística do hospital em disponibilizar os recursos com base no grau de gravidade da doença, de modo a evitar o colapso do sistema com o aumento de casos.

<a name="cont"></a>
# Contexto

No início de 2020 o mundo foi tomado por uma das maiores crises sanitárias da humanidade, a pandemia de COVID-19, que levou a um rápido contágio de parte da população mundial e a um colapso do sistema hospitalar, onde as hospitais não tinham a capacidade suficiente para atender todos aqueles que precisavam. 

A partir da necessidade de otimizar os recursos hospitalares para aqueles que necessitavam, iremos tentar criar um modelo preditor a partir de resultados de exames do paciente como exames de sangue, grupos de doença, faixa etária, sinais vitais e outros dados dos pacientes, de modo a prever a necessidade de leito de UTI antes de possíveis complicações da doença.


<a name="estru"></a>
# Estrutura do projeto

## [dados](https://github.com/Matheuslanna/Projeto_Final_Bootcamp_Alura/tree/main/Dados):

Diretório com os dados utilizados no projeto, divididos em dados brutos e dados limpos:

* [dados_brutos](https://github.com/Matheuslanna/Projeto_Final_Bootcamp_Alura/tree/main/Dados/Dados_brutos) : arquivo .xlsx original disponibilizado pelo Hospital Sírio-Libanês no Kaggle;
* [dados_limpos](https://github.com/Matheuslanna/Projeto_Final_Bootcamp_Alura/tree/main/Dados/Dados_limpos) : aquivo .csv com os dados pré-processados.

## [funcoes](https://github.com/Matheuslanna/Projeto_Final_Bootcamp_Alura/tree/main/Funcoes):

Este diretório foi destinado as funções utilizadas no projeto, essas foram divididas em 4 arquivos .py dependendo do objetivo das mesmas, são eles:

* [pre_processamento](https://github.com/Matheuslanna/Projeto_Final_Bootcamp_Alura/tree/main/Funcoes/pre_processamento.py) : funções usadas no pré-processamento dos dados;
* [feature](https://github.com/Matheuslanna/Projeto_Final_Bootcamp_Alura/tree/main/Funcoes/features.py) : funções usadas na feature selection;
* [func_plot](https://github.com/Matheuslanna/Projeto_Final_Bootcamp_Alura/tree/main/Funcoes/func_plot.py) : funções usadas na geração de gráficos;
* [func_classifier](https://github.com/Matheuslanna/Projeto_Final_Bootcamp_Alura/tree/main/Funcoes/func_classifier.py) : classe usada na criação dos modelos de ML.

## [notebooks](https://github.com/Matheuslanna/Projeto_Final_Bootcamp_Alura/tree/main/Notebooks):

Pasta com os notebooks utilizados para a análise explatória dos dados e criação dos modelos de ML.

* [Analise_Exploratoria](https://github.com/Matheuslanna/Projeto_Final_Bootcamp_Alura/blob/main/Notebooks/Analise_Exploratoria.ipynb): notebook desenvolvido no jupyter lab onde foi realizado o pré-processamento dos dados brutos e toda a parte de Análise exploratória.
* [Modelos](https://github.com/Matheuslanna/Projeto_Final_Bootcamp_Alura/blob/main/notebooks/Modelos.ipynb) : notebook destinado aos modelos de Machine Learning a partir dos dados pré-processados

<a name="model"></a>
# Modelos 

Após realizar o pré-processamento dos dados e a análise exploratória, foram testados diferentes modelos de Machine Learning, foram eles:

|Modelo                 |Pacote              |Método
|:----------------------|:-------------------|-----------|
|LogisticRegression     |sklearn.linear_model|Regressão Logística
|DecisionTreeClassifier |sklearn.tree        |Árvore de decisão
|RandomForestClassifier |sklearn.ensemble    |Ensemble
|ExtraTreesClassifier   |sklearn.ensemble    |Ensemble

A partir dos modelos testados, foram selecionados os dois com as melhores métricas para a otimização de hyperparâmetros de modo a melhor o modelo.

Os resultados obtidos do modelo final foram:

Métrica   |Média
:---------|----------:
ROC AUC   | **0.936**
ACURÁCIA  | **0.850**
PRECISÃO  | **0.852**
F1-SCORE  | **0.850**
RECALL    | **0.849**

<a name="bibli"></a>
# Bibliotecas utilizadas

Esse projeto foi realizado utilizando a linguagem Python versão 3.9.6, e os notebooks foram desenvolvidos através da ferramenta jupyter lab dentro de um ambiente criado pela plataforma anaconda, as principais bibliotecas usadas foram:
* Pandas versão 1.3.5
* Matplotlib versão 3.5.0
* Seaborn versão 0.11.2
* Numpy versão 1.22.0
* Scikit-learn versão 1.0.2

<a name="ref"></a>
# Referências

https://pandas.pydata.org/docs/index.html<br>
https://numpy.org/doc/stable/index.html<br>
https://matplotlib.org/<br>
https://seaborn.pydata.org/<br>
https://scikit-learn.org/stable/index.html<br>
https://www.kaggle.com/S%C3%ADrio-Libanes/covid19/code?datasetId=605991&language=Python<br>
