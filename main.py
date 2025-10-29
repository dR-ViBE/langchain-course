from langchain_tavily import TavilySearch
from langchain_groq import ChatGroq
from langchain_classic.agents.react.agent import create_react_agent
from langchain_classic.agents import AgentExecutor
from langchain_classic import hub
from dotenv import load_dotenv
load_dotenv()

tools = [TavilySearch(max_results=3, search_depth="basic")]


llm = ChatGroq(model="llama-3.1-8b-instant")
react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
chain = agent_executor


def main():
    result = chain.invoke(input={
        "input": "search for 3 job postings for an ai engineer using langchain in the bay area on linkein and list their details"})

    print(result)


if __name__ == "__main__":
    main()
