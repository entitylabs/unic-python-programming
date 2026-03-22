from typing import Union, List

def addition(numbers: List[float]) -> Union[float,None]:
    
    sum = 0.0
    if numbers is None or len(numbers) ==0:
       return None
    else: 
        for number in numbers:
            sum = sum+ number
        return sum
        

print(addition([]))
print(addition([1,2,3,4,5]))


def is_palindrome(input: str)-> bool:
    if input is None:
        return False
    else:
        length = len(input)
        if length %2 ==0:
            part1= input[: int(length/2)]
            part2= input[int(length/2):]
            return part1 == part2[None: None: -1]
        else:
            part1= input[: int(length/2)]
            part2= input[int(length/2)+1:]
            return part1 == part2[None: None: -1]


# print(is_palindrome('None'))

print(is_palindrome('detartrated'))


from typing import List
from typing import Any

def create_dictionary_from_lists(keys_list:List, values_list:List)-> dict:
    dictionary = dict(zip(keys_list, values_list))
    return dictionary;

def reverse_dictionary(dictionary)-> dict:
    return dictionary.values().value()

created_dictionary= create_dictionary_from_lists([1,2,3],['a','b','c'])
reverse_dictionary(created_dictionary)
print(created_dictionary)


