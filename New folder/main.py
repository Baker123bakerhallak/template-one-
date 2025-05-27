import string
import time

text = ["Baker Hallak", "Omar Hallak", "Mozna Hallak", "Balsam Mhanna"]
temp = ""
for name in text:
    for ch in name:
        for i in string.printable:
            if i == ch:
                time.sleep(0.02)
                print(temp + i)
                temp += ch
                break
            else:
                time.sleep(0.02)
                print(temp + i)
