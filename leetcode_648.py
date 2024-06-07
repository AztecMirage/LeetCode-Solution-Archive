# Process

# Convert the List to a Set:
# Converting the list of roots to a set makes it faster to check if a prefix exists.

# Define a Function to Replace Words:
# This function will check each word in the sentence to see if it starts with any of the roots.
# If it does, replace the word with that root.
# If not, keep the word unchanged.

# Split the Sentence into Words:
# This helps to process each word individually.

# Process Each Word:
# Use the replacement function to find and replace prefixes for each word.

# Reconstruct the Sentence:
# Combine the processed words back into a single string.

# Solution
def replaceWords(dictionary, sentence):
    root_set = set(dictionary)
    
    def find_root(word):
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            if prefix in root_set:
                return prefix  
        return word 

    words = sentence.split()
    
    replaced_words = [find_root(word) for word in words]
 
    return " ".join(replaced_words)

