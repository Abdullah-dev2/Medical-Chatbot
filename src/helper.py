from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from typing import List
from langchain.schema import Document


def load_pdf_files(data):
    loader = DirectoryLoader(
        data,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader)
    
    documents = loader.load()
    return documents

def filter_to_mini_docs(docs: List[Document]) -> List[Document]:
    mini_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source")
        mini_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )
    return mini_docs

def text_splitter(mini_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
        length_function=len
    )
    texts = text_splitter.split_documents(mini_docs)
    return texts

from langchain.embeddings import HuggingFaceEmbeddings
def download_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings