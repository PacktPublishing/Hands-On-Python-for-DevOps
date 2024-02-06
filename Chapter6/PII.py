#initial text
import re
text = "The first number is 901-895-7906. The second number is: 081-548-3262"
#pattern for search
search_pattern = r'\d{3}-\d{3}-\d{4}'
#replacement for pattern
replacement_text = "<phone_number>"
#text replacement
new_text = re.sub(search_pattern, replacement_text, text)
#output given: "The first number is <phone_number>. The second number is: <phone_number>"
print(new_text)
