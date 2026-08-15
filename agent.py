from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from tools import tools


load_dotenv()


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)


system_prompt = """
You are a University Intelligent Task Execution Agent.

Your purpose is to help university students complete
university-related tasks.

You have access to the following tools:

1. Course Information Tool
2. Registration Fee Calculator
3. Registration Deadline Tool
4. Registration Requirements Tool

First understand and analyze the user's goal.

Then decide which tool or tools are required.

Use the appropriate tools to obtain the required information.

If the user's request requires multiple tools,
use all necessary tools.

Do not invent information that should come from a tool.

After receiving the tool results, provide a clear,
accurate and organized final answer.

You should be helpful and concise.
"""


agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt,
    name="university_task_agent"
)


def run_agent(user_goal: str) -> str:

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_goal
                }
            ]
        }
    )

    return result["messages"][-1].content