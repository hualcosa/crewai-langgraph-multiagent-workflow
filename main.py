from src.workflows.main_workflow import app
from dotenv import load_dotenv

load_dotenv()


def main():
    query = """
    Can you reply to this email

    Hello,
    Thank you for applying to xyz company
    can you share me your previous CTC
    Thanks,
    HR
    """
    inputs = {"query": query, "messages": [query]}
    result = app.invoke(inputs)
    print("Agent Response:", result["messages"][-1])


if __name__ == "__main__":
    main()
