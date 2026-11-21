---
dataset_info:
  features:
  - name: odiNumber
    dtype: int64
  - name: dateComplaintFiled
    dtype: string
  - name: components
    dtype: string
  - name: summary
    dtype: string
  - name: label
    dtype: string
  splits:
  - name: train
    num_bytes: 4486274
    num_examples: 8356
  - name: eval
    num_bytes: 1121179
    num_examples: 2089
  - name: test
    num_bytes: 817523
    num_examples: 2089
  download_size: 3314443
  dataset_size: 6424976
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: eval
    path: data/eval-*
  - split: test
    path: data/test-*
license: apache-2.0
task_categories:
- text-classification
language:
- en
tags:
- veicular
- complaints
pretty_name: NHTSA Complaints Dataset
---

# NHTSA Complaints Dataset

Este dataset contém reclamações de veículos coletadas pela **National Highway Traffic Safety Administration (NHTSA)** entre 2014 e 2024. O objetivo do dataset é classificar o tipo de componente veicular relatado nas reclamações. O dataset foi criado para ser utilizado em tarefas de classificação de texto, com foco em Processamento de Linguagem Natural (NLP) e Machine Learning.

## Tarefa

Classificação de texto: O conjunto de dados consiste em uma abordagem multiclasse de reclamações de diferentes categorias de componentes veiculares. As categorias são:

- **ELECTRICAL SYSTEM**
- **AIR BAGS**
- **STRUCTURE**
- **SERVICE BRAKES**
- **OTHER** (categoria usada para outras classes menos frequentes ou classes combinadas)

## Descrição dos Dados

O dataset contém informações sobre as reclamações de veículos, incluindo o tipo de problema relatado, a marca e modelo do veículo, e outras informações relacionadas. Os dados foram adquiridos diretamente da API oficial da **NHTSA**, que são fornecidos em formato JSON.

### Arquivos

- `train.csv`: Conjunto de treinamento (8.357 amostras)
- `eval.csv`: Conjunto de validação (2.090 amostras)
- `test.csv`: Conjunto de teste (2.090 amostras)

### Estrutura do Arquivo

Cada arquivo contém as seguintes colunas:

- **odiNumber**: Número da reclamação
- **dateComplaintFiled**: Data em que a reclamação foi registrada
- **components**: Categoria de componente relacionado à reclamação (anotação fraca).
- **summary**: Descrição resumida da reclamação
- **label**: Categoria de componente relacionado à reclamação (anotação utilizada).

## Aquisição dos Dados

Os dados foram adquiridos diretamente da API da **NHTSA**. A coleta foi realizada em várias etapas:

1. Obtenção dos **anos de modelo**.
2. Obtenção das **marcas de veículos** por ano.
3. Obtenção dos **modelos de veículos** por marca e ano.
4. Obtenção das **reclamações** registradas para cada veículo.

Os dados foram armazenados em arquivos JSON e, posteriormente, processados e salvos em arquivos CSV.

## Processamento e Limpeza de Dados

O dataset passou por um processo de limpeza, que incluiu:

1. **Filtragem de Dados**: Apenas as colunas relevantes foram mantidas.
2. **Conversão de Datas**: A coluna `dateComplaintFiled` foi convertida para o formato datetime.
3. **Remoção de Dados Duplicados e Nulos**: Reclamações sem descrição ou sem categoria foram descartadas.
4. **Balanceamento de Classes**: Técnicas de balanceamento foram aplicadas para garantir uma distribuição uniforme das classes no conjunto de treinamento.
5. **Limpeza de Texto**: Remoção de caracteres especiais, normalização de texto e conversão para caixa baixa.

Os dados foram divididos em três conjuntos: **treinamento**, **validação** e **teste**, com as seguintes distribuições de classe:

| Conjunto de Dados  | ELECTRICAL SYSTEM | AIR BAGS | STRUCTURE | SERVICE BRAKES | OTHER |
|--------------------|-------------------|----------|-----------|----------------|-------|
| **train.csv**      | 1.672             | 1.671    | 1.671     | 1.671          | 1.671 |
| **eval.csv**       | 417               | 418      | 418       | 418            | 418   |
| **test.csv**       | 159               | 99       | 113       | 17             | 1.701 |

## Como Usar

### Exemplo de Código para Carregar o Dataset

```python
from datasets import load_dataset

# Carregar o dataset
dataset = load_dataset("vic35get/nhtsa_complaints_dataset")

# Visualizar os dados de treinamento
print(dataset["train"][0])
