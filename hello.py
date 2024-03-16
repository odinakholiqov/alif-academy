from .db import students
from time import sleep

for student in students:
    sleep(1)
    print("Salom", student)


