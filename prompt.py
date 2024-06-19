from langchain_core.messages import SystemMessage
from langchain_core.prompts import PromptTemplate


def prompt():
    prompt_template = PromptTemplate.from_template("Tell me a joke about {topic}")
    value = prompt_template.invoke({"topic": "cats"})
    print(value.text)


def chat_prompt():
    from langchain_core.prompts import ChatPromptTemplate

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant"),
        ("user", "Tell me a joke about {topic}")
    ])

    value = prompt_template.invoke({"topic": "cats"})
    print(value.messages)


def place_prompt():
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain_core.messages import HumanMessage

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant"),
        MessagesPlaceholder("msgs")
    ])

    value = prompt_template.invoke({"msgs": [HumanMessage(content="hi!"), SystemMessage(content="test ai!")]})
    print(value.messages)


if __name__ == '__main__':
    print('---------prompt-------')
    prompt()

    print('---------chat prompt-------')
    chat_prompt()

    print('---------place prompt-------')
    place_prompt()
