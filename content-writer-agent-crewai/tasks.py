from crewai import Task
from tools import yt_tool
from agents import blog_research, blog_writer

# Research Task
research_task = Task(
    description=(
        "Identify the video related to {topic}. "
        "Get detailed information about the video from the YouTube channel."
    ),
    expected_output="A comprehensive 3-paragraph report based on the {topic} of the video content.",
    tools=[yt_tool],
    agent=blog_research,
)

# Writing Task
write_task = Task(
    description=(
        "Use the information from the YouTube channel on the topic {topic} "
        "and create an engaging blog post."
    ),
    expected_output="Summarize the information from the YouTube channel video on the topic {topic} and create content for the blog.",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post-{topic}.md'
)
