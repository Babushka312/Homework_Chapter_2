# 2) Написать программу с использованием регулярного выражения, которая заменит
# пробелы пустоту
# " Python Exercises " должен превратиться в "PythonExercises"
import re
pattern = r" "
new_text = ""
text = """
Python Exercises
"""
res = re.sub(pattern, new_text, text)
print(res)