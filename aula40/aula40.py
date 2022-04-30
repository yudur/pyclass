"""
Sistema de perguntas e respostas com dicionário em python
"""
questions = {
    'question 1': {
        'question': 'quantos oceanos existem no mundo?',
        'answer': {
            'a': 'existem 3',
            'b': 'existem 5',
            'c': 'existem 2',
            'd': 'existem 6'
        },
        'correct_answer': 'b'
    },

    'question 2': {
        'question': 'em que ano surgiu o modernismo?',
        'answer': {
            'a': '1922',
            'b': '1879',
            'c': '1856',
            'd': '1920'
        },
        'correct_answer': 'a'

    },

    'question 3': {
        'question': 'Qual é o feminino de cavaleiro?',
        'answer': {
            'a': 'cavaleira',
            'b': 'amazona',
            'c': 'guerreira',
            'd': 'espadachim'
        },
        'correct_answer': 'b'
    },

    'question 4': {
        'question': 'qual desses carros é o mais potente?',
        'answer': {
            'a': 'Chevrolet Onix ',
            'b': 'Ford Ka SE Plus',
            'c': 'Citroën C3 Attraction',
            'd': 'McLaren Senna'
        },
        'correct_answer': 'd'
    },

    'question 5': {
        'question': 'qual o maior continente do mundo?',
        'answer': {
            'a': 'América',
            'b': 'Africa',
            'c': 'Ásia',
            'd': 'Europa'
        },
        'correct_answer': 'c'

    }
}

print('........escolha apenas uma das opções em colchete para cada resposta........')
print()

right_answers = 0

for pk, pv in questions.items():
    print(f'{pk}: {pv["question"]}')

    for solution_k, solution_v in pv["answer"].items():
        print(f'({solution_k}) {solution_v}')

    user_response = input('digite sua resposta: ')

    if user_response == pv['correct_answer']:
        print('parabéns você acertou!!!')
        right_answers += 1
    else:
        print('Ahh você errou!!!')

    print()

number_of_questions = len(questions)
percentage_of_hits = right_answers / number_of_questions * 100

if percentage_of_hits >= 50:
    print(f'parabéns você acertou {right_answers} questões isso é igual a {percentage_of_hits}% das perguntas')
else:
    print(f'que pena você acertou apenas {percentage_of_hits}% das perguntas')
