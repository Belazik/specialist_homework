from random import randrange
import math

class Queue:

    def __init__(self):
        self.__data = list()

    def enqueue(self, item):
        self.__data.append(item)

    def dequeue(self):
        if len(self.__data) > 0:
            return self.__data.pop(0)

    def look_front(self):
        if len(self.__data) > 0:
            return self.__data[0]

    def look_ass(self):
        if len(self.__data) > 0:
            return self.__data[-1]

    def is_empty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def show(self):
        print(' '.join(str(val) for val in self.__data))

# q = Queue()
#
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)


def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    loser = ""
    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        loser = queue.dequeue()
        print(f'{loser} out of game!')

    return queue.dequeue()


def sort_student(students):
    q9 = Queue()
    q10 = Queue()
    q11 = Queue()
    for item in students:
        if item.split(' ')[0] == '9':
            q9.enqueue(item.split(' ')[1])
        elif item.split(' ')[0] == '10':
            q10.enqueue(item.split(' ')[1])
        elif item.split(' ')[0] == '11':
            q11.enqueue(item.split(' ')[1])
    print(q9.show())
    print(q10.show())
    print(q11.show())


class RadixSort:

    def __init__(self, num):
        self.__nums = num
        self.__bins = list()
        for i in range(10):
            self.__bins.append(Queue())

    def sort_to_bins(self, digit):
        for i in range(10):
            if digit == 1:
                self.__bins[self.__nums[i] % 10].enqueue(self.__nums[i])
            else:
                self.__bins[math.floor(self.__nums[i] // 10)].enqueue(self.__nums[i])

    def collect(self):
        i = 0
        for digit in range(10):
            while not self.__bins[digit].is_empty():
                self.__nums[i] = self.__bins[digit].dequeue()
                i += 1

    def show(self):
        return f"".join(str(self.__nums))


class Dancers:

    def __init__(self, filename):
        self.__filename = filename
        self.__format_list = list()
        self.__man = Queue()
        self.__woman = Queue()

    def read_file(self):
        with open(self.__filename, 'r') as dancers:
            return dancers.readlines()

    def sorted_gender_to_queue(self, lst):
        for dancer in lst:
            dancer_gender = dancer.strip().split(' ')[0]
            if dancer_gender == 'W':
                self.__woman.enqueue(dancer.strip().split(' ')[1])
            elif dancer_gender == 'M':
                self.__man.enqueue(dancer.strip().split(' ')[1])

    def create_dance_pair(self):
        while not self.__man.is_empty() or self.__woman.is_empty():
            print(f'Man {self.__man.dequeue()} meeting dance girl {self.__woman.dequeue()}')
        if not self.__man.is_empty():
          print(f'Man`s queue {self.__man.size()}, first queue {self.__man.look_front()}')
        elif not self.__woman.is_empty():
            print(f'Woman`s queue {self.__woman.size()}, first queue {self.__woman.look_front()}')
        else:
            print('All Dancing!')




# names = ['Genry', 'Mila', 'Nesty', 'Henry', 'Poll', 'Elizabet']
# print(f"{hot_potato(names, 7)} WINNER!")

# students = ['10 Victor', '9 Gelly', '11 Bella', '9 Nikki', '11 Josh', '9 Less']
# sort_student(students)

# numbers = [randrange(100) for i in range(10)]
# rs = RadixSort(numbers)
# print(rs.show())
# rs.sort_to_bins(1)
# rs.collect()
# print(rs.show())
# rs.sort_to_bins(10)
# rs.collect()
# print(rs.show())

# dance = Dancers('dancers.txt')
# dance.sorted_gender_to_queue(dance.read_file())
# dance.create_dance_pair()
