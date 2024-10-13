import re


class StringValidator:
    @staticmethod
    def validate_email_format(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{2,4}+$'
        return re.match(email_regex, email)
