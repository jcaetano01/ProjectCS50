from project import choose_map, choose_weapon, choose_side

def test_choose_map(monkeypatch):
    inputs = iter(['1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    maps = ["de_heaven", "de_underpass", "de_dusty", "de_engine", "de_nuclear", "de_inca", "de_cxchz"]
    selected_map = choose_map(maps)

    assert selected_map == "de_heaven"

def test_choose_weapon(monkeypatch):

    inputs = iter(['2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    weapons = {
        "Ph4Mthon-S": "Medium accuracy and ideal for medium-range combat.",
        "Vankal-k7": "High power and damage but less accurate over long distances.",
        "Bullmas": "A balanced option between firepower and control.",
        "Umpectre": "Good for short distances and quick shootouts.",
        "AWperator": "Ideal for long distances with devastating power in one shot."
    }
    selected_weapon = choose_weapon(weapons)

    assert selected_weapon == "Vankal-k7"

def test_choose_side(monkeypatch):

    inputs = iter(['1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    selected_side = choose_side()

    assert selected_side == "Attacking"

def test_invalid_map_choice(monkeypatch):

    inputs = iter(['8', '0', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    maps = ["de_heaven", "de_underpass", "de_dusty", "de_engine", "de_nuclear", "de_inca", "de_cxchz"]

    selected_map = choose_map(maps)
    assert selected_map == "de_dusty"


def test_invalid_weapon_choice(monkeypatch):

    inputs = iter(['6', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    weapons = {
        "Ph4Mthon-S": "Medium accuracy and ideal for medium-range combat.",
        "Vankal-k7": "High power and damage but less accurate over long distances.",
        "Bullmas": "A balanced option between firepower and control.",
        "Umpectre": "Good for short distances and quick shootouts.",
        "AWperator": "Ideal for long distances with devastating power in one shot."
    }
    selected_weapon = choose_weapon(weapons)

    assert selected_weapon == "Vankal-k7"

def test_invalid_side_choice(monkeypatch):

    inputs = iter(['3', '1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    selected_side = choose_side()

    assert selected_side == "Attacking"
