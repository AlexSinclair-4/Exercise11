from quizmain import ChoiceQuestion

def main():
    first = ChoiceQuestion()
    first.setText("What is 10 x 2")
    first.addChoice("2", False)
    first.addChoice("20", True)
    first.addChoice("5", False)

    second = ChoiceQuestion()
    second.setText("What is 25 x 3")
    second.addChoice("50", False)
    second.addChoice("80", False)
    second.addChoice("75", True)

    third = ChoiceQuestion()
    third.setText("What is 5 x 5")
    third.addChoice("30", False)
    third.addChoice("25", True)
    third.addChoice("20", False)

    fourth = ChoiceQuestion()
    fourth.setText("What is 20 x 3")
    fourth.addChoice("70", False)
    fourth.addChoice("60", True)
    fourth.addChoice("55", False)

    fifth = ChoiceQuestion()
    fifth.setText("What is 365 x 14")
    fifth.addChoice("5110", True)
    fifth.addChoice("5090", False)
    fifth.addChoice("4990", False)
    fifth.addChoice("What am I a calculator?", True)

    presentQuestion(first)
    presentQuestion(second)
    presentQuestion(third)
    presentQuestion(fourth)
    presentQuestion(fifth)


def presentQuestion(q):
    q.display()
    response = input("Your Answer: ")
    print(q.checkAnswer(response))

main()