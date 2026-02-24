import time
import random

# --- The Color Lab ---
PURPLE = '\033[95m'
CYAN = '\033[96m'
GOLD = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'

print(f"{PURPLE}{BOLD}🛠️  ULTIMATE PROFILE ARCHITECT v3.0 🛠️{RESET}")

# 1. Inputs with a twist
name = input(f"{CYAN}👉 Enter your Name: {RESET}")
hobby = input(f"{CYAN}👉 Enter your favorite hobby: {RESET}")
energy = int(input(f"{CYAN}👉 Energy Level (1-10): {RESET}"))

# 2. Secret Logic (The "Something Extra")
titles = ["The Code Whisperer", "The Midnight Logic-Lord", "The Bug Hunter", "The Pythonic Legend"]
secret_title = titles[len(name) % len(titles)] # Picks a title based on name length!

# 3. Create the Visual Skill Bar
skill_bar = "▰" * energy + "▱" * (10 - energy)

# 4. The Grand Bio Construction
bio = f"""
╔══════════════════════════════════════════════════════╗
  🚀 DESTINY PROFILE: {name.upper()} 🚀
╚══════════════════════════════════════════════════════╝

🏷️  SECRET TITLE: {secret_title}
✨  SPIRIT VIBE:  {hobby} Enthusiast

[📊 LIFE STATS]
  ENERGY:  [{skill_bar}] {energy*10}%
  BRAIN:   [▰▰▰▰▰▰▰▰▰▱] 90% (Coding...)
  LUCK:    [▰▰▰▱▱▱▱▱▱▱] 30% (Debugging)

[📜 THE MISSION]
  "To master the syntax of the universe and turn 
   {hobby} into a digital masterpiece."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💎 SYSTEM STATUS: 100% AWESOME
📅 SYNC DATE: {time.ctime()}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# 5. Saving with "The Sound of Success"
print(f"\n{GOLD}💾 Compiling your atoms into the file...{RESET}")
time.sleep(1)

try:
    with open("profile.txt", "w", encoding="utf-8") as file:
        file.write(bio)
    
    # This makes a small "Beep" sound on most Windows computers!
    print("\a") 
    
    print(f"{GREEN}{BOLD}🎉 BOOM! It is done!{RESET}")
    print(f"{PURPLE}Check your folder for the most beautiful 'profile.txt' ever.{RESET}")
    
    # Showing a preview of the "Secret Title"
    print(f"\n{CYAN}Psst... your Secret Title is: {BOLD}{secret_title}{RESET}")

except Exception as e:
    print(f"{RED}💥 A glitch in the matrix: {e}{RESET}")
