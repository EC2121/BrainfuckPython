




class BrainfuckMachine():
    
    class HeadOverflow(Exception):
        pass
        
    class BracketMismatch(Exception):
        pass
    
    
    def __init__(self,size):
        self.size = size
        self.head = 0
        self.tape = [0] * size  #list(0 for i in range(size)) I was using this, is it better to use [0] * n ?
        self.code = ""
        self.message = ""
    
    def run(self):
        
        i = 0
        
        while i < len(self.code):
            
            if self.code[i] == '+':
                if self.tape[self.head] == 255:
                    self.tape[self.head] = 0
                else:
                    self.tape[self.head] += 1 
                
            elif self.code[i] == '-':
                if self.tape[self.head] == 0:
                    self.tape[self.head] = 255
                else:
                    self.tape[self.head] -= 1 
            
            elif self.code[i] == '<':
                self.head -= 1
                if self.head < 0:
                    raise self.HeadOverflow
                
            elif self.code[i] == '>':
                self.head += 1
                if self.head > self.size:
                    raise self.HeadOverflow
            
            elif self.code[i] == '[':
                
                # if self.code[i+1] is not None and self.code[i+1] == '[':
                #     raise self.BracketMismatch
                    
                if self.tape[self.head] == 0:
                    same_bracket_counter = 1
                    while same_bracket_counter > 0:
                        i += 1
                        if i >= len(self.code):
                            raise self.BracketMismatch
                        if self.code[i] == ']':
                            same_bracket_counter -= 1
                        elif self.code[i] == '[':
                            same_bracket_counter += 1
            
            
            elif self.code[i] == ']':
                if self.tape[self.head] != 0:
                    same_bracket_counter = 1                
                    while same_bracket_counter > 0:
                        i -= 1
                        if i < 0:
                            raise self.BracketMismatch
                        if self.code[i] == ']':
                            same_bracket_counter += 1
                        elif self.code[i] == '[':
                           same_bracket_counter -= 1      
            
            
            elif self.code[i] == '.':
                self.message = chr(self.tape[self.head])   #[chr(x) for x in self.tape if x != 0] 
                print(self.message)
                        
                   
            i += 1      
                        
            
         
                    
                
        
        
