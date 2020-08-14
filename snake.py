from random import randint
print("Elderly snake investigator.\n")
#snake_age = 0
o_count = 0
y_count = 0
def is_old(age):
    if age>=30:
        return True
    return False

times = int(input("How many snakes would you like to investigate today? "))
for i in range(times):
    age = randint(1, 60)
    if is_old(age):
        o_count +=1
    else:
        y_count+=1

print("out of", times, "snakes,", (o_count/times)*100, "% were old.")