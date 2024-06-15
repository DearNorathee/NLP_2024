import re

# Sample text
text = "The amount of premium is 75, 784, but we're still not sure"
text02 = ' OPD treatment for types of outpatient treatments over and above family sum insured to be covered up to Rs.75, 000/- per family only with original bills/ prescription'
# Regular expression pattern to find ', digit+ ,'
pattern = r',\s(\d+),'

# Replace the space within the matched pattern
actual01 = re.sub(pattern, r',\1', text)
actual02 = re.sub(pattern, r',\1', text02)
print(actual01)
print(actual02)