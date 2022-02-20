import time 
import datetime

class my_task():
    name = None
    priority = -1
    period = -1
    execution_time = -1
    last_execution_time = None

    def __init__(self,name,priority,period,execution_time,last_execution):
        
        self.name = name
        self.priority = priority
        self.period = period 
        self.execution_time = execution_time
        self.last_execution_time = last_execution

    def run(self):
        self.last_execution_time = datetime.datetime.now()

        print("\t" + self.name+ ": starting task ("+self.last_execution_time.strftime("%H:%M:%S")+")")
        time.sleep(self.execution_time)
        print("\t" + self.name+ ": Ending task ("+self.last_execution_time.strftime("%H:%M:%S")+")")



if __name__ == '__main__':
    last_execution = datetime.datetime.now()

    task_list = []

    task_list.append(my_task(name="thread_1", priority =1, period= 10 , execution_time=10 , last_execution=last_execution ))
    task_list.append(my_task(name="thread_2", priority =1, period= 20 , execution_time=5 , last_execution=last_execution ))
    task_list.append(my_task(name="thread_3", priority =1, period= 60 , execution_time=20 , last_execution=last_execution ))