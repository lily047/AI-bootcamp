class EmailValidator(): 

    def __init__(self, email):
        self.email = email 

    def check_first_condition(self): 

        if '@' in self.email: 
            return True 
        else: 
            return False 
        
    def second_condition(self): 

        if '.' in self.email: 
            return True 
        else: 
            return False
        
    def vaildate(self): 

        if self.check_first_condition() and self.second_condition(): 
            return "given email is valid" 
        else: 
            return "given email is invalid" 
        
    def get_domain(self): 

        domain = ''

        flag = False 

        for char in self.email: 
            
            if flag: 
                domain+=char

            if char == '@': 
                flag = True 

        return domain 
        
def main(): 

    e=EmailValidator('Meghana@gmail.com')
    print(e.vaildate())
    print(e.get_domain())

if __name__ == '__main__': 

    main()