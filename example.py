from db import session
from sqlalchemy.sql.expression import desc
import tables

"""
Простые запросы в базу 
"""
# first - вернет первый попавшийся результат (фильм)
result = session.query(tables.Films.film_id, tables.Films.title).first()
# all - вернет все фильмы в виде массива
result_all = session.query(tables.Films.film_id, tables.Films.title).all()
# one_or_none - вернет либо один результат (фильм) либо ничего
result_one = session.query(tables.Films.film_id, tables.Films.title).one_or_none()
print(result)

result_one_or_none = session.query(
    tables.Films.film_id, tables.Films.title
).filter(
    tables.Films.film_id == 180
).one_or_none()
if result_one_or_none:
    print('All is good')
else:
    print("Not good")
# выводит все фильмы которые подходят под параметры
result_min_max = session.query(
    tables.Films.film_id > 100,
    tables.Films.film_id < 150
).all()

if result_min_max:
    print("All is good")
else:
    print("Not good")

film_ids = session.query(
    tables.Films.film_id
).filter(tables.Films.film_id > 180).subquery()
print(film_ids)

result_1 = session.query(tables.Films.title).filter(tables.Films.film_id.in_(film_ids)).all()
print(result_1)

# сортировка по film_id
film_idss = session.query(
    tables.Films.film_id,
    tables.Films.title
).order_by(tables.Films.film_id).all()

print(film_idss)

# обратная сортировка сортировка по film_id с лимитом 1 (сколько дать) и оффсетом 1 (сколько пропустить)
film_ids_re = session.query(
    tables.Films.film_id,
    tables.Films.title
).order_by(desc(tables.Films.film_id)).limit(1).offset(1).all()

print(film_ids_re)
"""
Пример объекта на котором вы можете потренироваться, используя pydantic схемы.
Example of object for training with pydantic schemas.
"""

"""
player = {
    "account_status": "ACTIVE",
    "balance": 10,
    "localize": {
            "en": {"nickname": "Руслан", "countries": {"RU": 3}, {"ennnnn": {"ab": {}}}},
            "ru": {"nickname": "Руслан"},
            'ennnnnn': {'countries': {}}
    },
    "avatar": "https://google.com/images/cars/420/420"
}
"""

computer = {
    "id": 21,
    "status": "ACTIVE",
    "activated_at": "2013-06-01",
    "expiration_at": "2040-06-01",
    "host_v4": "91.192.222.17",
    "host_v6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "detailed_info": {
        "physical": {
            "color": 'green',
            "photo": 'https://images.unsplash.com/photo-1587831990711-23ca6441447b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZGVza3RvcCUyMGNvbXB1dGVyfGVufDB8fDB8fA%3D%3D&w=1000&q=80',
            "uuid": "73860f46-5606-4912-95d3-4abaa6e1fd2c"
        },
        "owners": [{
            "name": "Stephan Nollan",
            "card_number": "4000000000000002",
            "email": "shtephan.nollan@gmail.com",
        }]
    }
}

# Package	Version	Relative Performance	Mean validation time
# pydantic	            1.7.3	                93.7μs
# attrs + cattrs	    20.3.0	1.5x slower	    143.6μs
# valideer	            0.4.2	1.9x slower	    175.9μs
# marshmallow	        3.10.0	2.4x slower	    227.6μs
# voluptuous	        0.12.1	2.7x slower	    257.5μs
# trafaret	            2.1.0	3.2x slower	    296.7μs
# schematics	        2.1.0	10.2x slower	955.5μs
# django-rest-framework	3.12.2	12.3x slower	1148.4μs
# cerberus	            1.3.2	25.9x slower	2427.6μs
