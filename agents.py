from crewai import Agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_openai import ChatOpenAI

from langchain_community.llms import Ollama

# Human Tools
# human_tools = load_tools(["human"])

class RedditAgents():
    # def __init__(self):
        # self.OpenAIGPT35 = ChatOpenAI(
        #     model_name="gpt-3.5-turbo", temperature=0.7)
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        
        # self.mixtral = Ollama(
        #         # model="nous-hermes2-mixtral:8x7b-dpo-q5_K_M",
        #         model="starling-lm:7b-alpha-q6_K",
        #         base_url="http://localhost:11434",
        #         verbose=True,
        #         temperature=0,
        #         top_p=0.9,
        #         num_predict=-1,
        #         mirostat=2,             
        #         num_ctx=8192,
        #     )
        
        # self.llm = Ollama(
        #     # model="llama3:70b-instruct-q4_K_M",
        #     # model="command-r:plus-Q4_K_M",
        #     # model="dbrx:132b-instruct-q4_0",
        #     model="WizardLM2:8x22B-Q4_K_M",
        #     base_url="http://localhost:11434",
        #     verbose=True,
        #     temperature=0,
        #     top_p=0.9,
        #     num_predict=-1,
        #     mirostat=2,
        #     num_ctx=52000,
        # )

        # openai_api_key = 'taSncDAGzfe97eCUtEbeRUpGuAAWnypi0VE6y6JDj4ivqALV'
        # # base_url = os.environ.get("OPENAI_API_BASE")
        # # openai_api_key = os.environ.get("DEEPSEEK_API_KEY")
        # base_url = 'http://localhost:8080/v1'
        # self.llm = ChatOpenAI(model='accounts/fireworks/models/nous-hermes-2-mixtral-8x7b-dpo-fp8', verbose=True, temperature = 0, openai_api_key=openai_api_key, base_url=base_url) # Loading GPT-3.5
    
    def reddit_researcher(self, llm, search_tool):
        return Agent(
            role = "Senior Researcher",
            goal=f"Find and explore the most exciting information on Reddit",
            backstory="""You are an information expert and know how to discover exciting information.
            You're great at finding interesting, exciting projects on any subreddit. You transform the scraped data into reports with specific content. Only data scraped from Reddit subreddits is used in the report.
            """,
            verbose=True,
            allow_delegation=False,
            tools=[search_tool],
            max_iter=10,
            llm=llm,
            # function_calling_llm=llm,
        )

    def translator(self, llm):
        return Agent(
            role="translator",
            goal="Translate text into the language of the specified country",
            backstory="""As a professional translator, you are familiar with the languages ​​of various countries, and are especially able to translate with warmth and sensitivity based on the characteristics and habits of the target language. """,
            verbose=True,
            llm=llm,
            allow_delegation=False,
            max_iter=10,
            # tools=[search_tool, ContentTools.read_content],
        )
