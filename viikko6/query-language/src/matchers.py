from player import Player

class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class Not:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return True

        return False

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False

class All:
    def test(self, player):
        if isinstance(player, Player):
            return True
        return False

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value


class QueryBuilder:
    def __init__(self, matchers=All()) -> None:
        self._matchers = matchers

    def build(self):
        return self._matchers

    def playsIn(self, team):
        plays_in = QueryBuilder(And(self._matchers, PlaysIn(team)))
        return plays_in

    def hasAtLeast(self, value, attr):
        has_at_least = QueryBuilder(And(self._matchers, HasAtLeast(value, attr)))
        return has_at_least

    def hasFewerThan(self, value, attr):
        has_fewer_than = QueryBuilder(And(self._matchers, HasFewerThan(value, attr)))
        return has_fewer_than

    def oneOf(self, *matchers):
        one_of = QueryBuilder(Or(*matchers))
        return one_of
