class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def string2int(cls, time_string):
        timeList = time_string.split(':')
        for i in range(len(timeList)):
            timeList[i] = int(timeList[i])
        
        return timeList

    @classmethod        
    def is_time_valid(cls, time_string):
        timeList = cls.string2int(time_string)

        if timeList[0]>24 or timeList[0]<0:
            return False
        if timeList[1]>59 or timeList[1]<0:
            return False
        if timeList[2]>59 or timeList[2]<0:
            return False
        
        return True

    @classmethod
    def from_string(cls, time_string):
        timeList = cls.string2int(time_string)
        return Time(timeList[0], timeList[1], timeList[2])


time_string = input()


if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')