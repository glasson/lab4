class T(object):
    def __init__(self, row):
        self.type = ""
        self.row = str(row)

    def show(self):
        print(f"строка: {self.row}, {self.type}")

    def __str__(self):
        return str(self.row)

    def __del__(self):
        print("удален")

    def __sub__(self, sub) -> 'T':
        if not isinstance(self, sub.__class__):
            raise ValueError("bad_value")
            return
        print(str(self).replace(str(sub),""))
        return Factory.create_T(str(self).replace(str(sub),""))


class T1(T):
    def __init__(self, row):
        super().__init__(row)
        self.type = 'symb'


class T2(T):
    def __init__(self, row):
        super().__init__(row)
        self.type = "hex"


class Factory:
    @staticmethod
    def create_T(row):
        import re
        if bool(re.match(r"^[A-F\d]*$", row)):
            return T2(row)
        else:
            return T1(row)


def main():
    classes_array = []
    while True:
        print(
            "\nВвести \n1: чтобы создать обьект\n2: чтобы удалить обьект\n3: чтобы показать свойства класса"
            "\n4: вызова допфункции\n5: выхода"
        )
        get_input = input(">>> ")
        if get_input == "1":
            get_row = input("введите строку ")
            new_obj = Factory.create_T(get_row)

            classes_array.append(new_obj)
            print(classes_array)

        elif get_input == "2":
            get_index = int(input("введите индекс элемента для удаления "))
            try:
                del classes_array[get_index]
            except IndexError:
                print("нет такого индекса")
                continue


        elif get_input == "3":
            get_index = int(input("введите индекс элемента для вывода "))
            try:
                classes_array[get_index].show()
            except IndexError:
                print("нет такого индекса")
                continue


        elif get_input == "4":
            try:
                new_obj = classes_array[int(input("Введите индекс 1 элемента "))]
                sub = classes_array[int(input("Введите индекс 1 элемента "))]
            except IndexError:
                print("таких элементов нет")
                continue
            new_obj=new_obj.__sub__(sub)
            print(str(new_obj))
            if (isinstance(new_obj, T2)):
                classes_array.append(new_obj)


        elif get_input == "5":
            break
        else:
            continue


if __name__ == '__main__':
    main()
