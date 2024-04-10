# ValueError: Sample larger than population or is negative


# Using the min() function to solve the error

import random

a_list = ['bobby', 'hadz', 'com']

random_elements = random.sample(a_list, min(4, len(a_list)))
print(random_elements)  # 👉️ ['com', 'bobby', 'hadz']