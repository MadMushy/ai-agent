import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    print("Hello from ai-agent!")

    args = sys.argv[1:]
    content = " ".join(args)
    verbose = False

    messages = [
        types.Content(role="user", parts=[types.Part(text=content)]),
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents= messages
    )

    if '--verbose' in args:
        verbose = True
        args.remove('--verbose')
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        print(f"User prompt: {content}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")


    if not args:
        print("Error must pass content. Usage uv main.py <content>")
        sys.exit(1)

    print(response.text)




if __name__ == "__main__":
    main()
