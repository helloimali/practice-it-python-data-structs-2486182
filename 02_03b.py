from collections import deque

class Task(object):
    def __init__(self, taskDesc, hasPriority=False):
        self.taskDesc = taskDesc
        self.hasPriority = hasPriority

    def __str__(self):
        return "Task: {0}, Priority: {1}".format(self.taskDesc, self.hasPriority)
    
task_queue = deque()
      
def addToTask(task):
    if task.hasPriority:
        task_queue.appendleft(task)
    else:
        task_queue.append(task)

def do_task():
    return task_queue.popleft()

def print_tasks():
    for t in task_queue:
        print (t.taskDesc)

def main():
    addToTask(Task("1"))
    addToTask(Task("2"))
    addToTask(Task("3", True))
    print_tasks()
    print(do_task)
    return

if __name__ == "__main__":
    main()