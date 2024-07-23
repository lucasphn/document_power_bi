from gerando_docs import CriandoUmaDocumentacaoDoPowerBI
from gerando_site import update_mkdocs_yml



if __name__ == "__main__":
    main = CriandoUmaDocumentacaoDoPowerBI()
    main.run_pipeline()
    update_mkdocs_yml()