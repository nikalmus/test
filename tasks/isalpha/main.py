def is_alpha_or_what(s):
    result = {
        'alphanumeric': False,
        'alphabetic': False,
        'digit': False,
        'lower': False,
        'upper':False
    }

    """Check if the given string contains any alphanumeric characters."""
    for c in s:
        if c.isalnum():
            result['alphanumeric'] = True
            break

    """Check if the given string contains any alphabetic characters."""
    for c in s:
        if c.isalpha():
            result['alphabetic'] = True
            break

    """Check if the given string contains any digits."""
    for c in s:
        if c.isdigit():
            result['digit'] = True
            break

    """Check if the given string contains any lowercase characters."""
    for c in s:
        if c.islower():
            result['lower'] = True
            break

    """Check if the given string contains any uppercase characters."""
    for c in s:
        if c.isupper():
            result['upper'] = True
            break

    return result

if __name__ == "__main__":
    s = input().strip
    result = is_alpha_or_what(s)
    {print(v) for v in result.values()}