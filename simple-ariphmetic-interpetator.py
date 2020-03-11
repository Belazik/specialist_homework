import abc

class Stack:
    def __init__(self):
        self.__data = list()

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        return self.__data.pop()

    def is_empty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def peek(self):
        return self.__data[-1]

class InterpreterAbstract(abc.ABC):
    """Code interpretator"""

    def __init__(self, code):
        self.code = code

    def execute(self):
        """Start code, Return execute code"""
        return self._parse()

    @abc.abstractmethod
    def _parse(self):
        pass

    @abc.abstractmethod
    def _evaulate(self, code):
        pass


class Interpreter(InterpreterAbstract):

    def __init__(self, file=None, string=None):
        if string is not None:
            self.__code = string
        else:
            if file is None:
                raise AttributeError('Please take filename or string code')
            with open(file, 'r') as f:
                self.__code = f.read()
        self.__ops = Stack()
        self.__nums = Stack()

    def execute(self):
        return self._parse()

    def _parse(self):
        lines = self.__code.strip().split('\n')
        ret = []
        for line in lines:
            if not self._validate(line):
                raise Exception('Code is broken, please check correct "(" or ")"')
            line = ''.join(line.split())
            ret.append(self._evaulate(line))
        return ret

    def _evaulate(self, code):
        operators = ['+', '-', '*', '/', '^']
        code = '(' + code + ')'
        for char in code:
            if char == '(':
                continue
            elif char in operators:
                self.__ops.push(char)
            elif char == ')':
                op = self.__ops.pop()
                val = self.__nums.pop()
                if op == '+':
                    val += self.__nums.pop()
                elif op == '-':
                    val = self.__nums.pop() - val
                elif op == '*':
                    val *= self.__nums.pop()
                elif op == '/':
                    val = self.__nums.pop() // val
                elif op == '^':
                    val = self.__nums.pop() ** val
                self.__nums.push(val)
                continue
            else:
                self.__nums.push(int(char))
        return self.__nums.pop()

    def _validate(self, code):
        stack = Stack()
        for char in code:
            if char == '(':
                stack.push(char)
            elif char == ')':
                stack.pop()
        if stack.is_empty():
            return True
        else:
            return False

#interpreter = Interpreter(string='1+((2+3)*(4*5))')
#print(interpreter.execute())
interpreter = Interpreter(file='code.txt')
print(interpreter.execute())
