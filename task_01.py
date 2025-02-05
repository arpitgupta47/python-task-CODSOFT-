import random
import string

def generate_password():
    print("Welcome to Password Generator!")
    
    try:
    
        length = int(input("Enter desired password length: "))
        
        if length < 8:
            print("\nWarning: Passwords shorter than 8 characters are not recommended.")
            proceed = input("Do you want to continue? (y/n): ").lower()
            if proceed != 'y':
                return "Password generation cancelled."
        
       
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        numbers = string.digits
        symbols = string.punctuation
        
       
        print("\nSelect character types to include:")
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
      
        if not any([use_lower, use_upper, use_numbers, use_symbols]):
            return "Error: At least one character type must be selected!"
        
        
        char_pool = ''
        if use_lower:
            char_pool += lowercase
        if use_upper:
            char_pool += uppercase
        if use_numbers:
            char_pool += numbers
        if use_symbols:
            char_pool += symbols
        
      
        password = []
        
      
        if use_lower:
            password.append(random.choice(lowercase))
        if use_upper:
            password.append(random.choice(uppercase))
        if use_numbers:
            password.append(random.choice(numbers))
        if use_symbols:
            password.append(random.choice(symbols))
        
        
        while len(password) < length:
            password.append(random.choice(char_pool))
        
       
        random.shuffle(password)
        
       
        final_password = ''.join(password)
        
        return f"\nYour generated password is: {final_password}"
    
    except ValueError:
        return "Error: Please enter a valid number for password length!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def password_strength(password):
    """Evaluate password strength"""
    score = 0
    feedback = []
    
    
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short")
    
    
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers")
    
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add symbols")
    
    
    if score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"
    
    return strength, feedback


if __name__ == "__main__":
    while True:
        result = generate_password()
        print(result)
        
        if not result.startswith("Error"):
            
            password = result.split(": ")[1]
            strength, feedback = password_strength(password)
            print(f"\nPassword Strength: {strength}")
            if feedback:
                print("Suggestions to improve strength:")
                for suggestion in feedback:
                    print(f"- {suggestion}")
        
        again = input("\nGenerate another password? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using Password Generator!")
            break