from .db import students
from time import sleep

for student in students:
    sleep(2)
    print("Salom", student)


