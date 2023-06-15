from queue_1 import Queue


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