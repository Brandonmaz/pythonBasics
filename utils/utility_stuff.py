class Shortener:
    def __init__(self, items):
        self.original_items = items

    def print_original_items(self):
        print(self.original_items)


class ListAndCarShortener(Shortener):
    def print_shortened_items(self):
        print(self.original_items[0:3])


class DictionaryShortener(Shortener):
    def print_shortened_items(self):
        dict = self.original_items
        counter = 0
        result_dict = {}
        for k, v in dict.items():
            if(counter < 3):
                result_dict.update({k: v})
                counter += 1
        print(result_dict)


# myDictShortener = DictionaryShortener(
#     {1: 'mike', 2: 'tom', 3: 'mark', 4: 'paul', 5: 'steve'})
# myDictShortener.print_original_items()
# myDictShortener.print_shortened_items()


# mySentenceShortener = ListAndCarShortener("this is a sentence")
# myNumberShortener = ListAndCarShortener([1, 2, 3, 4, 5, 6])

# mySentenceShortener.print_shortened_items()
# myNumberShortener.print_original_items()
