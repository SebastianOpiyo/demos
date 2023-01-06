import time
import random
user_position = int(input("what floor are you on"))
print("doors closed")
if user_position > 10 or user_position < 0:
     print("that does not exist")
else:
     lift_position = random.randint(1, 10)
