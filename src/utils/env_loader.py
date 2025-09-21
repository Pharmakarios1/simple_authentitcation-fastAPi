import os

def load_env_file(file_path=".env"):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r') as env:
        for line in env:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, value = line.split("=",1)
            os.environ[key.strip()] = value.strip()