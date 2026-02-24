from datetime import datetime, timedelta

# 1. Get Today's Date
today = datetime.now().strftime("%b %d, %year")
# Challenge: Calculate a date 10 years into the future
future_date = (datetime.now() + timedelta(days=365*10)).strftime("%b %d, %Y")

print("--- Welcome to the 2026 Time Capsule Creator ---")

# 2. Gather Information
age = input("How old are you today? ")
song = input("What is your current favorite song? ")
goal = input("What is your biggest goal right now? ")
friend = input("Who is your best friend? ")
hobby = input("What is your favorite hobby? ")

# 3. Create the Formatted Content
# We use f-strings to build the "beautifully formatted" layout
content = f"""
╔═══════════════════════════════════════════╗
║           TIME CAPSULE - 2026             ║
║          Created: {today}            ║
╚═══════════════════════════════════════════╝

> To be opened in: {future_date}

- Current Age: {age}
- Favorite Song: {song}
- Biggest Dream: {goal}
- Best Friend: {friend}
- Current Hobby: {hobby}

---------------------------------------------
Dear future me, I hope you achieved those dreams!
---------------------------------------------
"""

# 4. Write to the file
with open("time_capsule_2026.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("\nSuccess! Your time capsule has been sealed in 'time_capsule_2026.txt'.")

#Prompt which I used to generate the above code:
#Write code for python according to these instructions .