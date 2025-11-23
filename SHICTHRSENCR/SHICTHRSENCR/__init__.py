# *-* coding: utf-8 *-*
# src\__init__.py
# SHICTHRS JSON LOADER
# AUTHOR : SHICTHRS-JNTMTMTM
# Copyright : © 2025-2026 SHICTHRS, Std. All rights reserved.
# lICENSE : GPL-3.0

import os
from colorama import init
init()
from .utils.hash.SHRENCR_get_hash_code import get_hash_code
from .utils.hash.SHRENCR_get_file_hash_code import get_file_hash_code
from .utils.hash.SHRENCR_get_hash_code_mask import get_hash_code_mask
from .utils.base64.SHRENCR_en_base64_code import en_base64_code
from .utils.base64.SHRENCR_de_base64_code import de_base64_code
from .utils.identity.SHRENCR_check_identity_number import check_identity_number
from .utils.identity.SHRENCR_check_chinese_text import check_chinese_text

print('\033[1mWelcome to use SHRENCR - ENCR System\033[0m\n|  \033[1;34mGithub : https://github.com/JNTMTMTM/SHICTHRS_ENCR\033[0m')
print('|  \033[1mAlgorithms = rule ; Questioning = approval\033[0m')
print('|  \033[1mCopyright : © 2025-2026 SHICTHRS, Std. All rights reserved.\033[0m\n')

class SHRENCRException(BaseException):
    def __init__(self , message: str) -> None:
        self.message = message
    
    def __str__(self):
        return self.message

def SHRENCR_get_hash_code(org_code : str) -> str:
    try:
        return get_hash_code(org_code)
    except Exception as e:
        raise SHRENCRException(f"SHRENCRException [ERROR.3000] unable to get hash code. | {str(e)}")

def SHRENCR_get_file_hash_code(path : str) -> str:
    try:
        if os.path.exists(path):
            if os.path.isfile(path):
                return get_file_hash_code(path)
            else:
                raise SHRENCRException(f"SHRENCRException [ERROR.3000.1.0] only support file. | {path}")
        else:
            raise SHRENCRException(f"SHRENCRException [ERROR.3000.1.1] file not found. | {path}")
    except Exception as e:
        raise SHRENCRException(f"SHRENCRException [ERROR.3000.1.2] unable to get file hash code. | {str(e)}")

def SHRENCR_get_hash_code_mask(org_code : str) -> str:
    try:
        return get_hash_code_mask(org_code)
    except Exception as e:
        raise SHRENCRException(f"SHRENCRException [ERROR.3000.2] unable to get hash code mask. | {str(e)}")

def SHRENCR_en_base64_code(org_code : str) -> str:
    try:
        return en_base64_code(org_code)
    except Exception as e:
        raise SHRENCRException(f"SHRENCRException [ERROR.3001] unable to encrypt base64 code. | {str(e)}")

def SHRENCR_de_base64_code(en_code : str) -> str:
    try:
        return de_base64_code(en_code)
    except Exception as e:
        raise SHRENCRException(f"SHRENCRException [ERROR.3002] unable to decrypt base64 code. | {str(e)}")

def SHRENCR_check_identity_number(identity_number : str) -> bool:
    try:
        return check_identity_number(identity_number)
    except Exception as e:
        raise SHRENCRException(f"SHRENCRException [ERROR.3003] unable to check identity number. | {str(e)}")

def SHRENCR_check_chinese_text(text : str) -> bool:
    try:
        return check_chinese_text(text)
    except Exception as e:
        raise SHRENCRException(f"SHRENCRException [ERROR.3004] unable to check chinese text. | {str(e)}")