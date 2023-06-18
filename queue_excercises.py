import math
from Data_Structures.queue_1 import Queue
import random

def hot_potato(name_list, num)->str:
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)
    while sim_queue.size()>1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        print(sim_queue.dequeue(), " lost")
    return sim_queue.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent","Brad"], 5))

class Printer:
    def __init__(self, ppm) -> None:
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0
    
    def tick(self):
        if self.current_task != None:
            self.time_remaining -=1
            if self.time_remaining <=0:
                self.current_task = None
    
    def busy(self)->bool:
        return True if self.current_task != None else False
    
    def start_task(self, task):
        self.current_task = task
        self.time_remaining = task.get_pages()*60/self.page_rate #Printer works in seconds but page rate is in minutes

class Task:
    def __init__(self, time) -> None:
        self.timestamp = time
        self.pages = random.randint(1,20)#Minimum and maximum number of pages students can print

    def get_stamp(self):
        return self.timestamp
    
    def get_pages(self):
        return self.pages
    
    def wait_time(self, current_time):
        return current_time - self.timestamp
    
def printer_line_simulation(num_seconds, page_per_minute, num_students = 10):

    lab_printer = Printer(page_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if random.randint(1,1800//num_students) == 1800//num_students:
            task = Task(current_second)
            print_queue.enqueue(task)
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second)) #This is the time they waited for the *task to start*, not for it to be done!
            #If we want time untill fully finished we can add time remaining after this line:
            lab_printer.start_task(next_task)

        lab_printer.tick()
    
    return (sum(waiting_times)/len(waiting_times), len(print_queue))


average_simulation_wait_time = []
for i in range(100):
    wait, tasks_remaining = printer_line_simulation(3600, 5)
    print(f"Test {i}: Average wait time of {wait}. {tasks_remaining} tasks remaining")
    average_simulation_wait_time.append(wait)
res_average_simulation_wait_time = sum(average_simulation_wait_time)/len(average_simulation_wait_time)
print(f"Average time between simulations: {res_average_simulation_wait_time}. Deviation: {math.sqrt(sum((i-res_average_simulation_wait_time)**2 for i in average_simulation_wait_time)/len(average_simulation_wait_time))}")


average_simulation_wait_time = []
for i in range(100):
    wait, tasks_remaining = printer_line_simulation(3600, 10)
    print(f"Test {i}: Average wait time of {wait}. {tasks_remaining} tasks remaining")
    average_simulation_wait_time.append(wait)
res_average_simulation_wait_time = sum(average_simulation_wait_time)/len(average_simulation_wait_time)
print(f"Average time between simulations: {res_average_simulation_wait_time}. Deviation: {math.sqrt(sum((i-res_average_simulation_wait_time)**2 for i in average_simulation_wait_time)/len(average_simulation_wait_time))}")


#Self Check: parameterize the number of students

average_simulation_wait_time = []
for i in range(20):
    wait, tasks_remaining = printer_line_simulation(3600, 10, 20)
    print(f"Test {i}: Average wait time of {wait}. {tasks_remaining} tasks remaining")
    average_simulation_wait_time.append(wait)
res_average_simulation_wait_time = sum(average_simulation_wait_time)/len(average_simulation_wait_time)
print(f"Average time between simulations: {res_average_simulation_wait_time}. Deviation: {math.sqrt(sum((i-res_average_simulation_wait_time)**2 for i in average_simulation_wait_time)/len(average_simulation_wait_time))}")
#Suppose that the length of the average printing task was cut in half: while we could modify the Printer class, using double the pages per minute has the same effect