
class Palindrome:
    
    def enter_text(self):
        
        x = input() #Taking input
        
        y = x.replace(",","").replace("'","").replace(" ","") # Replacing elements
        
        print("Entered text" , y)
        z = y.lower()
        print("Reverse text" , z)
        if z[::-1] == z: # Reversing
            return "yes it is a palindrome"
        else:
            return "no it is not a palindrome"

q_1 = Palindrome()

try:    
    output_1 = q_1.enter_text()
    print(output_1)
except Exception as e:
    print(e)

