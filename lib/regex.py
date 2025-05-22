import re

# Name regex:
# Matches names like "John Cena", "Anya Taylor-Joy", "D'Angelo"
# - Each part starts with a capital letter
# - Optional apostrophe or hyphen within parts
# - Optional single space between parts
name = r"^[A-Z][a-z]*(?:['-][A-Z][a-z]*)?(?:\s[A-Z][a-z]*(?:['-][A-Z][a-z]*)?)?$"
name_regex = re.compile(name)

# Phone regex:
# Matches:
# - 5555555555
# - 555-555-5555
# - (555) 555-5555
phone_number = r"^(?:\(\d{3}\)\s?|\d{3}-?)\d{3}-?\d{4}$"
phone_regex = re.compile(phone_number)

# Email regex:
# - Must start with a letter (A-Z or a-z)
# - Then letters, digits, underscores, dots, or hyphens allowed
# - Then @, domain, and TLD with at least two letters
email_address = r"^[A-Za-z][\w\.-]*@[\w\.-]+\.[a-zA-Z]{2,}$"
email_regex = re.compile(email_address)
