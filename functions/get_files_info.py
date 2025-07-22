#!/usr/bin/env python3
import os
import subprocess
from config import *

def get_files_info(working_directory, directory="."):

    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, directory))

    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    try:
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"

def get_file_content(working_directory, file_path):

    abs_working_dir = os.path.abspath(working_directory) 
    target_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outide the permitted working directory.'
    if not os.path.isfile(target_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:   
        if os.path.isfile(target_path):
            with open(target_path, "r") as file:
                content = file.read()
                words = content.split()

                if len(words) > 10000:
                    truncate_text = " ".join(words[:TRUNCATE])
                    return f"{truncate_text} File '{file_path}' truncated at 10000 characters"
                else:
                    truncate_text = content
                    return f"{truncate_text}"
    except Exception as e:
        return f"Error listing files: {e}"

def write_file(working_directory, file_path, content):

    abs_working_dir = os.path.abspath(working_directory) 
    target_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outide the permitted working directory.'
    try:
        if os.path.isfile(target_path):
            with open(target_path, "w") as file:
                file.write(content)
        else:
            os.makedirs(os.path.dirname(target_path), exist_ok = True)
            with open(target_path, "w") as file:
                file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error writing files: {e}'

def run_python_file(working_directory, file_path, args=[]):

    abs_working_dir = os.path.abspath(working_directory) 
    target_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory.'
    if not os.path.isfile(target_path):
        return f'Error: File "{file_path}" not found.'
    if not target_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        
        result = subprocess.run(["python3", target_path] + args, cwd=working_directory, timeout=30, capture_output=True, text=True)

        output = ""
        if result.stdout:
            output += f"STDOUT: {result.stdout}"
        if result.stderr:
            output += f"\nSTDERR: {result.stderr}"
        if not output.strip():
            return "No output produced."
        if result.returncode != 0:
            output += f"\nProcess exited with code {result.returncode}"
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"

        
