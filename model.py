
def model_chat():
    from langchain_anthropic import ChatAnthropic

    model = ChatAnthropic(model="claude-3-sonnet-20240229")

    for chunk in model.stream("what color is the sky?"):
        print(chunk.content, end="|", flush=True)


def model_openai():
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_openai import ChatOpenAI
    from langchain.output_parsers.json import SimpleJsonOutputParser

    model = ChatOpenAI(
        model="gpt-4o",
        model_kwargs={"response_format": {"type": "json_object"}},
    )

    prompt = ChatPromptTemplate.from_template(
        "Answer the user's question to the best of your ability."
        'You must always output a JSON object with an "answer" key and a "followup_question" key.'
        "{question}"
    )

    chain = prompt | model | SimpleJsonOutputParser()

    chain.invoke({"question": "What is the powerhouse of the cell?"})


if __name__ == '__main__':
    print('---------model_chat start-------')
    model_chat()
    print('---------model_chat end-------')

    print('---------model_openai start-------')
    model_openai()
    print('---------model_openai end-------')
