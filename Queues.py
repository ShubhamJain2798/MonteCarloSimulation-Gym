# for staging area, import Layout
import time
import Users
import machine


def make_queue():
    # initialize queue for the machine
    initialQueue = [None] * 5
    return initialQueue


def add_user_to_queue(currentUser: object, currentMachine: object):
    # initialize user to the machine queue
    # update User object with current_queue
    # update machine object with user

    # make the user scan here for a new machine with a smaller queue -- Layout.find_new_machine()
    if None not in currentMachine.queue:
        return False
    # updating machine queue
    currentMachine.queue.append(currentUser)
    # updating users' current queue
    currentUser.currentMachine = currentMachine
    # setattr(user, "current_queue", machine.queue)
    return True


def check_queue(machineList: object):
    # run this piece of code in a thread
    # check for impatient user
    # check if machine is empty
    time.sleep(5)
    for machine in machineList:
        for user in machine:
            if user.impatience:
                if user.currentQueueTime > user.impatientTime or user.currentQueueTime > user.thresholdTime:
                    # find new machine using Layout --->  Layout.find_new_machine(user, user.currentMachine)
                    pass


def remove_from_queue(currentMachine: object, currentUser: object):
    try:
        currentMachine.queue.remove(currentUser)
        return True
    except Exception as e:
        return False


if __name__ == '__main__':
    pass