# Write your code here
from sqlalchemy import create_engine, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta

from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///todo.db?check_same_thread=False")

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)

    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        print(self.task)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

isExit = False
while not isExit:
    print('''
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit''')
    user_input = input()

    if user_input == '1':
        today = datetime.today()
        print(f'Today {today.strftime("%b")} {today.day}:')
        tasks = session.query(Task).filter(Task.deadline == today.date()).all()
        if len(tasks) == 0:
            print('Nothing to do!')
        else:
            for i in range(0, len(tasks)):
                item = tasks[i]
                task = item.task
                print(f'{i + 1}. {task}')
    elif user_input == '2':
        today = datetime.today()
        day = today.weekday()
        # days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        # day_index = days.index(day)
        for i in range(0, 7):
            day = today + timedelta(i)
            tasks = session.query(Task).filter(Task.deadline == day.date()).all()
            day_str = day.strftime('%A %d %b')
            print(day_str+':')
            if len(tasks) == 0:
                print('Nothing to do!')
            else:
                for i in range(0, len(tasks)):
                    item = tasks[i]
                    task = item.task
                    print(f'{i + 1}. {task}')
            print()
    elif user_input == '3':
        print('All tasks: ')
        tasks = session.query(Task).order_by(Task.deadline).all()
        if len(tasks) == 0:
            print('Nothing to do!')
        else:
            for i in range(0, len(tasks)):
                item = tasks[i]
                task = item.task
                month = item.deadline.strftime("%b")
                day = item.deadline.day
                print(f'{i + 1}. {task}. {day} {month}')
    elif user_input == '5':
        new_task = input('Enter task\n')
        deadline = input('Enter deadline')
        new_row = None
        if deadline:
            strs = deadline.split('-')
            year = int(strs[0])
            month = int(strs[1])
            day = int(strs[2])
            deadline = datetime(year, month, day)
            new_row = Task(task=new_task, deadline=deadline)
        else:
            new_row = Task(task=new_task)
        session.add(new_row)
        session.commit()
        print('The task has been added!')
    elif user_input == '4':
        print("Missed tasks:")
        today = datetime.today()
        tasks = session.query(Task).filter(Task.deadline < today).order_by(Task.deadline).all()

        if len(tasks) == 0:
            print('Nothing to do!')
        else:
            for i in range(0, len(tasks)):
                item = tasks[i]
                task = item.task
                month = item.deadline.strftime("%b")
                day = item.deadline.day
                print(f'{i + 1}. {task}. {day} {month}')
    elif user_input == '6':
        today = datetime.today()
        tasks = session.query(Task).filter(Task.deadline < today).order_by(Task.deadline).all()
        if(len(tasks) == 0):
            print('Nothing to delete')
        else:
            print('Choose the number of the task you want to delete:')
            task_num = 0
            for i in range(0, len(tasks)):
                item = tasks[i]
                task = item.task
                month = item.deadline.strftime("%b")
                day = item.deadline.day
                print(f'{i + 1}. {task}. {day} {month}')

            task_num = int(input()) -1
            del_task = tasks[task_num]
            session.delete(del_task)
            session.commit()
            print('The task has been deleted!')

    elif user_input == '0':
        print('Bye!')
        isExit = True
