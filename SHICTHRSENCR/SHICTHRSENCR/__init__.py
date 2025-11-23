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
        raise SHRENCRException(f"SHRENCR [ERROR.1001] unable to get hash code. | {e}")