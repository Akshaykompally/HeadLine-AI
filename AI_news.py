import streamlit as st
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load API Keys
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="AI News Summarizer",
    page_icon="📰",
    layout="centered"
)

st.title("📰 AI News Summarizer")
st.write("Search the latest AI news and get a concise summary using Mistral AI.")

# User Input
query = st.text_input(
    "Enter a topic",
    value="Latest AI news"
)

if st.button("Summarize News"):

    with st.spinner("Fetching latest news..."):

        try:
            # Tavily Search
            search_tool = TavilySearchResults(max_results=5)
            news_result = search_tool.invoke({"query": query})

            # LLM
            llm = ChatMistralAI(model_name="mistral-small-2506")

            # Prompt
            prompt = ChatPromptTemplate.from_template("""
You are an expert AI news assistant.

Summarize the following news into concise bullet points.

News:
{news}

Summary:
""")

            chain = prompt | llm | StrOutputParser()

            summary = chain.invoke({
                "news": news_result
            })

            st.success("Summary Generated!")

            st.subheader("📄 Summary")
            st.write(summary)

            with st.expander("🔍 Raw Search Results"):
                st.json(news_result)

        except Exception as e:
            st.error(f"Error: {e}")