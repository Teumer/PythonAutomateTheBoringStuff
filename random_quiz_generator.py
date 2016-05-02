#! python3
# random_quiz_generator.py - Creates quizzes with questions and answers in
# random order, along with the answer key

import random

# The quiz data - keys are states and values are their capitals
capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

number_of_quizzes_to_make = 4

# Generate quiz files
for quiz_num in range(1, number_of_quizzes_to_make + 1):

    # Create quiz and answer keys files
    quiz_file = open("capitals_quiz_questions{}".format(quiz_num), "w")
    answer_file = open("capitals_quiz_answers{}".format(quiz_num), "w")

    # Write out the header for the quiz
    quiz_file.write("Name:\n\nData:\n\nPeriod:\n\n")
    quiz_file.write((" " * 20) + "State Capitals Quiz (Form {})".format(quiz_num))
    quiz_file.write("\n\n")

    # Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each
    for question_num in range(50):

        # Get right and wrong answers
        correct_answer = capitals[states[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        # Write the question and the answer options to the quiz file
        quiz_file.write("{0}. What is the capital of {1}?\n".format(
            question_num + 1,
            states[question_num]
        ))
        for i in range(4):
            quiz_file.write("    {0}. {1}\n".format(
                'ABCD'[i],
                answer_options[i]
            ))
            quiz_file.write('\n')

        # Write the answer key to a file
        answer_file.write("{0}. {1}\n".format(
            question_num + 1,
            'ABCD'[answer_options.index(correct_answer)]
        ))
    quiz_file.close()
    answer_file.close()

