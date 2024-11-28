import re
import getpass

# Display a welcome message
print("---------------- Password Complexity Checking Tool -----------------")

def assess_password_strength(password: str) -> str:
    """
    Evaluates the strength of a password based on several criteria:
    - Contains numbers
    - Contains both uppercase and lowercase letters
    - Meets minimum length requirement
    - Contains special characters
    """
    # Check if the password contains numbers
    has_numbers = any(char.isdigit() for char in password)
    
    # Check if the password contains both uppercase and lowercase letters
    has_upper_lower_case = any(char.isupper() for char in password) and any(char.islower() for char in password)
    
    # Check if the password meets the minimum length requirement (8 characters)
    meets_length_requirement = len(password) >= 8
    
    # Check if the password contains special characters
    has_special_characters = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    # Count how many criteria are met
    met_criteria_count = sum([has_numbers, has_upper_lower_case, meets_length_requirement, has_special_characters])
    
    # Classify the password based on the number of met criteria
    if met_criteria_count == 4:
        return "Password Strength Level: Very Strong (All criteria are met)."
    elif met_criteria_count == 3:
        return "Password Strength Level: Moderately Strong (Three criteria are met)."
    elif met_criteria_count == 2:
        return "Password Strength Level: Strong (Two criteria are met)."
    else:
        return "Password Strength Level: Weak (Fewer than two criteria are met)."

# Prompt user to input password securely (it will not show on the screen)
password_input = getpass.getpass("Enter your password: ")

# Mask the password for display, showing the first and last characters, masking the rest
masked_password = password_input[0] + '#' * (len(password_input) - 2) + password_input[-1]

# Assess the password's strength
result = assess_password_strength(password_input)

# Output the masked password and the result of the strength assessment
print(f"\nEntered Password: {masked_password}")
print(f"\n{result}\n")

# Provide tips for creating a stronger password
tips = [
    "Here are some quick tips for creating a secure password:",
    "1. Length: Aim for at least 12 characters.",
    "2. Mix Characters: Use a combination of uppercase, lowercase, numbers, and symbols.",
    "3. Avoid Common Words: Don't use easily guessable information.",
    "4. No Personal Info: Avoid using names, birthdays, or personal details.",
    "5. Use Passphrases: Consider combining multiple words or a sentence.",
    "6. Unique for Each Account: Don't reuse passwords across multiple accounts.",
    "7. Regular Updates: Change passwords periodically.",
    "8. Enable 2FA: Use Two-Factor Authentication where possible.",
    "9. Be Wary of Phishing: Avoid entering passwords on suspicious sites.",
    "10. Password Manager: Consider using one for secure and unique passwords."
]

# Print out password security tips
for tip in tips:
    print(tip)
