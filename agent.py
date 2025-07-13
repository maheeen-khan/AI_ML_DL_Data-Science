from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["API_KEY"] = os.getenv("API_KEY")

agent = Agent(
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    description="You are an assistant please reply based on the question",
    tools=[DuckDuckGoTools()]
    markdown=True,
)