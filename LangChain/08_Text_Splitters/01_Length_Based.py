


# When to Use
# Use CharacterTextSplitter when:

# You don't have well-structured text (e.g., no paragraphs or headings).

# You want fine control over how text is chunked (based purely on character count).


# it split document based both length of charactors

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader("F:\study\LangGraph_LangChain\paper.pdf")

doc = loader.load()

textsplitter = CharacterTextSplitter(separator=" ",
                                     chunk_size = 200,
                                     chunk_overlap=0
                                     )

split_doc = textsplitter.split_documents(doc)

print(split_doc[1].page_content)

