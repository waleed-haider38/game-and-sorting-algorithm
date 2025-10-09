def quiz_game():
    score = 0
    
    # Questions ko list of dictionaries me store karna
    questions = [
        {
            "question": "1. What is the capital of Pakistan?",
            "options": ["a) Karachi", "b) Islamabad", "c) Lahore", "d) Multan"],
            "answer": "b"
        },
        {
            "question": "2. Which programming language is known as the 'mother of all languages'?",
            "options": ["a) Python", "b) C", "c) Java", "d) JavaScript"],
            "answer": "b"
        },
        {
            "question": "3. Who is the founder of Microsoft?",
            "options": ["a) Steve Jobs", "b) Bill Gates", "c) Elon Musk", "d) Mark Zuckerberg"],
            "answer": "b"
        }
    ]
    
    # Loop through questions
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        
        user_answer = input("Enter your answer (a/b/c/d): ").lower()
        
        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong! Correct answer was:", q["answer"])
    
    # Final score
    print("\n🎯 Your Final Score:", score, "/", len(questions))


# Run the game
quiz_game()
