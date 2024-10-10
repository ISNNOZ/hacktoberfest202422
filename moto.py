
---

### `password_checker.py`

```python
import re

def check_password_strength(password):
    strength_score = 0
    strength_criteria = {
        "length": len(password) >= 8,
        "uppercase": re.search(r'[A-Z]', password),
        "lowercase": re.search(r'[a-z]', password),
        "numbers": re.search(r'[0-9]', password),
        "special_chars": re.search(r'[@$!%*?&#]', password)
    }
    
    # Evaluate password strength based on the criteria
    for key, value in strength_criteria.items():
        if value:
            strength_score += 1

    # Provide feedback on password strength
    if strength_score <= 2:
        return "Weak"
    elif strength_score == 3 or strength_score == 4:
        return "Medium"
    else:
        return "Strong"

if __name__ == "__main__":
    password = input("Enter your password to check its strength: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")
