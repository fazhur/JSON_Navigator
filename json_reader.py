"""Navigator on the given json-file"""
import json
from json.decoder import JSONDecodeError


def convert_to_dict():
    """Converts json dictionary to python dictionary"""
    while True:
        path = input('Enter a path to your json-dictionary: ')
        try:
            with open(path, 'r', encoding='utf-8') as file:
                dictionary = json.load(file)
                return dictionary
        except FileNotFoundError:
            print('This path does not exist, try again')
        except IsADirectoryError:
            print('This is a directory, choose path to file')
        except JSONDecodeError:
            print('This is not a JSON-file, try again')


def navigation(object):
    """Provides a navigation is the python dictionary recursively"""
    if type(object) not in {dict, list}:
        print('This is a ', object.__class__.__name__, ': ', object, sep='')
        print('Thank you for using this product!')
    elif type(object) == list:
        print('This is a list of', len(object), 'elements')
        print('List:', object)
        while True:
            choice = int(input('Choose number of element you want to enter: '))
            if type(choice) != int:
                print('You need to enter integer, try again')
            elif choice not in range(len(object)):
                print('Your number is out of the list range, try again')
            else:
                navigation(object[choice])
                break
    else:
        print('This is a dictionary with such keys:')
        print(object.keys())
        while True:
            choice = input('Choose neccessary key: ')
            if choice in object.keys():
                navigation(object[choice])
                break
            else:
                print('This key does not exist, try again')


if __name__ == "__main__":
    navigation(convert_to_dict())
