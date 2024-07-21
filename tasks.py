# from functools import partial
from crewai import Task
from textwrap import dedent
from datetime import datetime


class RedditTasks():

    today_date = datetime.now().strftime('%Y-%m-%d-%H-%M')

    def search_reddit(self, agent, query, sort, time_filter, subreddit, limit):
        return Task(
            description=dedent(f"""
                Pass the complete Reddit search parameters (subreddit:{subreddit}, query: {query}, sort: {sort}, time_filter: {time_filter}, limit: {limit}) to the agent.
                Search topic data from Reddit subreddit, 
                summarize the information of each topic, and generate reports respectively.
                Note: It must be a complete report, the number of topics should be consistent with the {limit} quantity.
                """),
            agent=agent,
            output_file=f"output/{self.today_date}_Reddit_Report.md",
            expected_output = dedent(f"""
                It's a complete report.
                And must be in Chinese,
                and saved to the specified file. 
                Please use Markdown format, as shown in the following example:                   
                '## 1.post title (标题):
                    - Link to this post: 
                    - Post type (类型):
                    - Highlights (亮点):
                    - Tools and links cited in the post:
                    - Summarize (摘要):
                ... ... '
                """),            
        )

    def translate_report(self, agent):
        return Task(
            description=dedent(f"""Professional translation of the report into Chinese. 
                """),
            agent=agent,
            # context=context,
            output_file=f"output/{self.today_date}_Reddit_Report_ZH.md",
            expected_output = dedent(f"""  
            For your final Outputs use the markdown format.
            Note: that terms such as post title, tool name, function name, model name, company name, etc. retain their original names and do not translate. Keep the format of the original English report.
                """),
        )
