question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
             "you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
     "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class Question :
    def __init__(self, question, text):
        self.question = question
        self.text = text

data_machine = []
for i in question_data:
    question_text = i['text']
    question_answer = i['answer']
    data_machine = Question(question_text, question_answer)

class QuizBrain :
    def __init__(self, data_list):
        self.number = 0
        self.list = data_list

    def quiz(self):
        answer = input(f'{self.list}는?')

QuizBrain(data_machine).quiz()
