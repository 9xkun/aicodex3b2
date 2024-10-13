import re


class StringValidator:
    @staticmethod
    def validate_email_format(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{2,4}+$'
        return re.match(email_regex, email)

    # validate string that has numbers only
    @staticmethod
    def validate_number_string(string):
        number_regex = r'^[0-9]+$'
        return re.match(number_regex, string)