class BrainfuckMachine():
    
    class HeadOverflow(Exception):
        pass
        
    class BracketMismatch(Exception):
        pass
    
    
    def __init__(self,size):
        self.size = size
        self.head = 0
        self.index = 0
        self.instructions = {
            '+' : self.plus,
            '-' : self.minus,
            '>' : self.move_head_to_right,
            '<' : self.move_head_to_left,
            '[' : self.open_bracket,
            ']' : self.closed_bracket,
            '.' : self.print_code
        }
        self.tape = [0] * size  
        self.code = ""
        self.message = ""
    
    
    
    def plus(self):
        self.tape[self.head] += 1
        if self.tape[self.head] == 255:
            self.tape[self.head] = 0
            
    def minus(self):
        self.tape[self.head] -= 1
        if self.tape[self.head] == -1:
            self.tape[self.head] = 255
    
    def move_head_to_right(self):
        self.head += 1
        if self.head >= self.size:
            raise self.HeadOverflow
    
    def move_head_to_left(self):
        self.head -= 1
        if self.head < 0:
            raise self.HeadOverflow
        
    def open_bracket(self):
        if self.tape[self.head] == 0:
            same_bracket_counter = 1
            while same_bracket_counter > 0:
                self.index += 1
                if self.index >= len(self.code):
                     raise self.BracketMismatch
                if self.code[self.index] == ']':
                    same_bracket_counter -= 1
                elif self.code[self.index] == '[':
                    same_bracket_counter += 1 
    
    
    def closed_bracket(self):
        if self.tape[self.head] != 0:
            same_bracket_counter = 1                
            while same_bracket_counter > 0:
                self.index -= 1
                if self.index < 0:
                    raise self.BracketMismatch
                if self.code[self.index] == ']':
                    same_bracket_counter += 1
                elif self.code[self.index] == '[':
                    same_bracket_counter -= 1      
    
    
    def print_code(self):
        self.message = chr(self.tape[self.head])   #[chr(x) for x in self.tape if x != 0] 
        print(self.message)
        
        
    
    def run(self):
        
       
        
        while self.index < len(self.code):
            
            instruction = self.instructions[self.code[self.index]]
            instruction()
            self.index += 1
            
            
            
            
            
            
                        
                   
                        
            
         
                    
                
        
        
