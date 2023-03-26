my_module_variable = [1, 3, 5, 7, 9]


def my_module_function(casefold):
    txt = "you just called my_module_function"
    if casefold == "upper":
        txtout = txt.lower()
    elif casefold == "upper":
        txtout = txt.upper()
    else:
        txtout = txt
    return txtout


class MyModuleClass:

    def __init__(self, number):
        self.number = number

    def NumberHolder(self):
        return self.number
