from langchain_community.document_loaders import WebBaseLoader
url = "https://github.com/campusx-official/langchain-document-loaders/blob/main/webbase_loader.py"
doc = WebBaseLoader(url)