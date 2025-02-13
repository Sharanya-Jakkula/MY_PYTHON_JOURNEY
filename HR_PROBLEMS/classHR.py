class Car:
    def __init__(self, max_speed, speed_unit):
        self.max_speed = max_speed
        self.speed_unit = speed_unit

    def __str__(self):
        if self.speed_unit == 'km/h':
            return 'Car with the maximum speed of {} {}'.format(self.max_speed, self.speed_unit)
        elif self.speed_unit == 'mph':
            return 'Car with the maximum speed of {} {}'.format(self.max_speed, self.speed_unit)
        else:
            return 'Car with the maximum speed of {} {}'.format(self.max_speed, self.speed_unit)

class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def __str__(self):
        return 'Boat with the maximum speed of {} knots'.format(self.max_speed)

if __name__ == '__main__':
    q = int(input())
    queries = []
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        for _ in range(q):
            args = input().split()
            vehicle_type, params = args[0], args[1:]
            if vehicle_type == "car":
                max_speed, speed_unit = int(params[0]), params[1]
                vehicle = Car(max_speed, speed_unit)
            elif vehicle_type == "boat":
                max_speed = int(params[0])
                vehicle = Boat(max_speed)
            else:
                raise ValueError("Invalid vehicle type")
            fptr.write("%s\n" % vehicle)
