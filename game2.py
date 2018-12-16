from quiz import Question

question_prompts = [
    'What is Eutrophication \n (a) Excess nutrients in the ocean \n (b) Excess nutrients in the lake/ponds \n (c) a solar flare',
    'What is red tides \n (c) Excess nutrients in the ocean \n (b) Excess nutrients in the lake/ponds \n (a) a red ocean',
    'What is one of the cause of eutrophication \n (a) fertilizers \n (b) sewers \n acid rain',
    'What are plant nutrients most beneficial for \n (b) algae \n (a) fish \n (c) whales',
    'Why does eutrophication occur \n (a) excess pollution \n (b) fertilizers \n (c) ewaste',
    'Which thing causes red tides \n  (c) dinoflagellate \n (b) algae \n (a) land plants',
    'What is the ultimate result of eutrophication \n (a) the lake/ponds becomes anaroxic \n (b) the lake/ponds gains more oxygen \n (c) fishes get larger',
    'what is the ultimate result of red tides \n (a) the ocean becomes anaroxic \n (b) the sealevel rises \n (c) sharks get feet',
    'Why are red tides bad \n (a) they kill ocean life \n (b) they take the oceans oxygen away \n (c) all ',
    'Eutrophication has increased due to human involvement \n (a) true \n (b) false ',

]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "c"),
    Question(question_prompts[9], "a"),

]


def eu_questions(questions):
    score = 0
    for questions in questions:
        answer = input(questions.prompt)
        if answer == questions.answer:
            score += 100
    print("You got "
          "{0}/{1}correct".format(str(score), str(questions))
          )


eu_questions(questions)
