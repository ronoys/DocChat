import os

def save_uploaded_file(uploaded_file, save_dir="/tmp"):
    temp_file_path = os.path.join(save_dir, uploaded_file.name)
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return temp_file_path
