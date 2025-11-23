
from datetime import datetime

IDENTITY_FACTORS = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
IDENTITY_CHECK_CODES = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

def check_identity_number(identity_number : str) -> bool:
    if not isinstance(identity_number, str):
        return False
    
    identity_number = identity_number.strip().upper()
    
    if len(identity_number) not in [15, 18]:
        return False
    
    if len(identity_number) == 15:
        if not identity_number.isdigit():
            return False
        
        try:
            birth_date = datetime.strptime("19" + identity_number[6:12], "%Y%m%d")
            if birth_date > datetime.now():
                return False
        except ValueError:
            return False
            
        return True
    
    if not (identity_number[:17].isdigit() and (identity_number[17].isdigit() or identity_number[17] == 'X')):
        return False
    
    try:
        birth_date = datetime.strptime(identity_number[6:14], "%Y%m%d")
        if birth_date > datetime.now():
            return False
    except ValueError:
        return False
    
    total = 0
    for i in range(17):
        total += int(identity_number[i]) * IDENTITY_FACTORS[i]
    
    mod = total % 11
    calculated_check_code = IDENTITY_CHECK_CODES[mod]
    
    if identity_number[17] != calculated_check_code:
        return False
        
    return True