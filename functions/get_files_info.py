def get_files_info(working_directory, directory="."): 
    full_path = os.path.join(working_directory, directory)
    full_path = os.path.abspath(full_path)

    if not full_path.startswith(os.path.abspath(working_directory))
        raise ValueError(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    return full_path
