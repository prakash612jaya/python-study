import re
from string import whitespace

# step 1: storing the original paragraph to a variable
text = """tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# step 2: fixing capitalization for each sentence
sent01 = re.split(r'(?<=[.?!])\s', text)
norm_sent = [s.capitalize() for s in sent01]

# step 3: fixing the incorrect word 'iz' to 'is'
fix_sent = []
for sentence in norm_sent:
    fixed = re.sub(r'\biz\b', 'is', sentence)
    fix_sent.append(fixed)

# step 4: creating new sentence for last words
last_words = [s.strip().split()[-1].rstrip('.,') for s in fix_sent if s.strip()]
new_sent = ' '.join(last_words).capitalize() + '.'
fix_sent.append(new_sent)

# step 5: joining all into final text
final_text = ' '.join(fix_sent)

# step 6: count all white spaces characters
whitespace_count = sum(1 for char in final_text if char.isspace())

# output
print("Final Text:\n")
print(final_text)
print("\nTotal whitespace characters:", whitespace_count)
