s = "The sky is blue"
#output: blue is sky The

words = s.split()

reversed_words = words[::-1]
reversed_line = " ".join(reversed_words)
print(reversed_line)

import string

def remove_punctuation(line):
  """Removes punctuation from a line of text."""
  translator = str.maketrans('', '', string.punctuation)  # Create a translation table for punctuation
  no_punct = line.translate(translator)  # Translate the line, removing punctuation
  return no_punct

# Example usage:
my_line = "This is a line, with some punctuation! Let's remove it."
cleaned_line = remove_punctuation(my_line)
print(cleaned_line)  # Output: This is a line with some punctuation Lets remove it
