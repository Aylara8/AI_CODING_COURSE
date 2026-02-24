def study_selector():
    print("--- Advanced Study Method Selector ---")
    
    subject = input("Subject: ").strip()
    
    print("\nTime Available:\n1. < 30m\n2. 1-2 Hours\n3. 3-5 Hours\n4. All Day")
    time = input("Select 1-4: ")

    print("\nStyle:\nA. Visual\nB. Auditory\nC. Kinesthetic\nD. Social")
    style = input("Select A-D: ").upper()

    print(f"\n--- Strategy for {subject} ---")

    # Logic Chain with Resources
    if time == "1":
        if style == "A": 
            rec = "Review a Cheat Sheet."
            link = "https://www.cheatsheet.com/"
        elif style == "B": 
            rec = "Quick Podcast Summary."
            link = "https://www.bbc.co.uk/learningenglish/english/features/6-minute-english"
        elif style == "D":
            rec = "Rapid Quiz with a Peer."
            link = "https://quizlet.com/"
        else: 
            rec = "Active Recall (Blurting)."
            link = "https://smowl.net/en/blog/active-recall/"

    elif time == "2":
        if style == "A": 
            rec = "Mind Mapping."
            link = "https://www.mindmapping.com/"
        elif style == "B": 
            rec = "The Feynman Technique."
            link = "https://todoist.com/inspiration/feynman-technique"
        elif style == "D":
            rec = "Explain a concept to a friend."
            link = "https://www.colorado.edu/artssciences-advising/the-feynman-technique"
        else: 
            rec = "Pomodoro Technique."
            link = "https://asana.com/resources/pomodoro-technique"

    elif time == "3":
        if style == "C": 
            rec = "SQ3R Method (Survey, Question, Read, Recite, Review)."
            link = "https://in.nau.edu/academic-success-centers/sq3r-reading-method/"
        else: 
            rec = "Deep Work Practice Testing."
            link = "https://www.21kschool.com/in/blog/study-methods/"

    elif time == "4":
        rec = "Spaced Repetition Marathon."
        link = "https://e-student.org/spaced-repetition/"

    else:
        rec = "Input not recognized."
        link = "N/A"

    print(f"Recommended: {rec}")
    if link != "N/A":
        print(f"Learn how to do it here: {link}")

study_selector()
