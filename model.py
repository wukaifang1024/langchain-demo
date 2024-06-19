
def model_chat():
    from langchain_anthropic import ChatAnthropic

    model = ChatAnthropic(model="claude-3-sonnet-20240229")

    for chunk in model.stream("what color is the sky?"):
        print(chunk.content, end="|", flush=True)


if __name__ == '__main__':
    model_chat()
