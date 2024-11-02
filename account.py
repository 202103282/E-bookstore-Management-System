class Account:
    """Represents a user account with email and password, allowing account creation, login, and logout functionality."""

    # Class-level dictionary to store all created accounts with email as the key
    _accounts = {}

    def __init__(self, email: str, password: str):
        self._email = email
        self._password = password
        self._is_logged_in = False

    @classmethod
    def createAccount(cls, email: str, password: str) -> None:
        """Creates a new account with the given email and password, if the email is not already registered."""
        if email in cls._accounts:
            raise ValueError("An account with this email already exists.")
        # Add the new account to the _accounts dictionary
        cls._accounts[email] = cls(email, password)
        print(f"Account created successfully for {email}.")

    def login(self, email: str, password: str) -> bool:
        """Logs in the user if the email and password match an existing account."""
        # Check if the email exists in the _accounts dictionary
        if email in Account._accounts and Account._accounts[email]._password == password:
            Account._accounts[email]._is_logged_in = True
            print(f"{email} logged in successfully.")
            return True
        print("Invalid email or password.")
        return False

    def logout(self) -> None:
        """Logs the user out if they are logged in."""
        if self._is_logged_in:
            self._is_logged_in = False
            print(f"{self._email} logged out successfully.")
        else:
            print(f"{self._email} is not currently logged in.")

    @property
    def email(self):
        return self._email

    @property
    def is_logged_in(self):
        return self._is_logged_in

    def __str__(self):
        return f"Account(email={self._email}, logged_in={self._is_logged_in})"
