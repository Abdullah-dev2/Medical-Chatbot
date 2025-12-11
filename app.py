from flask import Flask, request, render_template
from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_ai21 import ChatAI21
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
AI21_API_KEY = os.getenv("AI21_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["AI21_API_KEY"] = AI21_API_KEY

# Load embeddings
embeddings = download_embeddings()

# Pinecone index
index_name = "medical-chatbot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

# Retriever
retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# AI21 Chat Model
chatModel = ChatAI21(model="jamba-large")

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "{input}")
])

# RAG Chain
question_answering_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answering_chain)


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["POST"])
def chat():
    # FIXED: read POST form data
    msg = request.form.get("msg")

    if not msg:
        return "Please type a message."

    print("USER:", msg)

    # Run RAG pipeline
    response = rag_chain.invoke({"input": msg})

    # Safely extract answer (LangChain version proof)
    answer = (
        response.get("answer")
        or response.get("result")
        or response.get("output_text")
        or "I'm sorry, I couldn't generate a response."
    )

    print("BOT:", answer)
    return answer


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
