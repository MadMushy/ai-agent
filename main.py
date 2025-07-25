import os
import sys
import types
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file, call_function

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

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    available_functions = types.Tool(function_declarations=[schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file])

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents= messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    
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

    if not response.function_calls:
        return response.text

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")
        

    

if __name__ == "__main__":
    main()
