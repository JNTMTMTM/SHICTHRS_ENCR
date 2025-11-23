
import base64

def en_base64_code(org_code : str) -> str:
    return base64.b64encode(org_code.encode('utf-8')).decode('utf-8')