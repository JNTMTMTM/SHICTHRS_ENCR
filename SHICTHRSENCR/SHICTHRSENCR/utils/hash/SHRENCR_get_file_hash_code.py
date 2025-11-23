
import hashlib

def get_file_hash_code(path : str) -> str:
    sha256_hash = hashlib.sha256()
    
    with open(path , "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    
    return sha256_hash.hexdigest()