"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefa
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
"""
from colorama import Fore


def del_ref():
    if task_name == 'del':
        last_item_deleted.append(tasks[-1])
        tasks.pop(-1)

    elif task_name == 'ref':

        tasks.append(last_item_deleted[-1])
        last_item_deleted.pop(-1)


last_item_deleted = []
tasks = []

print(Fore.RED + 'del: deleta o ultimo item da lista de tarefas',
      Fore.GREEN + '\nref: refaz o ultimo item apagado\n')


while True:
    try:
        print()
        task_name = input(Fore.BLUE + 'digite a tarefa: ' + Fore.RESET)

        if task_name == 'del' or task_name == 'ref':
            del_ref()
        else:
            tasks.append(task_name)

        print(f'\t{tasks}')

    except IndexError:
        print(Fore.RED + '\tERROR')
