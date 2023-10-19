import autogen

config_list = [
    {
        'model': 'gpt-3.5-turbo-16k',
        "api_key": "NULL",
    }
]

llm_config = {
    "request_timeout": 600,
    "seed": 42,
    "temperature": 0,
}

assistant = autogen.AssistantAgent(
    name="CEO", system_message="Chief executive officer of a tech company",llm_config=llm_config
)
assistant = autogen.AssistantAgent(
    name="CTO", system_message="Chief technical officer of a tech company",llm_config=llm_config
)
assistant = autogen.AssistantAgent(
    name="Designer", system_message="Designer / User experience",llm_config=llm_config
)
assistant = autogen.AssistantAgent(
    name="Frontend Engineer", system_message="Frontend Software Engineer of a tech company",llm_config=llm_config
)
assistant = autogen.AssistantAgent(
    name="Backend Engineer", system_message="Backend Software Engineer of a tech company",llm_config=llm_config
)

user_proxy = autogen.UserProxyAgent(
  name="user_proxy",
  human_input_mode="TERMINATE",
  max_consecutive_auto_reply=10,
  is_termination_msg=lambda x: x.get("content","").rstrip().endswith("TERMINATE"),
  code_execution_config={"work_dir":"web"},
  llm_config=llm_config,
  system_message="""Reply TERMINATE if the task has been solved at full satisfaction. Otherwise, reply CONTINUE, or the reason why the task is not solved yet.""",
)

task = """
Give me a summary of this article: https://apnews.com/article/u2-sphere-c83d05a33246525c16d6638a12bb9324
"""

user_proxy.initiate_chat(
  assistant,
  message=task,

)