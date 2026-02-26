  I have built project "OpenShelf" which helps to people keep their any resource files for learning  on the internet for not filling destkop, and for searching other's resoursec too.
The feature I am most proud of is function edit profile cause it was hard for me to make it work 
and I wanted to remove that function but with help of AI we could fix the bug in my code.
On the other hand the most chalenged mistake was handling errors in my main app.py and making good
UI without any slip-ups. My way of overcoming errors always has been copy-pasting terminal's warning to Gemini but with UI slip-ups it was hard to do that. Therefore I had two options, first being excelent at CSS or always calling AI and explaining what I want properly. For now I am on my way to do them both but I hope one day I will use only first option.
   I have had learnt how to use github almost fully by connecting it to my VS studio, I have learnt 
how to use AI for more narrow things too, what is API and how to use it for making projects more 
interesting, About UI, javascript. The skill I have improved using virtual environment. I wanted to be more professional and learning venv and git really gave me more inspiration. The second thing I have improved app.py code understanding especially thing I had grasped hardly was some app routes especially downloading files. And as I said CSS one thing I want to improve first. AI is like friend everything that I don't understand or can't fix myself with help of AI becomes easy. How he gives clear pattern to solve any problem with understanding or bugging is incredible. 
   If compare my coding abilities which iI had 7 th Session, now it surely improved. I have always 
known what is backend and fronted but I wasn't known frontend deeply. I didn't know to build full web app with good design. Now my abilities improved web development was much more iteresting than I think tasks getting harder but it is also interesting, know when I visit other webside I open dev tool and trying to understand their code thier UI design. My next goal is being fluent in web development especially starting writing full code myself I am trying to not only understand and change but also write something, I can write simple app.py function and simple html I want to level up in that too. 
   Main function of my Chekpoint program is already added but I would add some new functions like 
community, comment rating of books and other files and functions like private shelf and OpenShelf for keeping resources. I am looking forward to improve my OpenShelf project for presenting it in final but I have other ideas too to implement. I most excited about learning Database it is really interesting and crucial for good fullstack developer which I want to be in future.
Code I am proud of:
# --- CONTEXT PROCESSOR ---
@app.context_processor
def inject_quote():
    local_quotes = [{"content": "Knowledge is power.", "author": "Francis Bacon"}]
    
    # 1. Load the history
    if os.path.exists(QUOTES_FILE):
        try:
            with open(QUOTES_FILE, 'r') as f:
                data = json.load(f)
                if data: local_quotes = data
        except: pass

    # 2. Try to get a NEW one
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=2)
        if response.status_code == 200:
            api_data = response.json()[0]
            new_quote = {"content": api_data['q'], "author": api_data['a']}
            
            # Check if we already have this quote in our JSON
            exists = any(q['content'] == new_quote['content'] for q in local_quotes)
            if not exists:
                local_quotes.append(new_quote)
                with open(QUOTES_FILE, 'w') as f:
                    json.dump(local_quotes[-15:], f, indent=4) # Keep last 15
            
            display_quote = new_quote
        else:
            # If API is busy, SHUFFLE the history so it looks different
            display_quote = random.choice(local_quotes)
    except:
        display_quote = random.choice(local_quotes)
    
    return dict(quote=display_quote)