from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

path = Path("F:\study\LangGraph_LangChain\paper.pdf")
loader = PyPDFLoader(path)

doc = loader.load()

print(len(doc))
print(doc[0].page_content)
print(doc[0].metadata)

# total 649 page 