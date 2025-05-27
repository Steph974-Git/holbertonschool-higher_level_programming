#!/usr/bin/python3

class VerboseList(list):

    def append(self,item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        super().extend(x)
        print("Extended the list with [{}] items.".format(len(x)))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list.".format(item))


    def pop(self, item=-1):
        elem = self[item]
        super().pop(item)
        print("Popped [{}] from the list.".format(elem))
