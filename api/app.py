from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"

app = FastAPI(
    title="Langchain Server",
    description="API for Langchain",
    version="1.0"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
model = ChatOpenAI()
# ollama llama2
llm = Ollama(model="llama2")

prompt_openai = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words")
prompt_ollama = ChatPromptTemplate.from_template(
    "Write me an poem about {topic} with 100 words")

add_routes(
    app,
    prompt_openai | model,
    path="/essay"
)
add_routes(
    app,
    prompt_ollama | llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
