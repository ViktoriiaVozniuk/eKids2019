import random

questions = ["What is your name ?","How old are you ?","What are you doing ?"]
random.shuffle (questions)

answers = ["Riko","15","I play football !"]
random.shuffle (answers)

for item in range (3):

    print ( "girl: " + questions[item])
    print ( "Riko: " + answers[item])
