import asyncio
import os
from dotenv import load_dotenv
from agents.planning_agent import planner_agent

load_dotenv()

def handle_api_error(exc: Exception) -> None:
    message = str(exc).lower()

    if not os.getenv("GOOGLE_API_KEY"):
        print("Missing GOOGLE_API_KEY. Add it to your environment or .env file before running the planner.")
        return

    if "quota" in message or "resource_exhausted" in message or "429" in message or "rate limit" in message:
        print("Gemini API quota has been exhausted. Check your Google AI billing/quota limits and try again later.")
        return

    print(f"The planner could not generate a response: {exc}")


async def main():
    while True:
        query = input("Wedding request: ")

        if query.lower() == "exit":
            break

        try:
            response = await planner_agent.ainvoke({
                "messages": [
                    {
                        "role": "user",
                        "content": query
                    }
                ]
            })

            print()

            for message in response["messages"]:
                print("\n----------------")
                print(type(message).__name__)
                print(message.content)

            print("\n\n -- ACTUAL PLAN -- \n\n")


            print(response["messages"][-1].content[0]["text"])
        except Exception as exc:
            handle_api_error(exc)
            break


if __name__ == "__main__":
    asyncio.run(main())