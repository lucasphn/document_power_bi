# Geração Automática de Documentação do Power BI

Este projeto tem como objetivo gerar uma documentação completa do Power BI de forma automática. A documentação gerada inclui medidas, tabelas e relacionamentos do projeto, proporcionando uma visão clara e organizada da estrutura do Power BI.

## Passo-a-Passo para Configuração e Execução

### 1. Instalação do Ambiente Virtual

1. Clone o repositório para o seu ambiente local.
2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv env
    source env/bin/activate  # Para Linux/Mac
    .\env\Scripts\activate  # Para Windows
    ```

### 2. Instalação das Dependências

1. Instale as dependências necessárias a partir do arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### 3. Gerar Arquivo .xlsx do Projeto Power BI

1. Você pode assistir ao vídeo para gerar o arquivo `.xlsx` do seu projeto do Power BI:
    [Gerar Arquivo .xlsx](https://www.youtube.com/watch?v=aRMP5LYYJsw&t=1s)

2. Alternativamente, abra o projeto do Power BI no DAX Studio, copie o script DAX que está no arquivo `query_dax.txt` e execute-o. Salve o output da execução em um arquivo Excel e renomeie-o para `doc.xlsx`, colocando-o no diretório raiz do projeto.

### 4. Configuração do Arquivo `mkdocs.yml`

1. Edite o arquivo `mkdocs.yml` para que tenha a seguinte estrutura:
    ```yaml
    site_name: BI Contábil

    extra_css:
      - stylesheets/custom.css

    plugins:
      - search
      - mermaid2
      - mkdocstrings

    nav:
      - Home: index.md
      - Arquitetura:
        - medidas.md
        - relationship.md
      - Tabelas:
    ```

### 5. Execução do Script

1. Execute o script `main.py` para gerar a documentação:
    ```bash
    python main.py
    ```

## Documentação Gerada

A documentação gerada estará disponível em: [Documentação do Power BI](https://lucasphn.github.io/document_power_bi/tabela_d_contas_subgrupo_3/)

## Estrutura do Projeto

- `docs/`: Contém os arquivos `.md` gerados.

