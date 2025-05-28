import random
from IPython.display import display, Markdown, Latex, clear_output, display_markdown
import sys
# Using this one for generating random numbers for practicing
# B-trees and B+ trees

num_list = []
for i in range(10):
    rn = random.randint(0,20)
    while rn in num_list:
        rn = random.randint(0,20)
    num_list.append(rn)
num = str(num_list).replace("[","").replace("]","")
display(Markdown((f"# ``` {num} ```" )))

for i in range(0, len(num_list)-1):
    ch = int(input())
    while(ch not in num_list or ch == -1):
        ch = int(input())
    if ch == -1:
        sys.exit(0)
    num_list[i] = "x"
    num = str(num_list).replace("[","").replace("]","")
    clear_output()
    display(Markdown((f"# ``` {num} ```" )))
