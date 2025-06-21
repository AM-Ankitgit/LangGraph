from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(path="/LangChain",
                         glob=["*.pdf"],
                         loader_cls=PyPDFLoader)

doc = loader.lazy_load()

