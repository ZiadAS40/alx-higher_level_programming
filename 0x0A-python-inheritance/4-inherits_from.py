#!/usr/bin/python3
def is_instance_of_subclass_only(obj, a_class):
    if isinstance(obj, a_class):
        return type(obj) != a_class
    return False
