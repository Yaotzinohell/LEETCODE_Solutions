class Solution(object):
    def minMovesToSeat(self, seats, students):
        sumesh = 0
        seats.sort()
        students.sort()
        for i in range(0, len(students)):
            sumesh = sumesh + abs(seats[i]-students[i])
        return sumesh