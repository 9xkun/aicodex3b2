import unittest
from app.utils.stringvalidator import StringValidator

class TestStringValidator(unittest.TestCase):

    def test_validate_email_format_valid(self):
        valid_emails = [
            "test@example.com",
            "user.name+tag+sorting@example.com",
            "user_name@example.co.uk",
            "user-name@example.org",
            "user.name@example.io"
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(StringValidator.validate_email_format(email))

    def test_validate_email_format_invalid(self):
        invalid_emails = [
            "plainaddress",
            "@missingusername.com",
            "username@.com",
            "username@.com.",
            "username@com",
            "username@-example.com",
            "username@example..com",
            "username@.example.com",
            "username@.example.com.",
            "username@.example..com"
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(StringValidator.validate_email_format(email))

if __name__ == "__main__":
    unittest.main()