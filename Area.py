from cmath import pi


radius = input('Type your input')


def Area(radius):
    '''
    area = PI * r ^2
    '''
    result = 3.146 * int(radius) * int(radius)
    print(result)


Area(radius)
