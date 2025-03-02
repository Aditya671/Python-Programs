

import play_with_list as pl
class ListSystem:
    def __init__(self, *input_lists):
        self.description = 'Class to Execute various methodologies related to Lists'
        self.input_lists = input_lists
        self.validation_messages = [self._validate_list(lst) for lst in input_lists]

    def _validate_list(self):
        if not isinstance(self.input_list, 'list'):
           return "Input data is not a list object"

    max_in_list = lambda input_list : pl.find_max_in_list(input_list)
    
    min_in_list = lambda input_list : pl.find_min_in_list(input_list)

    insert_at_index = lambda input_list, position, value : pl.insert_at_index(input_list, position, value)
    
    pop_at_index = lambda input_list, position, value : pl.pop_at_index(input_list)
    
    ascending_sort = lambda input_list : pl.sort_ascending(input_list)
    
    descending_sort = lambda input_list : pl.sort_descending(input_list)
    
    list_length = lambda input_list : pl.length_of_list(input_list)
    
    add_value = lambda input_list, value : pl.list_add_new_element_at_end(input_list, value)
    
    remove_value = lambda input_list, value : pl.remove_specific_value(input_list, value)
    
    count_value_occurrence= lambda input_list : pl.count_value_occurrence_in_list(input_list)
    
    list_reverse = lambda input_list : pl.reverse_a_list(input_list)
    
    sum_of_list_elements = lambda input_list : pl.sum_of_elements(input_list)

    average_of_list = lambda input_list : pl.average_of_list(input_list)
    
    median_of_list = lambda input_list : pl.median_of_list(input_list) 
    
    element_in_list = lambda input_list, ele : pl.element_in_list(input_list, ele)


list_system = ListSystem()