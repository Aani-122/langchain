from dotenv import load_dotenv
import os
from langchain_community.llms import HuggingFaceHub
from langchain_core.runnables.config import get_executor_for_config
from langchain.chains import LLMChain, SequentialChain
from langchain_core.prompts import (PromptTemplate,
                                    ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    MessagesPlaceholder)
from tools.sql import run_query_tool,list_tables,describe_tables_tool,addition_tool,multiplication_tool
from langchain.schema import SystemMessage
load_dotenv()

from langchain.agents import create_openai_functions_agent, AgentExecutor


mistral=ChatGoogleGenerativeAI(model="gemini-pro",convert_system_message_to_human=True)
tables=list_tables()
print(tables)
#HuggingFaceHub(repo_id="HuggingFaceH4/zephyr-7b-beta")
prompt=ChatPromptTemplate(
    messages=[
        SystemMessage(content=f"""you are good assistant and you have the access of tool to solve 
                      problem contain two or more steps of mutilpication and addition"""),
        HumanMessagePromptTemplate.from_template("give me the answer for following {input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)
tools=[addition_tool]

agent=create_openai_functions_agent(
    llm=mistral,
    prompt=prompt,
    tools=tools
)

agent_executer=AgentExecutor(
    agent=agent,
    verbose=True,
    tools=tools
)
a=agent_executer({"input":" add five and 10 "})
print(a)

