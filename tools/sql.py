import sqlite3
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool,Tool
conn=sqlite3.connect("C://Users//my_project//langchian_agent//db.sqlite")

def list_tables():
    c=conn.cursor()
    c.execute("select name from sqlite_master where type='table';")
    rows=c.fetchall()
    return "\n".join(row[0] for row in rows if row[0] is not None)

class calculator_input(BaseModel):
    a: int=Field(description="first Number")
    b: int=Field(description="second Number")

class multiplyer_input(BaseModel):
    m: int=Field(description="third number")
    n: int=Field(description="fourth number")    


def run_sqlite_query(query: str) ->str :
    c=conn.cursor()
    try:
        c.execute(query)
        return c.fetchall()
    except Exception as e:
        return f"following error is occured {str(e)}"

run_query_tool= Tool.from_function(
    name="run_sqlite_query",
    description="Run a sqlite query",
    func=run_sqlite_query
)

def addition(a:int, b:int) ->int:
    "adding two numbers"
    return a+b

async def multiplication(m:int,n:int) ->int:
    """multiply two integers"""
    return m*n
    
multiplication_tool=StructuredTool.from_function(
    name="multiplication_tool",
    description="multiply two u=numbers",
    func=multiplication,
    args_schema=multiplyer_input,
    return_direct=True
)


addition_tool=StructuredTool.from_function(
    name="addition_tool",
    description="add two integers",
    func=addition,
    args_schema=calculator_input,
    return_direct=True
)

def describe_tables(tables):
    tables=list(tables)
    c=conn.cursor()
    try:
        tables=", ".join("'" + table + "'" for table in tables)
        rows=c.execute(f"select sql from sqlite_master where type='table' and name in ({tables});")
        return "\n".join(row[0] for row in rows if row[0] is not None)
    except Exception as e:
        return f"following error is occured {e}"

describe_tables_tool=Tool.from_function(
    name="describe_tables",
    description="look for the coloumns present in the table don't assume",
    func=describe_tables
)
    
