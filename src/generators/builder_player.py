from enum import Enum

from src.baseclasses.builder import BuilderBaseClass
from src.enums.user_enums import Statuses
from src.generators.player_localization import PlayerLocalization

"""
Не совсем простенький генератор Player.
Uncommon generator for Player ^_^.
"""


class Player(BuilderBaseClass):

    # конструктор что будет делать за что отвечать
    def __init__(self):
        super().__init__()
        self.reset()

    def set_status(self, status=Statuses.ACTIVE.value):
        self.result['account_status'] = status
        return self

    def set_balance(self, balance=0):
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar="https://google.com/"):
        self.result['avatar'] = avatar
        return self

    def reset(self):
        self.set_status()
        self.set_avatar()
        self.set_balance()
        self.result["localize"] = {
            "en": PlayerLocalization('en_US').build(),
            "ru": PlayerLocalization('ru_RU').build()
        }
        return self

    # def update_inner_value(self, keys, value):
    #     if not isinstance(keys, list):
    #         self.result[keys] = value
    #     else:
    #         temp = self.result
    #         for item in keys[:-1]:
    #             if item not in temp.keys():
    #                 temp[item] = {}
    #             temp = temp[item]
    #         temp[keys[-1]] = value
    #     return self

    def update_inner_generator(self, key, generator):
        #self.result[key] = generator.build()
        self.result[key] = {"en": generator.build()}
        return self

    # def build(self):
    #     return self.result


# z = Player().set_balance(20).set_status('none').set_avatar().build()
# print(z)