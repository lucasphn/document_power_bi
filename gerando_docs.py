import os
import yaml
import pandas as pd
from tabulate import tabulate

class CriandoUmaDocumentacaoDoPowerBI():

    def __init__(self):
        # Source
        self.df = 'doc.xlsx'
        # Gerando dataframes
        try:
            self.df_medidas = pd.read_excel(self.df, sheet_name=0)
            self.df_tables = pd.read_excel(self.df, sheet_name=1)
            self.df_relationship = pd.read_excel(self.df, sheet_name=2)
        except Exception as e:
            print(f"Erro ao carregar os arquivos Excel: {e}")

    def run_pipeline(self):
        print("Iniciando geração de documentação")
        self.preparando_dataframe_medidas()
        self.preparando_dataframe_tables()
        self.preparando_dataframe_relationship()
        self.gerando_html()
        self.construindo_arquivo_md()
        self.fatiar_e_gerar_html_e_md_tables()
        print('Documentação Finalizada')

    def preparando_dataframe_medidas(self):
        # Retirando \n do html gerado
        self.df_medidas = self.df_medidas.replace('\n', ' ', regex=True)

        # Substituindo 'NaN' por nada 
        self.df_medidas = self.df_medidas.fillna('')

        return self.df_medidas

    def preparando_dataframe_tables(self):
        # Retirando \n do html gerado
        self.df_tables = self.df_tables.replace('\n', ' ', regex=True)

        # Substituindo 'NaN' por nada 
        self.df_tables = self.df_tables.fillna('') 

        # Retirando as tabelas temporárias de data geradas automaticamente pelo Power BI da documentação
        self.df_tables = self.df_tables[~self.df_tables['Tabela'].str.contains('DateTableTemplate', na=False)]
        self.df_tables = self.df_tables[~self.df_tables['Tabela'].str.contains('LocalDateTable', na=False)]

        # Omitindo colunas ocultas
        self.df_tables = self.df_tables[self.df_tables['Está Oculto?'] != True]

        # Retirando colunas pasta 
        self.df_tables = self.df_tables.drop(columns=['Pasta'])

        # Modificando formato 
        self.df_tables['Formato'] = self.df_tables['Formato'].replace('0', 'Int')

        return self.df_tables

    def preparando_dataframe_relationship(self):

        # Retirando as tabelas temporárias de data geradas automaticamente pelo Power BI da documentação
        self.df_relationship = self.df_relationship[~self.df_relationship['Para Tabela'].str.contains('DateTableTemplate', na=False)]
        self.df_relationship = self.df_relationship[~self.df_relationship['Para Tabela'].str.contains('LocalDateTable', na=False)]

        return self.df_relationship

    def fatiar_e_gerar_html_e_md_tables(self):
        # Obtendo os valores distintos na coluna 'Tabela'
        tabelas_distintas = self.df_tables['Tabela'].unique()

        # Iterando sobre cada valor distinto
        for tabela in tabelas_distintas:
            # Criando um dataframe específico para cada valor distinto na coluna 'Tabela'
            df_tabela_especifica = self.df_tables[self.df_tables['Tabela'] == tabela]

            # Gerando HTML para o dataframe específico
            html_tabela_especifica = df_tabela_especifica.to_html(index=False, classes='styled-table')

            # Estrutura do arquivo MD
            markdown_content_tabela_especifica = f'''
## Tabela: {tabela}
<div class="table-responsive">
{html_tabela_especifica}
</div>
            '''

            # Criando arquivo MD específico
            with open(f'docs/tabela_{tabela}.md', 'w', encoding='utf-8') as f:
                f.write(markdown_content_tabela_especifica)


    def gerando_html(self):
        # Gerando html
        self.html_medidas = self.df_medidas.to_html(index=False, classes='styled-table')
        self.html_tables = self.df_tables.to_html(index=False, classes='styled-table')
        self.html_relationship = self.df_relationship.to_html(index=False, classes='styled-table')

        return self.html_medidas, self.html_tables, self.html_relationship

    def construindo_arquivo_md(self):
        # Verifica se o diretório docs existe, se não, cria
        if not os.path.exists('docs'):
            os.makedirs('docs')

        # Estrutura arquivos MD
        # Para medidas
        self.markdown_content_medidas = f'''
## Medidas e Cálculos
<div class="table-responsive">
{self.html_medidas}
</div>
        '''

        # Para tabelas
        self.markdown_content_tables = f'''
## Dicionário de Dados
<div class="table-responsive">
{self.html_tables}
</div>
        '''

        # Para relacionamentos
        self.markdown_content_relationship = f'''
## Modelagem e Arquitetura de Dados
<div class="table-responsive">
{self.html_relationship}
</div>
        '''
        # Verifica se o diretório docs existe, se não, cria
        if not os.path.exists('docs'):
            os.makedirs('docs')

        # Criando arquivos MD
        with open('docs/medidas.md', 'w', encoding='utf-8') as f:
            f.write(self.markdown_content_medidas)

        with open('docs/tables.md', 'w', encoding='utf-8') as f:
            f.write(self.markdown_content_tables)

        with open('docs/relationship.md', 'w', encoding='utf-8') as f:
            f.write(self.markdown_content_relationship)



