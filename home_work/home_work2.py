
paragraph = """This Python course is designed for beginners who want to learn the fundamentals of Python programming. 
It covers topics such as variables, data types, control flow, functions, and basic object-oriented programming."""

length = len(paragraph)
print("Length of paragraph:", length)
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

preview = paragraph[:50]
print("Preview first 50 chars:", preview)

paragraph_upper = paragraph.replace("Python", "PYTHON")
print("\nAfter replacing 'Python' with 'PYTHON':\n", paragraph_upper)

paragraph_lower = paragraph.lower()
print("\nParagraph in lowercase:\n", paragraph_lower)

paragraph_clean = paragraph.strip()
print("\nParagraph after stripping whitespaces:\n", paragraph_clean)

words = paragraph.split()
print("\nList of words:\n", words)

if "course" in paragraph.lower():
    print("\nThe word 'course' exists in the paragraph.")

print("\nThe course description is {} characters long and has {} words.".format(len(paragraph), len(words)))
