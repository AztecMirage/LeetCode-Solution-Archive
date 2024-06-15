# Process
# Combine Costs and Profits:
# Put the cost and profit of each stand into pairs.

# Use Two Special Lists (Heaps):
# One list to keep track of stands based on their starting cost.
# Another list to pick the most profitable stand you can afford.

# Choose Stands to Invest In:

# For each investment (up to a given limit), do the following:
# Move all affordable stands to the profit list.
# Pick the stand with the highest profit.
# Add its profit to your money.
# If no stands are affordable, stop.

# Solution
import heapq

class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        # Ensure Profits and Capital are lists
        if not isinstance(Profits, list) or not isinstance(Capital, list):
            raise TypeError("Profits and Capital must be lists")
        
        # Ensure k is an integer and W is an integer or float
        if not isinstance(k, int) or not isinstance(W, (int, float)):
            raise TypeError("k must be an integer and W must be an integer or float")
        
        # Step 1: Combine costs and profits into pairs
        # zip is a built-in function that takes two or more sequences (like lists or tuples) and returns an iterator of tuples, where each tuple contains elements from each of the sequences at the same position.
        # Essentially, it "zips" together the elements of the sequences.
        projects = list(zip(Capital, Profits))
        
        # Step 2: Create a heap (special list) for project costs
        min_cap_heap = []
        for cap, prof in projects:
            heapq.heappush(min_cap_heap, (cap, prof))
        
        # Step 3: Create another heap for profits
        max_prof_heap = []
        
        # Step 4: Invest in up to k projects
        for _ in range(k):
            # Move all projects you can afford to the profit heap
            while min_cap_heap and min_cap_heap[0][0] <= W:
                cap, prof = heapq.heappop(min_cap_heap)
                heapq.heappush(max_prof_heap, (-prof, cap))  # Use negative profit to create a max-heap
            
            # If there are no affordable projects left, stop
            if not max_prof_heap:
                break
            
            # Choose the project with the highest profit
            W += -heapq.heappop(max_prof_heap)[0]
        
        return W