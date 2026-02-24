import datetime
import random
import os
import webbrowser

def favorite_things_journal():
    print("✨" * 25)
    print("   🌟 AYLAR'S SECURE MULTIVERSE JOURNAL 🌟")
    print("✨" * 25)
    
    name = input("Hi! I'm your AI Journal. What is your name? ").strip()
    
    # --- Advanced Security ---
    password_file = "secret.txt"
    if not os.path.exists(password_file):
        print(f"Welcome {name}! Let's set a master password to protect your files.")
        new_pw = input("Create your secret password: ")
        with open(password_file, "w") as f: f.write(new_pw)
        print("Password locked! 🔒")
    else:
        with open(password_file, "r") as f: saved_pw = f.read().strip()
        attempt = input(f"Enter your secret password to unlock your journal: ")
        if attempt != saved_pw:
            print("❌ ACCESS DENIED! You cannot view or update this journal.")
            return # Stops the code immediately

    print(f"\n✅ Welcome back, {name}! Your tastes are evolving...")

    # --- Data Collection ---
    journal = {
        "Color": "",
        "Food": "",
        "Movie": "",
        "Book": {"title": "", "author": ""},
        "Place": "",
        "Music": {"song": "", "artist": ""} 
    }

    # Diverse reactions
    reactions = ["Your style is legendary!", "I love how your taste changes!", "That's a classic!", "Wow, sounds interesting!"]

    for key in journal.keys():
        if key == "Music":
            song = input("What's your  favorite song? ")
            artist = input(f"Who sings '{song}'? ")
            journal["Music"] = {"song": song, "artist": artist}
        elif key == "Book":
            title = input("What's your favorite book? ")
            author = input(f"Who wrote '{title}'? ")
            journal["Book"] = {"title": title, "author": author}
        else:
            journal[key] = input(f"What is your favorite {key} today? ")
        
        print(f"✨ {random.choice(reactions)}")
        print("~" * 20)

    # --- Search Link Generation ---
    m_query = f"{journal['Music']['artist']} {journal['Music']['song']}".replace(" ", "+")
    music_url = f"https://www.youtube.com/results?search_query={m_query}"

    mov_query = journal["Movie"].replace(" ", "+") + "+trailer"
    movie_url = f"https://www.google.com/search?q={mov_query}"

    b_query = f"{journal['Book']['title']} {journal['Book']['author']}".replace(" ", "+")
    book_url = f"https://www.google.com/search?q={b_query}+book+summary"

    # --- Saving with 'APPEND' Mode ('a') ---
    current_time = datetime.datetime.now().strftime("%B %d, %Y (%I:%M %p)")
    filename = f"{name}_permanent_journal.txt"

    try:
        # 'a' mode adds to the file without deleting old data
        with open(filename, "a", encoding="utf-8") as file:
            file.write("\n" + "◈" * 50 + "\n")
            file.write(f"  📅 NEW ENTRY: {current_time}\n")
            file.write(f"  Note: {name}'s taste is growing!\n")
            file.write("◈" * 50 + "\n")
            
            for key, value in journal.items():
                if key == "Music":
                    file.write(f"🎵 MUSIC: {value['song']} by {value['artist']}\n   🔗 Listen: {music_url}\n")
                elif key == "Book":
                    file.write(f"📚 BOOK: {value['title']} by {value['author']}\n   🔗 Read Summary: {book_url}\n")
                elif key == "Movie":
                    file.write(f"🎬 MOVIE: {value}\n   🔗 Trailer: {movie_url}\n")
                else:
                    file.write(f"⭐ {key.upper()}: {value}\n")
            
            file.write("-" * 50 + "\n")
                
        print(f"\n🎉 Success! Your new favorites have been added to '{filename}'.")
        print("The old information is still safe at the top of the file!")

        # Quick Launch Menu
        print("\nWhat would you like to do?")
        print("1. Music  |  2. Movie Trailer  |  3. Book Info  |  4. Just Exit")
        go = input("Choice: ")
        if go == "1": webbrowser.open(music_url)
        elif go == "2": webbrowser.open(movie_url)
        elif go == "3": webbrowser.open(book_url)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    favorite_things_journal()

#Prompt
#Write code for python according to these instructions.
#maybe add favourite music and and in my journal i can listen that too , is it possible to do that 
#add book side too so i can read and after running again code don't delete previous information just say you taste is changing and write new inside that file and nobody without password can't open that file and update that file
