"""
2-3: Store a person's name in a variable, and print a message to that person. 
Message example: "Hello Eric, would you like to learn some Python today?"
"""
name = "Melville"
print("Hello", name, "would you like to learn some Python today?")

""""
2-4: store person's name in variable, then print person's name in lowercase, upper case, title case
"""
person_name = "melville"
print(person_name.title(), person_name.upper(), person_name.lower())

"""
2-5: famous quote: using escape characters, covers 2-6 as well
"""
author = "albert einstein"
quote = "\"A person who never made a mistake never tried anything new\""
print(author.title(), "once said,", quote)

"""
2-7: stripping strings, lstrip(), rstrip(), strip()
"""
name_to_strip = "\t melville \t"
print(name_to_strip.lstrip(), "\n",
      name_to_strip.rstrip(), "\n",
      name_to_strip.strip())
