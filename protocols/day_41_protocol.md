# Day 41 protocol - RAG pipelines - 30.10.2025

## What is RAG?
**Retrieval-Augmented Generation (RAG)** is a technique that combines:
- **Retriever** -> finds relevant information from documents
- **Generator (LLM)** -> uses retrieved information to generate response from query

Advantages:
- gives **fact-based answers** based on specific data
- reduces **hallucinations** (made-up facts)
- handles **domain-specific** information not in its training data

Used in:
- Enterprise document search
- Domain-specific chatbots
- Coding assistants
- Financial report analyses


---

## Main Components

| Component | Description | Example Tools |
|------------|--------------|----------------|
| **Documents** | source data (e.g. PDFs) | PyPDFLoader |
| **Text Splitter** | splits text into smaller chunks | RecursiveCharacterTextSplitter |
| **Embeddings** | transforms text into numeric vectors that capture meaning | HuggingFaceEmbeddings |
| **Vector Store** | stores embeddings | FAISS |
| **Retriever** | finds most relevant chunks to specific query | |
| **LLM (Generator)** | reads retrieved chunks and generates response | ChatGroq |
| **RAG Chain** | combines retriever and LLM into one pipeline | |

---

## Example of RAG pipeline in Python

0. **Prepare LLM**
```python
from dotenv import load_dotenv
import warnings
from langchain_groq import ChatGroq
from langchain.prompts.prompt import PromptTemplate

load_dotenv()

warnings.filterwarnings("ignore")

llm = ChatGroq(
    model="llama-3.1-8b-instant", #"llama3-8b-8192",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)
```

0. **Import libraries**
```python
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.faiss import DistanceStrategy
from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
import numpy as np
```

1. **Load documents**
```python
def load_pdf_data(pdf_path):
    """
    Load text data from PDF file.
    """
    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()
    return documents

react_docs = load_pdf_data(pdf_path="../documents/react_paper.pdf")
```

2. **Split text**
```python
def split_documents(documents, chunk_size=200, chunk_overlap=50):
    """
    Splits documents into chunks of given size and overlap
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = text_splitter.split_documents(documents=documents)
    
    # Just to add id for etch chunks to map it later 
    for i, chunk in enumerate(chunks):
         chunk.metadata.update({"id": f"chunk_{i}"})
    
    return chunks

react_chunks = split_documents(react_docs)
```

3. **Embed chunks and store vectors**
```python
def create_embedding_vector_db(chunks, db_name):
    """
    This function uses the open-source embedding model HuggingFaceEmbeddings 
    to create embeddings and store those in a VectorStore called FAISS, 
    which allows for efficient similarity search
    """
    # instantiate embedding model
    embedding = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-mpnet-base-v2',
        encode_kwargs={"normalize_embeddings": True}
    )
    # create the vector store 
    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embedding,
        distance_strategy=DistanceStrategy.COSINE  # or DistanceStrategy.DOT or DistanceStrategy.L2 
        
    )
    # save VectorStore locally
    vectorstore.save_local(f"../vector_databases/vector_db_{db_name}")
    return vectorstore

all_embedding = create_embedding_vector_db(chunks=react_chunks, db_name="react")
```

4. **Retrieve**
```python
def retrieve_from_vector_db(vector_db_path):
    """
    this function splits out a retriever object from a local VectorStore
    """
    # instantiate embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-mpnet-base-v2',
        encode_kwargs={"normalize_embeddings": True}
    )
    react_vectorstore = FAISS.load_local(
        folder_path=vector_db_path,
        embeddings=embeddings,
        allow_dangerous_deserialization=True,
        distance_strategy=DistanceStrategy.COSINE  # or DistanceStrategy.DOT or DistanceStrategy.L2 
    )
    retriever = react_vectorstore.as_retriever()
    return retriever, react_vectorstore

react_retriever, react_vectorstore = retrieve_from_vector_db("../vector_databases/vector_db_react")
```

5. **Connect retriever to LLM**
```python
def connect_chains(retriever):
    """
    this function connects stuff_documents_chain with retrieval_chain
    """
    stuff_documents_chain = create_stuff_documents_chain(
        llm=llm,
        prompt=hub.pull("langchain-ai/retrieval-qa-chat")
    )
    retrieval_chain = create_retrieval_chain(
        retriever=retriever,
        combine_docs_chain=stuff_documents_chain
    )
    return retrieval_chain

react_retrieval_chain = connect_chains(react_retriever)
```

6. **Generate an answer**
```python
output = react_retrieval_chain.invoke({"input": "what is zebra?"})
print(output['answer'])
```

## Main Components

- ds-rag-pipeline/notebooks/RAG-Pipeline-Llama.ipynb
- ds-rag-pipeline/notebooks/RAG-Exercise_Notebook.ipynb