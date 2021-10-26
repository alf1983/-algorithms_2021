"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class BaseTaskBoard:
    def __init__(self):
        self.tasks = []
        self.revision = []

    def is_empty(self):
        return self.tasks == []

    def to_queue(self, item):
        self.tasks.insert(0, item)

    def _to_queue_revision(self, item):
        self.revision.insert(0, item)

    def from_queue(self, to_revision=False):
        if to_revision:
            self._to_queue_revision(self.tasks.pop())
            return
        return self.tasks.pop()

    def from_queue_revision(self):
        return self.revision.pop()

    def size(self):
        return len(self.tasks)


if __name__ == '__main__':
    task_board = BaseTaskBoard()
    tasks = ["задача1", "задача2", "задача3", "задача4", "задача5", "задача6", "задача7", "задача8", "задача9"]
    for task in tasks:
        task_board.to_queue(task)
    print(task_board.from_queue())
    task_not_resolved = True
    if task_not_resolved is not False:
        task_board.from_queue(task_not_resolved)
    print(task_board.from_queue_revision())

