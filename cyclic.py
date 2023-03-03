from llist import *

# Modified by Justin Kroh on 03/01/2023

def llprint(lst, num):
    """print the first num terms of linked list lst"""
    thisNode = lst.head
    counter = 0
    while thisNode and counter < num:
        print(thisNode.val,end=" ")
        thisNode = thisNode.next
        counter += 1

def find_cycle(lst):
    """return the start index and length of the cycle"""
    tortoise = lst.head.next
    hare = lst.head.next.next
    # Find two of the same value
    print("Start...")
    while tortoise is not hare:
        tortoise = tortoise.next # Move 1 Step
        hare = hare.next.next # Move 2 Steps
    print("Same values found!")
    mu = 0
    tortoise = lst.head
    # Find the start of the cycle
    while tortoise is not hare:
        tortoise = tortoise.next
        hare = hare.next
        mu += 1
    print("Start of cycle found!",mu)
    lam = 1
    hare = tortoise.next
    # Find the length of the cycle
    while tortoise is not hare:
        hare = hare.next
        lam += 1
    print("Length of cycle found!",lam)
    print("Start of Cycle: ",mu,"Length of Cycle: ",lam)

if __name__ == "__main__":
    print("hi")
    from gencyclic import lst
    find_cycle(lst)
    llprint(lst,1000)

