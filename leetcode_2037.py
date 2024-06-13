# Process
# Credits: https://leetcode.com/u/lancertech6/

# Sorting:
# First, sort both the seats list and the students list in ascending order.
# This helps in pairing each student with the nearest available seat in a way that minimizes the total movement.

# Pairing:
# Pair each seat with a student based on their positions in the sorted lists.
# This means the first seat in the sorted seats list is paired with the first student in the sorted students list, the second seat with the second student, and so on.

# Calculating Differences:
# For each pair of seat and student, calculate the absolute difference between the seat's position and the student's position.
# This difference represents the number of moves a student needs to reach the seat.

# Summing Up:
# Add up all the absolute differences calculated in the previous step.
# The sum of these differences gives the total number of moves required to seat all students.

# Solution
class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        return sum(abs(seat - student) for seat, student in zip (seats, students))
        # zip() is a Python built-in function that pairs elements from multiple iterables (in this case, seats and students) together.
        # It creates tuples where each tuple contains one seat and one student.

        # for loop that iterates over the tuples produced by zip(seats, students).
        # During each iteration, seat and student are assigned the values of the current tuple.
        # For example, in the first iteration, seat will be 1 and student will be 2.