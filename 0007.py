class Thpermometer(object):
    def warm(self,amount):
        reading = self.reading + amount
        return reading


device = Thpermometer()
device.reading = 18
result = device.warm(4)
print(result,device.reading)
