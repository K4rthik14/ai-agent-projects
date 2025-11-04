from crewai_tools import YoutubeChannelSearchTool
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "dummy")

# Create LLM instance for the tool
tool_llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    temperature=0.0
)

# Create Embedding model instance
google_embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001"
)

# Pass both the LLM and the embedder to the config
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle='https://www.youtube.com/channel/UCNU_lfiiWBdtULKOw6X0Dig',

    config=dict(
        llm=tool_llm,
        embedder=google_embeddings
    )
)
