from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",  # Fixed 'odel' -> 'model'
    temperature=0.0
)

# Create a Senior Blog Content Researcher Agent
blog_research = Agent(
    role="Senior Blog Content Researcher",
    goal="Get relevant video content ideas for the given {topic} from YouTube and provide a detailed research report.",
    name="Senior Blog Content Researcher",
    verbose=True,
    memory=True,
    llm=llm,
    backstory=(
        "Expert in understanding videos in Data Science, Machine Learning, and AI domains."
    ),
    tools=[yt_tool],
    allow_delegation=True
)

# Create a Senior Blog Content Writer Agent
blog_writer = Agent(
    role="Senior Blog Writer",
    goal="Narrate compelling tech stories about the video {topic}.",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible and compelling manner."
    ),
    llm=llm,
    tools=[yt_tool],
    allow_delegation=False  # Fixed typo 'deligation' -> 'delegation'
)
