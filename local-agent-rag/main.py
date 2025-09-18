from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model =OllamaLLM(model="llama3.2")

template = """"
You are an expert in answering questions about pizza restaurants.
Here are some relevant reviews = {reviews}
Here is the questions to answer = {question} 
Please provide a detailed answer based on the reviews."""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


while True:
    print("\n\n-------------------")
    question = input("Ask Your Question(press Q to quit): ")
    print("-------------------\n\n")
    if question == "q" or question == "Q":
        break
    reviews = retriever.invoke(question)  
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)