import string

# מחלקת חריגה מותאמת אישית לחריגה כשיש תו לא חוקי בשם המשתמש
class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, char, index):
        self.char = char
        self.index = index

    def __str__(self):
        return f"Username contains illegal character '{self.char}' at index {self.index}."

# מחלקת חריגה עבור שם משתמש קצר מדי
class UsernameTooShort(Exception):
    def __str__(self):
        return "Username is too short. Must be between 3 and 16 characters."

# מחלקת חריגה עבור שם משתמש ארוך מדי
class UsernameTooLong(Exception):
    def __str__(self):
        return "Username is too long. Must be between 3 and 16 characters."

# מחלקת חריגה בסיסית עבור סיסמה שחסרה תו נדרש
class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "Password is missing a required character."

# מחלקות חריגה עבור כל סוג תו שחסר בסיסמה
class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)."

class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)."

class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)."

class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)."

# מחלקת חריגה עבור סיסמה קצרה מדי
class PasswordTooShort(Exception):
    def __str__(self):
        return "Password is too short. Must be between 8 and 40 characters."

# מחלקת חריגה עבור סיסמה ארוכה מדי
class PasswordTooLong(Exception):
    def __str__(self):
        return "Password is too long. Must be between 8 and 40 characters."

# פונקציה לבדיקת הקלט של שם משתמש וסיסמה
def validate_input(username, password):
    # בדיקה אם שם המשתמש באורך תקין
    if not (3 <= len(username) <= 16):
        if len(username) < 3:
            raise UsernameTooShort()
        else:
            raise UsernameTooLong()

    # בדיקה אם שם המשתמש מכיל תווים חוקיים בלבד
    for index, char in enumerate(username):
        if not (char.isalnum() or char == '_'):
            raise UsernameContainsIllegalCharacter(char, index)

    # בדיקה אם הסיסמה באורך תקין
    if not (8 <= len(password) <= 40):
        if len(password) < 8:
            raise PasswordTooShort()
        else:
            raise PasswordTooLong()

    # בדיקה אם הסיסמה מכילה לפחות אות גדולה אחת
    if not any(c.isupper() for c in password):
        raise PasswordMissingUppercase()
    # בדיקה אם הסיסמה מכילה לפחות אות קטנה אחת
    if not any(c.islower() for c in password):
        raise PasswordMissingLowercase()
    # בדיקה אם הסיסמה מכילה לפחות ספרה אחת
    if not any(c.isdigit() for c in password):
        raise PasswordMissingDigit()
    # בדיקה אם הסיסמה מכילה לפחות תו מיוחד אחד
    if not any(c in string.punctuation for c in password):
        raise PasswordMissingSpecial()

    print("OK")
    # אם כל הבדיקות עוברות, מדפיסים "OK"

def main():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            validate_input(username, password)
            break  # אם הבדיקה עברה בהצלחה, יוצאים מהלולאה
        except Exception as e:
            print(e)  # מדפיסים את השגיאה
            print("Please try again.")  # מבקשים לנסות שוב

if __name__ == "__main__":
    main()