"""
Description: A simple password checker

Name: Jiashu Wei
"""


def is_valid_password(text):
    """Check whether a given text has the correct password format"""
    return 8 <= len(text) <= 20

def main():
    """Start program"""
    new_password = "hello world"
    print(f"{new_password} is a valid password? {is_valid_password(new_password)}")


if __name__ == '__mian__':
    main()




