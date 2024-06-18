from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain_core.messages import AnyMessage, BaseMessage
from langchain.schema import SystemMessage #this will help us t get hardcoded message system message 
from langchain.prompts.base import StringPromptTemplate
from langchain.agents import create_openai_functions_agent, AgentExecutor
from tools.sql import run_query_tool, list_tables,describe_tables_tool, addition_tool

load_dotenv()
chat=ChatGoogleGenerativeAI(model="gemini-pro") #,convert_system_message_to_human=True
tables=list_tables()
print(tables)
prompt=ChatPromptTemplate(
    messages=[
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)#SystemMessage(content=f"you are Ai that has access to a SQLite databse.\n{tables}"),

tools=[addition_tool]
agent=create_openai_functions_agent(
    llm=chat,
    prompt=prompt,
    tools=tools
)

agent_executer=AgentExecutor(
    agent=agent,
    verbos=True,
    tools=tools
)

print(agent_executer.invoke({"input":"add 5 and 3 "}))