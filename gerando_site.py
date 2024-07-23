import os
import yaml

def update_mkdocs_yml():
    # Caminho do arquivo mkdocs.yml
    print('Iniciando atualização do mkdocs.yml')
    # Caminho do arquivo mkdocs.yml
    mkdocs_yml_path = 'mkdocs.yml'

    # Diretório onde estão os arquivos .md gerados
    docs_dir = 'docs'

    # Carregar o conteúdo atual do mkdocs.yml
    with open(mkdocs_yml_path, 'r', encoding='utf-8') as file:
        mkdocs_content = yaml.safe_load(file)

    # Listar todos os arquivos .md no diretório docs
    md_files = [f for f in os.listdir(docs_dir) if f.endswith('.md')]

    # Filtrar arquivos que começam com 'tabela_'
    tabela_md_files = [f for f in md_files if f.startswith('tabela_')]

    # Atualizar a navegação
    nav = mkdocs_content.get('nav', [])

    # Encontrar a entrada 'Tabelas' no nav, se existir
    tabelas_nav = next((item for item in nav if 'Tabelas' in item), None)
    if tabelas_nav:
        # Atualizar a lista de arquivos .md
        tabelas_nav['Tabelas'] = tabela_md_files
    else:
        # Adicionar uma nova entrada para 'Tabelas'
        nav.append({'Tabelas': tabela_md_files})

    # Atualizar o conteúdo do mkdocs_content
    mkdocs_content['nav'] = nav

    # Escrever o conteúdo atualizado de volta para mkdocs.yml
    with open(mkdocs_yml_path, 'w', encoding='utf-8') as file:
        yaml.dump(mkdocs_content, file, default_flow_style=False, allow_unicode=True)

    print('mkdocs.yml atualizado com sucesso!')


