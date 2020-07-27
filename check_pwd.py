def check_pwd(password):
    symbols = '~`!@#$%^&*()_+-='

    if len(password) < 8 or len(password) > 20:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    return True
