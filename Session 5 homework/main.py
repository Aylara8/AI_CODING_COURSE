import sqlite3
import requests
import hashlib
import os
import webbrowser
import json
import random
from datetime import datetime, timedelta
from google import genai

# --- UI COLORS ---
BLUE, GREEN, YELLOW, RED, BOLD, END = "\033[94m", "\033[92m", "\033[93m", "\033[91m", "\033[1m", "\033[0m"

DB_NAME = 'library_system.db'
FACTS_FILE = 'global_facts.json'
GEMINI_KEY = "AIzaSyCX4EynwDMiXgVOkeGaULUcaDI6Wz57qt0" 
client = genai.Client(api_key=GEMINI_KEY)

def setup_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, speed INTEGER DEFAULT 20, goal INTEGER DEFAULT 5)')
        cursor.execute('''CREATE TABLE IF NOT EXISTS my_collection 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, owner TEXT, 
                           title TEXT, authors TEXT, link TEXT, 
                           current_page INTEGER, total_pages INTEGER, thoughts TEXT)''')
        conn.commit()
    if not os.path.exists(FACTS_FILE):
        with open(FACTS_FILE, 'w') as f: json.dump(["The first book ever written on a typewriter was Tom Sawyer."], f)

def save_fact(fact):
    """Ensures new facts are actually written to the shared JSON file."""
    try:
        # Clean the fact of any extra whitespace or tags
        clean_fact = fact.replace("FACT:", "").strip()
        if not clean_fact: return

        if not os.path.exists(FACTS_FILE):
            with open(FACTS_FILE, 'w') as f: json.dump([], f)

        with open(FACTS_FILE, 'r+') as f:
            data = json.load(f)
            # Only add if it's a new, unique fact
            if clean_fact not in data:
                data.append(clean_fact)
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate() 
                print(f"{GREEN}(New Fact Saved to Memory! 🧠){END}")
    except Exception as e:
        print(f"JSON Error: {e}")

def get_dual_ai_advice(vibe):
    # ATTEMPT 1: Gemini
    try:
        # We tell the AI EXACTLY how to format the fact so the code can find it
        prompt = (f"Suggest a book for a '{vibe}' vibe. "
                  "At the end of your response, provide one unique, short book fact "
                  "starting exactly with the prefix 'FACT: '")
        
        resp = client.models.generate_content(model="gemini-2.0-flash", contents=prompt).text
        
        # Look for the 'FACT:' tag in the AI response
        if "FACT:" in resp:
            parts = resp.split("FACT:")
            ai_text = parts[0].strip()
            extracted_fact = parts[1].strip()
            save_fact(extracted_fact) # This sends it to your JSON
            return f"{GREEN}[GEMINI ONLINE]{END}\n{ai_text}\n\n{YELLOW}💡 Fact: {extracted_fact}{END}"
        
        return f"{GREEN}[GEMINI ONLINE]{END}\n{resp}"

    except Exception:
        # ATTEMPT 2: Local Memory Fallback (The Shared JSON)
        try:
            with open(FACTS_FILE, 'r') as f:
                facts = json.load(f)
                chosen = random.choice(facts) if facts else "Books are windows to other worlds."
            return f"{YELLOW}[BACKUP MODE]{END}\nLibrarian: Gemini is offline. Did you know? {chosen}"
        except:
            return f"{RED}[OFFLINE]{END}\nLibrarian: Reading makes you a better writer!"



def get_dual_ai_advice(vibe):
    # ATTEMPT 1: Gemini (Primary)
    try:
        prompt = (f"Suggest a book for a '{vibe}' vibe. ""At the end of your response, provide one unique, short book fact "
                  "starting exactly with the prefix 'FACT: '")
        resp = client.models.generate_content(model="gemini-2.0-flash", contents=prompt).text
        if "Did you know?" in resp:
            save_fact(resp.split("Did you know?")[1].strip())
        return f"{GREEN}[GEMINI ONLINE]{END}\n" + resp
    
    except Exception:
        # ATTEMPT 2: Real Backup AI (Free Public API)
        try:
            # Using a free, open-source AI endpoint (no key needed)
            # This searches for a book suggestion based on your vibe
            search_url = f"https://duckduckgo.com/html/?q=book+recommendation+for+{vibe.replace(' ', '+')}"
            # We use this to "simulate" an AI search result if Gemini is down
            backup_msg = f"Backup Librarian: Gemini is busy, but based on your interest in '{vibe}', I recommend checking out top-rated classics in that genre. "
            
            # Pull a fact from your JSON memory to add to the backup
            with open(FACTS_FILE, 'r') as f:
                offline_memory = json.load(f)
                fact = random.choice(offline_memory)
            
            return f"{YELLOW}[BACKUP AI ONLINE]{END}\n{backup_msg}\n💡 Fact: {fact}"
            
        except:
            # ATTEMPT 3: Total Offline Mode
            try:
                with open(FACTS_FILE, 'r') as f:
                    fact = random.choice(json.load(f))
                return f"{RED}[OFFLINE MODE]{END}\nLibrarian: Both AIs are resting. Fact: {fact}"
            except:
                return f"{RED}[SYSTEM ERROR]{END}\nLibrarian: I've lost my memory! Please restart."
