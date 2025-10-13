apple = 15.5
orange = 20
grape = 10.25

total_volume = apple + orange + grape
print("total volume = ", total_volume)

volume_int = int(total_volume)
print("volume in int = ",volume_int)

volume_str = str(total_volume)
print("volume in str = ", volume_str)

import random
bonus = random.randint(5, 10)
final_total = total_volume + bonus
print("After adding bonus liters " ,final_total)
