# Process

# Check Divisibility:
# Ensure the total number of cards is divisible by the group size, else return False.

# Sort Cards:
# Sort the hand to process cards in ascending order.

# Count Card Occurrences:
# Count how many of each card exists in the hand.

# Iterate Through Cards:
# For each card:
# If it's already processed, skip it.
# Check if there are enough cards to form a group.
# Decrement card counts for forming groups.

# Return Result:
# If all groups are successfully formed, return True; otherwise, return False.

# Solution
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        count = Counter(hand)
        
        for card in hand:
            if count[card] == 0:
                continue
            for i in range(groupSize):
                if count[card + i] > 0:
                    count[card + i] -= 1
                else:
                    return False
        return True