from mock import Mock, patch
import unittest


class Human(object):
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender


def get_human(age, gender):
    if age > 100:
        raise ValueError('age too lage')
    if gender not in ['male', 'famale']:
        raise ValueError('gender must in <male, famale>')
    return Human(age, gender)


def test_get_human():
    result = get_human(20, 'male')
    assert result.age == 20
    assert result.gender == 'male'

    result = get_human(200, 'male')


if __name__ == '__main__':
    test_get_human()
