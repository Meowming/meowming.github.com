class DaysTemp:
    def __init__(self,high=0,low=0):
        self.high = high
        self.low = low
    def __str__(self):
        result = ""
        result += "Today's low temperature is expected to be: {} \n".format(self.low)
        result += "Today's high temperature will be: {} \n".format(self.high)
        return result

    def get_average(self):
        return (self.high + self.low)/2

    def __le__(self,right):
        return self.get_average() <= right.get_average()

    def __lt__(self,right):
        return self.get_average() < right.get_average()

    def __ge__(self,right):
        return self.get_average() >= right.get_average()

    def __gt__(self,right):
        return self.get_average() > right.get_average()

    def __eq__(self,right):
        return self.get_average() == right.get_average()
    
d1 = DaysTemp()
print(d1)

d2 = DaysTemp(72,36)
print(d2)

print(d1<=d2)
