import datetime

def run_calculator():
    print("--- Simple Calculator with Memory ---")
    
    # 1. Get two numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    # 2. Perform calculations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    
    # Handle division by zero
    if num2 != 0:
        division = num1 / num2
        div_result = f"{division:.2f}" # Format to 2 decimal places
    else:
        div_result = "Undefined (Cannot divide by zero)"

    # 3. Format the output for display and file
    # We use f-strings for clean formatting. 
    # :.2f tells Python to show only 2 decimal places.
    output_lines = [
        f"Addition:       {num1} + {num2} = {addition:.2f}",
        f"Subtraction:    {num1} - {num2} = {subtraction:.2f}",
        f"Multiplication: {num1} * {num2} = {multiplication:.2f}",
        f"Division:       {num1} / {num2} = {div_result}"
    ]

    # Get current timestamp
    current_time = datetime.datetime.now().strftime("%b %d, %Y - %I:%M %p")
    
    # 4. Print results to screen
    print("\n--- Results ---")
    for line in output_lines:
        print(line)

    # 5. Save to file (Append mode)
    # 'a' mode stands for Append. It adds to the end without deleting old content.
    with open("calculator_history.txt", "a") as file:
        file.write(f"\n[{current_time}]\n")
        for line in output_lines:
            file.write(line + "\n")
            
    print(f"\nSaved to calculator_history.txt!")

if __name__ == "__main__":
    run_calculator()


#Prompt which I used to generate the above code:
#Write code for python according to these instructions .