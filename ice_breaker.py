from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

from third_parties.likedin import scrape_linkedin_profile

if __name__ == "__main__":
    print("Hello Langchain")
    load_dotenv()

    summary_template = """
        given the LinkedIn information {information} about a person from I want you to create:
        1. 한국어로 짧은 요약
        2. 그것에 대한 2가지 재밌는 사실
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )
    # llm = ChatOllama(model="llama3.1",temperature=0)

    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/eden-marco/",
        mock=True
    )

    res = chain.invoke(input={"information": linkedin_data})

    print(res)