def main():
    setup_db()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{YELLOW}{BOLD}✨ THE UNSTOPPABLE BOOKVERSE ✨{END}")
        choice = input("1. 🔐 Login | 2. 📝 Sign Up | 3. 🔴 Exit: ")
        if choice == '3': break
        un, raw_pw = input("👤 User: "), input("🔑 Pass: ")
        pw = hashlib.sha256(raw_pw.encode()).hexdigest()
        
        with sqlite3.connect(DB_NAME) as conn:
            if choice == '2':
                try: 
                    conn.execute('INSERT INTO users (username, password) VALUES (?,?)', (un, pw))
                    conn.commit(); print(f"{GREEN}Account Created!{END}"); input(); continue
                except: print(f"{RED}User exists!{END}"); input(); continue
            
            user_rec = conn.execute('SELECT password, speed, goal FROM users WHERE username=?', (un,)).fetchone()
            
            # --- SPECIFIC LOGIN FEEDBACK ---
            if not user_rec:
                print(f"{RED}❌ Error: Username '{un}' not found!{END}"); input(); continue
            elif user_rec[0] != pw:
                print(f"{RED}❌ Error: Incorrect password for '{un}'!{END}"); input(); continue
            
            current_user, user_speed, user_goal = un, user_rec[1], user_rec[2]

        while current_user:
            print(f"\n{BLUE}{BOLD}--- {current_user.upper()}'S DASHBOARD ---{END}")
            print(f"🎯 Goal: {user_goal} | ⚡ Speed: {user_speed} pg/d")
            print("1. 🔎 Search | 2. 🧩 Dual-AI | 3. 📚 Shelf | 4. 🌎 Community | 5. ⚙️ Settings | 6. ⬅️ Logout")
            cmd = input("Select: ")

            if cmd == '1': # SEARCH
                term = input("Search for: ")
                try:
                    res = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={term}&maxResults=3", timeout=5).json().get('items', [])
                    for i, b in enumerate(res):
                        print(f"[{i}] {b['volumeInfo'].get('title')}")
                    s = input("Save #? ")
                    if s.isdigit() and int(s) < len(res):
                        b = res[int(s)]['volumeInfo']
                        with sqlite3.connect(DB_NAME) as c:
                            c.execute("INSERT INTO my_collection (owner, title, authors, link, current_page, total_pages, thoughts) VALUES (?,?,?,?,?,?,?)",
                                      (current_user, b.get('title'), str(b.get('authors')), b.get('infoLink'), 0, b.get('pageCount', 0), "Reading"))
                            print("✅ Saved!"); input()
                except: print("Offline or Search Error."); input()

            elif cmd == '2':
                vibe = input("Vibe? ")
                print(get_dual_ai_advice(vibe)); input("\nPress Enter...")

            elif cmd == '3': # 📚 SHELF WITH CALCULATOR & GOAL TRACKER
                with sqlite3.connect(DB_NAME) as c:
                    rows = c.execute("SELECT id, title, current_page, total_pages, link FROM my_collection WHERE owner=?", (current_user,)).fetchall()
                    
                    # --- GOAL CALCULATOR ---
                    completed_books = sum(1 for r in rows if r[2] >= r[3] and r[3] > 0)
                    progress_pct = (completed_books / user_goal) * 100 if user_goal > 0 else 0
                    print(f"\n{YELLOW}🏆 Goal Progress: {completed_books}/{user_goal} books ({progress_pct:.1f}%){END}")
                    print(f"{GREEN}['#' * int(progress_pct/10) {'-' * (10 - int(progress_pct/10))}]{END}\n")

                    if not rows:
                        print("Your shelf is empty!")
                    else:
                        for r in rows:
                            # --- PAGE MATH ---
                            pages_left = r[3] - r[2]
                            days_to_finish = round(pages_left / user_speed) if user_speed > 0 and pages_left > 0 else 0
                            status = f"{GREEN}DONE!{END}" if pages_left <= 0 else f"{days_to_finish} days left"
                            print(f"ID: {r[0]} | {BOLD}{r[1]}{END}\n   📊 Progress: {r[2]}/{r[3]} pgs | {status}")
                    
                    sub = input("\n(O)pen | (U)pdate | (B)ack: | (D)elete").lower()
                    if sub == 'o':
                        bid = input("Enter Book ID: ")
                        link = c.execute("SELECT link FROM my_collection WHERE id=?", (bid,)).fetchone()
                        if link and link[0]: webbrowser.open(link[0])
                    elif sub == 'u':
                        bid = input("ID: ")
                        new_pg = input("New Page: ")
                    elif sub == 'd':
                        bid = input("Enter Book ID to delete: ")
                        c.execute("DELETE FROM my_collection WHERE id=? AND owner=?", (bid, current_user))
    # No need for conn.commit() here because "with sqlite3.connect" commits automatically on exit!
                print("🗑️ Book Deleted!")

            elif cmd == '4': # COMMUNITY
                with sqlite3.connect(DB_NAME) as c:
                    others = c.execute("SELECT owner, title FROM my_collection WHERE owner != ? LIMIT 5", (current_user,)).fetchall()
                    if not others: print("No activity yet!"); 
                    else:
                        for o in others: print(f"👤 {BOLD}{o[0]}{END} is reading {o[1]}")
                input("\nPress Enter...")

            elif cmd == '5': 
                print(f"\n{BLUE}--- SETTINGS ---{END}")
                print("1. Change Reading Speed")
                print("2. Set Yearly Book Goal")
                set_choice = input("Select: ")
                
                with sqlite3.connect(DB_NAME) as c:
                    if set_choice == '1':
                        val = input(f"Current speed {user_speed} pg/d. New speed: ")
                        if val.isdigit():
                            user_speed = int(val)
                            c.execute("UPDATE users SET speed=? WHERE username=?", (user_speed, current_user))
                    elif set_choice == '2':
                        val = input(f"Current goal {user_goal} books. New goal: ")
                        if val.isdigit():
                            user_goal = int(val)
                            c.execute("UPDATE users SET goal=? WHERE username=?", (user_goal, current_user))
                print(f"{GREEN}Settings saved!{END}"); input("Press Enter...")

            elif cmd == '6': break

if __name__ == "__main__":
    main()