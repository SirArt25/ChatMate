from functools import partial

# add strict strict_classmethod to ensure that i can create strictly classmethods
class strict_classmethod:
    def __init__(self, func):
         self.func = func
    def __get__(self, instance, owner):
         if instance is not None:
              raise TypeError("This method cannot be called from instances")
         return partial(self.func, owner)