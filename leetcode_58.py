# Process
# Remove Trailing Spaces:
# s = s.rstrip() removes any trailing spaces from the string.
# This is important because trailing spaces shouldn't affect the calculation of the last word's length.

# Split the String into Words:
# words = s.split() splits the string by spaces into a list of words.

# Check if Words List is Empty:
# if not words: checks if the words list is empty.
# If it is, this means there are no words in the string, so the function should return 0.

# Return the Length of the Last Word:
# return len(words[-1]) returns the length of the last word in the list.

# Solution
class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        words = s.split()
        if not words:
            return 0
        return len(words[-1])