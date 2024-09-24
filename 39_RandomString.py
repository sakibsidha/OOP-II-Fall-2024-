import string    
import random
S = 7 # lenght
ran = "".join(random.choices(string.ascii_letters + string.digits, k = S))    
print("The randomly generated string is: " + str(ran))