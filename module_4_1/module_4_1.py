from fake_math import divide as fdiv
from true_math import divide as tdiv

print("Fake math:", fdiv(6, 3))
print("Fake math:", fdiv(6, 0))
print("True math", tdiv(10, 5))
print("True math", tdiv(10, 0))
