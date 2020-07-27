def check_pwd(password):
    symbols = '~`!@#$%^&*()_+-='

    if len(password) < 8 or len(password) > 20:
        return False

    return True
