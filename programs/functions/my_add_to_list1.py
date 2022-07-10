def my_add_to_list1(sequence,target=[]):
    """
        Uses a mutable default, usually leads to unexpected behavior
    """
    target.extend(sequence)
    return target



my_add_to_list1("hi")
