# Initializing Variables:
# We start by initializing an empty dictionary named min_counts to store the minimum counts of characters across all strings.
# Counting Characters in the First String:
# We iterate through each character in the first string "bella" and count the occurrences of each character.
# For example, 'b' appears once, 'e' appears once, 'l' appears twice, and 'a' appears once.

# We store these counts in the min_counts dictionary.

# Counting Characters in Subsequent Strings:
# We iterate through the remaining strings "label" and "roller".
# For each string, we count the occurrences of each character and store these counts in a temporary dictionary current_counts.
# We then compare these counts with the counts already stored in min_counts, updating min_counts with the minimum counts for each character.
# Constructing the List of Common Characters:
# Once we have the minimum counts for each character across all strings, we construct the list of common characters based on these minimum counts.

# For each character and its minimum count in min_counts, we add the character to the list of common characters common_chars repeated count times.
# By repeating each character count times, we ensure that each common character is included the correct number of times in the final list, reflecting its minimum count across all strings.

# Returning the Result:
# Finally, we return the list of common characters.

# In the example, 
# for input ["bella", "label", "roller"], the output will be ['b', 'e', 'l', 'l', 'a']
# which represents the common characters among all strings in the list.

# Solution
class Solution(object):
    def commonChars(self, words):
        min_counts = {}
        for char in words[0]:
            min_counts[char] = words[0].count(char)
        for string in words[1:]:
            current_count = {}
            for char in string:
                current_counts[char] = string.count(char)
            for char in min_counts:
                if char in current_count:
                    min_counts[char] = min(min_counts[char], current_counts[char])
            else:
                min_counts[char] = 0

        common_char = []
        for char, count in min_counts.items():
            common_chars.extend([char] * count)
        return common_char