from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

search_tool = TavilySearchResults(max_results=5)

llm = ChatMistralAI(model_name="mistral-small-2506")

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant.

Summarize the following AI news into clear bullet points.

{news}
""")

chain = prompt | llm | StrOutputParser()

news_result = search_tool.invoke({"query": "Latest AI news"})

result = chain.invoke({
    "news": news_result
})

print(result)