# example of class method
class Bird:
    # this is a class var
    wings = 2

    # this is a class method
    def fly(cls, name):
        print('{} flies with {} wings'.format(name, cls.wings))


# display information for 2 birds
Bird.fly('sparrow')
Bird.fly('Pigeon')
