class Stack:
    def __init__(self, element):
        self.stack = []
        self.stack.extend(element)
    
    def isEmpty(self):
        stored_amount = len(self.stack)
        if stored_amount == 0:
            return True
        else:
            return False
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty() is False:
            pop_id = len(self.stack) - 1
            popped_value = self.stack.pop(pop_id)
            return popped_value

    def peek(self):
        if self.isEmpty() is False:
            peeked_element_id = len(self.stack) - 1
            peeked_element = self.stack[peeked_element_id]
            return peeked_element
    
    def size(self):
        stack_size = len(self.stack)
        return stack_size
    
    def is_it_balanced(self):
        start_size = self.size()
        if (start_size % 2) == 0:
            symbol_count = {}
            iteration_length = self.size()
            for step in range(iteration_length):
                key = self.pop()
                if key not in symbol_count:
                    symbol_count[key] = 1
                else:
                     symbol_count[key] = symbol_count[key] + 1
            comparison_scheme = {
                ')': '(',
                ']': '[',
                '}': '{'
            }
            parentheses_stack = True
            for key, value in comparison_scheme.items():
                if symbol_count[key] == symbol_count[value]:
                    pass
                else:
                    parentheses_stack = False
            if parentheses_stack:
                print('Сбалансировано')
        else:
            print('Несбалансировано')

tryout_stack = Stack('(((([{}]))))')
tryout_stack.is_it_balanced()