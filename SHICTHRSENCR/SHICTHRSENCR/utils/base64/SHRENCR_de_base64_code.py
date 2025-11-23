
import base64

def de_base64_code(en_code : str) -> str:
    return base64.b64decode(en_code).decode('utf-8')