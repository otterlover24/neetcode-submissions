class MinStack:

    def __init__(self):
        self._stack = []
        self._mins = [] # self._mins[i] stores minimum from self._stack[0] to self._stack[i]
        

    def push(self, val: int) -> None:
        self._stack.append(val)
        if len(self._mins) == 0:
            self._mins.append(val)
        else:
            self._mins.append(min(self._mins[-1], val))
        

    def pop(self) -> None:
        self._stack.pop()
        self._mins.pop()
        

    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self._mins[-1]
        
