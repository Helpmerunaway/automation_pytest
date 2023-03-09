
import pytest
import requests
from src.generators.player_localization import PlayerLocalization
from src.enums.user_enums import Statuses

@pytest.mark.parametrize("status", [
    "ACTIVE",
    "BANNED",
    "DELETED",
    "INACTIVE"
])
def test_status_old(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize("status", Statuses.list())
def test_status_new(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize("balance_value", [
    "100",
    "0",
    "-10",
    "sd"
])
#@pytest.mark.parametrize("status", [status.value for status in Status])
def test_balance(balance_value, get_player_generator):
    print(get_player_generator.set_balance(balance_value).build())


@pytest.mark.parametrize("delete_key", [
    "account_status",
    "balance",
    "localize",
    "avatar"
])
def test_delete(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


def test_object(get_player_generator):
    object_to_send = get_player_generator.update_inner_generator(
        'localize', PlayerLocalization('fr_FR')).build()
    print(object_to_send)


def test_object_set_number(get_player_generator):
    object_to_send = get_player_generator.update_inner_generator(
        'localize', PlayerLocalization('fr_FR').set_number(15))\
        .build()
    print(object_to_send)


def test_object_set_number_value(get_player_generator):
    object_to_send = get_player_generator.update_inner_value(
        'localize', PlayerLocalization('fr_FR').set_number(15).build())\
        .build()
    print(object_to_send)


def test_object_set_localize_5(get_player_generator):
    object_to_send = get_player_generator.update_inner_value(
        'localize', 5)\
        .build()
    print(object_to_send)


def test_object_set_countries(get_player_generator):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', 'fr', 'is', 'the', 'best', 'lang'], PlayerLocalization('fr_FR')
        .set_number(15).build()).build()
    print(object_to_send)


@pytest.mark.parametrize('localizations, loc', [
    ("fr", "fr_FR")
])
def test_object_set_localize(get_player_generator, localizations, loc):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations], PlayerLocalization(loc)
        .set_number(15).build()).build()
    print(object_to_send)