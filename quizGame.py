print (" wellcome to quiz game")
print (" you will be asked 5 questions\n")
user_score=0

questions={
    "what is the national bird of BD?":{
        "A":"Doel",
        "B":"Parrot",
        "C":"Peacock",
        "D":"Eagle",
        "answer":"A"
    },
    "what is the capital of BD?":{
        "A":"Dhaka",
        "B":"Chittagong",
        "C":"Sylhet",
        "D":"Rajshahi",
        "answer":"A"
    }
    }

user_input=input('enter q to quit and s to start:').lower()
if user_input =="q":
    exit()
elif user_input=="s":
    print("lets start the quiz game\n")

    
    for question , answer in questions.items():
        print(question)
        correct=None
        
        for option,values in  answer.items():
            if option != "answer":
                print(f"{option}:{values}")
            if option=="answer":
                correct=values
        
        user_ans=input("answer: ").upper()
       
       
        if user_ans==correct:
            user_score+=1
            print("\ncorrect, new score is :",user_score)
            
        else:
            print("\nwrong , answer is :",correct)



print("\ntotal earned score is :",user_score)
print("goodbye!")