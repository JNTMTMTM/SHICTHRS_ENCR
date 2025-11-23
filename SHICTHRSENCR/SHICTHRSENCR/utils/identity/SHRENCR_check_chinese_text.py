
import re

def check_chinese_text(text : str) -> bool:
    if not text or text.strip() == '':
        return False
    
    pattern = r'^[\u4e00-\u9fff]+$'

    return bool(re.fullmatch(pattern , text))