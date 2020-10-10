# This file is part of Project Deity.
# Copyright 2020, Frostflake (L.A.)
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

from item import Item
from deity import Deity


def run_item_tests():
    print("Testing Item class...")
    print("1. Create item.")
    test_item1 = Item("Orb of Readiness", "Weapon", "orb.jpg",
                      100, 10, attributes={"attack": 1})
    test_item2 = Item("Orb of Readiness", "Shield", "bright_orb.jpg",
                      250, 15, rarity=1, modifier="Bright")
    print("2. Get item name.")
    assert test_item1.name == "Orb of Readiness"
    assert test_item2.name == "Orb of Readiness"
    print("3. Get item class type.")
    assert test_item1.class_type == "Weapon"
    assert test_item2.class_type == "Shield"
    print("4. Get item image.")
    assert test_item1.get_image() == "./images/items/orb.jpg"
    assert test_item2.get_image() == "./images/items/bright_orb.jpg"
    print("5. Get item value.")
    assert test_item1.value == 100
    assert test_item2.value == 250
    print("6. Get item rarity.")
    assert test_item1.rarity == 0
    assert test_item2.rarity == 1
    print("7. Get item modifier.")
    assert test_item1.modifier == ""
    assert test_item2.modifier == "Bright"
    print("8. Get item weight.")
    assert test_item1.weight == 10
    assert test_item2.weight == 15
    print("9. Get item attributes.")
    assert test_item1.attributes["attack"] == 1
    assert len(test_item2.attributes) == 0
    print("10. Get item description.")
    assert "Orb of Readiness" in str(test_item1)
    assert "100 gold" in str(test_item1)
    assert "weighs 10" in str(test_item1)
    assert "Bright Orb of Readiness" in str(test_item2)
    assert "250 gold" in str(test_item2)
    assert "weighs 15" in str(test_item2)
    print("Item class passed all tests!")


def run_deity_tests():
    print("Testing Deity class...")
    print("1. Create deity.")
    test_deity1 = Deity(1, "Tester")
    test_deity2 = Deity(2, "Testing", bridge_info={'discord': 12315436})
    print("2. Get deity ID.")
    assert test_deity1.id == 1
    assert test_deity2.id == 2
    print("3. Get deity name.")
    assert test_deity1.name == "Tester"
    assert test_deity2.name == "Testing"
    print("4. Check if character slots are available.")
    assert test_deity1.can_create_character()
    assert test_deity2.can_create_character()
    print("5. Check if Discord bridge is activated.")
    assert not test_deity1.discord_enabled()
    assert test_deity2.discord_enabled()
    print("Deity class passed all tests!")


def run_tests():
    run_item_tests()
    run_deity_tests()


if __name__ == '__main__':
    run_tests()
