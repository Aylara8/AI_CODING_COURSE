# Initialize a variable to control the loop
is_strong = False

print("--- Password Security Setup ---")

# The loop keeps running as long as is_strong is False
while not is_strong:
    pwd = input("\nEnter a strong password: ")
    
    # We start by assuming the password is valid, then try to find reasons it's not
    has_error = False
    
    # Check 1: Length
    if len(pwd) < 8:
        print("❌ Too short! Must be at least 8 characters.")
        has_error = True
        
    # Check 2: Contains a digit
    # any() checks if any character in the password is a digit
    if not any(char.isdigit() for char in pwd):
        print("❌ Must contain at least one number (0-9).")
        has_error = True
        
    # Check 3: Contains uppercase
    if not any(char.isupper() for char in pwd):
        print("❌ Must contain at least one uppercase letter (A-Z).")
        has_error = True

    # Final check: If no errors were found, we break the loop
    if not has_error:
        print("✅ Success! Your password is secure.")
        is_strong = True
    else:
        print("Please try again.")

# I used while for passwords because I have an unknown duration.