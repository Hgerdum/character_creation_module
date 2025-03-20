from datetime import datetime as dt
import time


class Quest():
    def __init__(self, name, goal, discription):
        self.name = name
        self.goal = goal
        self.discription = discription
        self.start_time = None
        self.end_time = None
        print(name)
        print(goal)
        print(discription)

    def accept_quest(self):
        if self.end_time == None:
            self.start_time = dt.now()
            print(f'Начало "{self.name}" положено.')
            return self.start_time
        else:
            print('С этим испытанием вы уже справились.')

    def pass_quest(self):
        if self.start_time:
            self.end_time = dt.now()
            complete_time = self.end_time - self.start_time
            print(f'Квест "{self.name}" окончен. Время выполнения квеста: '
                  f'{complete_time}')
            return self.end_time
        else:
            print('Нельзя завершить то, что не имеет начала!')


quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''

# Создайте экземпляр класса Quest.
new_quest = Quest(quest_name, quest_goal, quest_description)

new_quest.pass_quest()
new_quest.accept_quest()
time.sleep(3)
new_quest.pass_quest()
new_quest.accept_quest()
