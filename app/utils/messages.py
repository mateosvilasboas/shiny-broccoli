class UserMessage:
    @staticmethod
    def email_already_exists():
        """Email already exists error message"""
        return """Email already exists"""

    @staticmethod
    def not_enough_permissions():
        """Not enough permissions error message"""
        return """Not enough permissions"""

    @staticmethod
    def user_deleted():
        """User deleted error message"""
        return """User deleted"""

    @staticmethod
    def user_already_deleted():
        """User already deleted error message"""
        return """User already deleted"""


class AuthMessage:
    @staticmethod
    def wrong_email_or_password():
        """Wrong email or password error message"""
        return """Wrong email or password"""


class ChartMessage:
    @staticmethod
    def chart_not_found(code: str):
        """Chart with code not found error message"""
        return f"Chart with code '{code}' not found"
    
    @staticmethod
    def entries_not_found(code: str):
        """Entries in chart with code not found error message"""
        return f"Entries in chart with code '{code}' not found"
