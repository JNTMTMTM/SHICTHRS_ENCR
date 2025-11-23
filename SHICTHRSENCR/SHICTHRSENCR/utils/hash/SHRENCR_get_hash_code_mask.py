
def get_hash_code_mask(org_code : str) -> str:
    return org_code[:4] + '*' * 24 + org_code[-4:]