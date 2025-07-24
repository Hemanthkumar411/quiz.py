def quiz():
    quiz_data = [
        {
            "question": "How many runs did Virat Kohli score in the 2016 IPL season?",
            "options": ["1. 851\t\t", "2. 973\n", "3. 859\t\t", "4. 967\n"],
            "answer": 2
        },
        {
            "question": "How many IPL trophies does MI have?",
            "options": ["1. 1", "2. 3", "3. 9", "4. 5"],
            "answer": 4
        },
        {
            "question": "who has the highest individual score at IPL?",
            "options": ["1.Brandum Mcclum","2.Virat Kohli","3. Chris Gayle","4.Suresh Raina"],
            "answer": 3
        },
        {
            "question": "who won orange cap in ipl 2016?",
            "options": ["1.Chris Gayle","2. Virat Kohli","3.David Warner","4.Robbin Utthappa"],
            "answer": 2
        },
        {
            "question": "which player is called as Mr 360 in cricket?",
            "options": ["1.Surya Kumar Yadav","2. Jos Buttler","3.Ben Strokes","4.AB de villiers"],
            "answer": 4
        },
        {
            "question": "in which year was IPL introduced?",
            "options": ["1.2007","2.2008","3.2009","4.2010"],
            "answer": 2
        },
        {
            "question": "for which IPL team Virat Kohli is playing for?",
            "options": ["1.RCB","2.CSK","3.MI","4.DC"],
            "answer": 1
        },
        {
            "question": "which two teams got banned in 2016-2017 IPL season?",
            "options": ["1. CSK&SRH","2.CSK&MI","3.SRH&RR","4.CSK&RR"],
            "answer": 4
        },
        {
            "question": "Who captained CSK in 2008?",
            "options": ["1.MS dhoni","2. Mathew Hayden","3. Stephen Flemmings","4.Suresh Raina"],
            "answer": 1
        },
        {
            "question": "Which team won the first ever IPL?",
            "options": ["1.CSK","2.RCB","3.RR","4.KKR"],
            "answer": 3
        },
    ]

    levels = [100,200,300,400,500,600,700,800,900,1000]
    amount = 0
    count = 0  

    for i in range(len(quiz_data)):
        current_question = quiz_data[i] 

        print(f"Question {i+1}: {current_question['question']}\n") 
        for opt in current_question['options']: 
            print(opt)
        
        try:
            user_option = int(input("Enter your option number"))
        except ValueError:
            print("not a valid option")
            break 
            
        if user_option == current_question['answer']: 
            print(f"congradulations, you have won {levels[i]}\n")
            count += 2
            print(f"total points:{count}\n")
            
            if(i==3):
                amount=400
            elif(i==6):
                amount=700
            elif(i==9):
                amount=1000
                
        else:
            print("wrong answer")
            count = count - 1 
            print(f"total points:{count}\n")
            break 
            
    print(f"Game over! Your total winnings: ₹{amount}") 
print("enter only the numbers from 1 to 4 for options\n")
quiz()