from faker import Faker

fake = Faker(['ru-RU'])


def test_faker():
    print('\n', fake.name())
    print('\n', fake.phone_number())
    print('\n', fake.email())
    print('\n', fake.country(), '-', fake.address())
    print('\n', fake.company(), '-', fake.job())
    print('\n', fake.image.cats)


"""
 Якушева Фаина Сергеевна

 86138064043

 emillebedev@example.com

 Андорра - клх Краснотурьинск, бул. Сиреневый, д. 591, 140430

 ОАО «Боброва-Наумова» - Маммолог
"""