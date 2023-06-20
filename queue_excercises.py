import math
from queue_1 import Queue
from queue_1 import QueueLinkedList
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

"""
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

""" # Simulations commented out so they don't run every time
"""Implement a radix sorting machine. A radix sort for base 10 integers is a mechanical
sorting technique that utilizes a collection of bins, one main bin and 10 digit bins. Each
bin acts like a queue and maintains its values in the order that they arrive. The algorithm
begins by placing each number in the main bin. Then it considers each value digit by
digit. The first value is removed and placed in a digit bin corresponding to the digit being
considered. For example, if the ones digit is being considered, 534 is placed in digit bin
4 and 667 is placed in digit bin 7. Once all the values are placed in the corresponding
digit bins, the values are collected from bin 0 to bin 9 and placed back in the main bin.
The process continues with the tens digit, the hundreds, and so on. After the last digit is
processed, the main bin contains the values in order
"""

def radix_sorter(to_sort: list)->list:
    main_bin = QueueLinkedList()
    digit_bins = [QueueLinkedList() for _ in range(10)]
    
    for n in to_sort:
        main_bin.enqueue(n)
    print(main_bin.items)
    have_digits = True
    digit = 0
    while have_digits:
        have_digits = False
        while not main_bin.is_empty():
            temp = main_bin.dequeue()
            if temp // (10**digit) == 0:
                digit_bins[0].enqueue(temp)
            else:
                have_digits = True
                digit_bins[(temp%(10**(digit+1)))//(10**digit)].enqueue(temp) #Could've just turned them into strings and used indexation
                #Wouldn't be as funny though. That expresion returns the digit at "digit" position through mathematical operations
        iter = 0
        while iter <=9:
            while not digit_bins[iter].is_empty():
                temp = digit_bins[iter].dequeue()
                main_bin.enqueue(temp)
            iter+=1
        digit+=1
    return main_bin.items #IMPORTANT: This returns a list in the correct (descending) order beacuse of IMPLEMENTATION (see QueueLinkedList).
    #This isn't very good: asumming most queue implementations append the most recent item at index 0, we would end up with a desdending list ordering
    #We would usually need a reversal in the iter loop to make it descending
    #See however that the Queue's implementation produces no errors: Qeue's insides are not expected to be read, and our implementation works just fine
    #for the required Queue ADT operations. Reading the insides is just not one of them. 
    
print(radix_sorter([random.randrange(0,10001) for _ in range(100)]))
print(sorted([1,2,5,4]))
