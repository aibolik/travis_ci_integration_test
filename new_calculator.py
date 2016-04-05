class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class Calculator(object):

    infix = ""
    display = ""
    curnumber = None


    def __init__(self):
        self.display = ""
        self.curnumber = ""
        self.infix = ""

    def parse_rpn(self, expression):
        """ Evaluate a reverse polish notation """

        stack = []

        for val in expression.split(' '):
            if val in ['-', '+', '*', '/']:
                op1 = stack.pop()
                op2 = stack.pop()
                if val=='-': result = op2 - op1
                if val=='+': result = op2 + op1
                if val=='*': result = op2 * op1
                if val=='/': result = op2 / op1
                stack.append(result)
            else:
                stack.append(float(val))

        return stack.pop()

    def infixToPostfix(self):
        prec = {}
        prec["*"] = 3
        prec["/"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1
        opStack = Stack()
        postfixList = []
        tokenList = self.infix.split(' ')

        for token in tokenList:
            if token not in ["*", "+", "-", "/"]:
                postfixList.append(token)
            elif token == '(':
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not opStack.isEmpty()) and \
                   (prec[opStack.peek()] >= prec[token]):
                      postfixList.append(opStack.pop())
                opStack.push(token)

        while not opStack.isEmpty():
            postfixList.append(opStack.pop())

        self.infix = ""
        self.display = ""
        return " ".join(postfixList)

    def add_number(self):
        self.curnumber = ""

    def clear(self):
        self.curnumber = ""
        self.display = ""
        self.infix = ""

    def convertToInfix(self):
        self.infix = ""
        for symbol in self.display:
            if symbol in ["+", "-", "*", "/"]:
                self.infix += " "
                self.infix += symbol
                self.infix += " "
            else:
                self.infix += symbol


    def press(self, symbol):
        if symbol.lower() == 'c':
            self.clear()
            return
        self.display += symbol
        if symbol.isdigit():
            self.curnumber += symbol
        elif symbol in ["+", "-", "*", "/", "(", ")"]:
            self.add_number()
        elif symbol == '=':
            self.add_number()
            self.display = self.display[:-1]
            self.convertToInfix()
            expression = self.infixToPostfix()
            result = self.parse_rpn(expression)
            self.display = str(int(result))
