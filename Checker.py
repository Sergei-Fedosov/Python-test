import os

def check_file(path):

    if os.path.exists(path) and os.path.getsize(path) > 0:
        return True
    else:
        return False