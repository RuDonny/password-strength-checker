import getpass
import re

COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "abc123",
    "letmein",
    "admin",
    "welcome",
    "iloveyou",
}

COMMON_SEQUENCES = (
    "1234",
    "abcd",
    "qwerty",
    "password",
)


def check_password(password):
    """Evaluate a password and return its score and recommendations."""
    score = 0
    feedback = []

    if len(password) >= 16:
        score += 35
    elif len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
    else:
        feedback.append("Use at least 12 characters; 16 or more is better.")

    if re.search(r"[a-z]", password):
        score += 10
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 10
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 10
    else:
        feedback.append("Add numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
    else:
        feedback.append("Add symbols.")

    if len(set(password)) >= 10:
        score += 10
    else:
        feedback.append("Use a wider variety of characters.")

    if password.lower() in COMMON_PASSWORDS:
        score -= 40
        feedback.append("This password appears in the common-password list.")

    if any(sequence in password.lower() for sequence in COMMON_SEQUENCES):
        score -= 15
        feedback.append("Avoid common words and predictable sequences.")

    if re.search(r"(.)\1{2,}", password):
        score -= 10
        feedback.append("Avoid repeating the same character three or more times.")

    score = max(0, min(score, 100))

    if score >= 80:
        rating = "STRONG"
    elif score >= 60:
        rating = "GOOD"
    elif score >= 40:
        rating = "WEAK"
    else:
        rating = "VERY WEAK"

    return score, rating, feedback


def main():
    print("Password Strength Checker")
    print("Your password will not be displayed or stored.\n")

    password = getpass.getpass("Enter a password to evaluate: ")
    score, rating, feedback = check_password(password)

    print("\nSecurity assessment")
    print(f"Score:  {score}/100")
    print(f"Rating: {rating}")

    if feedback:
        print("\nRecommendations:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("\nNo basic weaknesses were detected.")

    print(
        "\nNote: A strong score does not prove that a password has never "
        "appeared in a data breach."
    )


if __name__ == "__main__":
    main()
