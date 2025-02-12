def sum_of_elements(numbers):
    x = 0 
    for num in numbers:
        x += num  
    return x  

print(sum_of_elements([1, 2, 3, 4, 5]))  

def find_maximum(numbers):
    max_num = numbers[0]  
    for num in numbers:  
        if num > max_num:  
            max_num = num  
    return max_num  

print(find_maximum([1, 2, 3, 4, 5]))  

def count_occurrences(lst, element):
    count = 0  
    for item in lst:  
        if item == element:  
            count += 1  
    return count  

print(count_occurrences([1, 2, 2, 3, 4], 2))  

def reverse_list(lst):
    reversed_lst = []  
    for item in lst:  
        reversed_lst.insert(0, item)  
    return reversed_lst  

print(reverse_list([1, 2, 3, 4, 5]))  

def remove_duplicates(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
            return unique_lst

print(remove_duplicates([1, 2, 2, 3, 4, 4]))

def sort_list(numbers):
    sorted_lst = [] 
    while numbers:  
        min_num = numbers[0]  
        for num in numbers:  
            if num < min_num:  
                min_num = num
        sorted_lst.append(min_num)  
        numbers.remove(min_num)  
    return sorted_lst  

print(sort_list([5, 3, 1, 4, 2]))  

def list_length(lst):
    count = 0  
    for item in lst:  
        count += 1  
    return count  

print(list_length([1, 2, 3, 4, 5]))  

def concatenate_lists(lst1, lst2):
    concatenated_lst = []  
    for item in lst1:  
        concatenated_lst.append(item)  
    for item in lst2:  
        concatenated_lst.append(item)  
    return concatenated_lst  

print(concatenate_lists([1, 2], [3, 4]))  

def list_slicing(lst, start, end):
    sliced_lst = []  
    for i in range(start, end):  
        if i < len(lst):  
            sliced_lst.append(lst[i])  
    return sliced_lst  

print(list_slicing([1, 2, 3, 4, 5], 1, 4))  

def check_element_existence(lst, element):
    for item in lst:  
        if item == element:  
            return True  
    return False  

print(check_element_existence([1, 2, 3, 4], 3))  










