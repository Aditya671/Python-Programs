

import play_with_list as pl
class ListSystem:
    def __init__(self, self, *input_lists):
        self.description = 'Class to Execute various methodologies related to Lists'
        self.input_lists = input_lists
        self.validation_messages = [self._validate_list(lst) for lst in input_lists]

    def _validate_list(self):
        if not isinstance(self.input_list, 'list'):
           return "Input data is not a list object"

    max_in_list = lambda input_list : pl.find_max_in_list(input_list)

