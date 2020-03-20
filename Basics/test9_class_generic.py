class ClassName(object):
    #instance methods always take self as the first parameter
    def instance_method(self, passed_params):
        #code to execute

    #the constructor is an instance method
    def __init__(self, passed_params):
        #assignments

    #class methods always take a class instance as the first parameter
    @classmethod
    def class_method(cls, passed_params):
        #code to execute

    @staticmethod
    def static_method(passed_params):
        #code to execute

class_instance = ClassName()
#calling instance and class methods
class_instance.instance_method()
#calling static methods
ClassName.static_method()