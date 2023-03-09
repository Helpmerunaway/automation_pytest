

class BuilderBaseClass:
    """
    Базовый класс для билдера. Можно дополнить ещё другими полезными
    методами, сейчас представлен только один.

    Base class for builder. You can add additional useful methods, but for now
    it has only one.
    """
    def __init__(self):
        self.result = {}

    def update_inner_value(self, keys, value):
        """
        Этот метод помогает обновить/добавить новое значение в объекте на
        указанном уровне.

        The method helps us update and add new values into object on specified
        level.
        """
        # верхний уровень ключи - не являются массивами, тогда просто обновляем значение
        if not isinstance(keys, list):
            self.result[keys] = value
        else:
            temp = self.result
            # удаляем последний элемент из массива
            for item in keys[:-1]:
                # если ключ отсутствует создаем пустой массив и переходим в него
                if item not in temp.keys():
                    temp[item] = {}
                # если ключ присутствует то переходим в него
                # (account_status, balance, localize, avatar)
                temp = temp[item]
            # последний элемент создай или пересоздай со значением value
            temp[keys[-1]] = value
        return self

    def build(self):
        return self.result
