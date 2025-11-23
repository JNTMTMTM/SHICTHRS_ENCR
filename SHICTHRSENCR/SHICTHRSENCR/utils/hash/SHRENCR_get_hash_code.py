
import hashlib

def get_hash_code(org_code : str) -> str:
    md5 = hashlib.md5()
    md5.update(org_code.encode('utf-8'))
    ecy_code = md5.hexdigest()
    return ecy_code