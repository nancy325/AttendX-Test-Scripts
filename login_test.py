import unittest


def login(username, password):
    if username == "student" and password == "test123":
        return "Login successful"
    return "Invalid credentials"


class LoginTest(unittest.TestCase):

    def test_valid_login(self):
        self.assertEqual(
            login("student", "test123"),
            "Login successful"
        )

    def test_invalid_password(self):
        self.assertEqual(
            login("student", "wrong"),
            "Invalid credentials"
        )


if __name__ == "__main__":
    unittest.main()