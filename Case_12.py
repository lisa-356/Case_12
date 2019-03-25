from local import *
import os


def main():
    while True:
        '''Меню программы'''
        print(os.getcwd())
        print(FIRST)
        print(SECOND)
        print(THIRD)
        print(FOURTH)
        print(FIFTH)
        print(SIXTH)
        print(SEVENTH)
        print()
        command = acceptCommand()
        runCommand(command)
        print()
        if command == 7:
            print(END)
            break


def acceptCommand():
    """Выбор пункта меню"""
    while True:
        try:
            number = int(input(DECISION))
            break
        except Exception:
            print(ERROR)
            print()
    return number


def runCommand(command):
    """"Выполнение необходимых функций"""
    if command == 1:
        path = os.getcwd()
        return printDirs(path)
    elif command == 2:
        print(RESULT)
        print(moveUp())
    elif command == 3:
        path = os.getcwd()
        return moveDown(path)
    elif command == 4:
        print(WHERE)
        print(ONE)
        print(TWO)
        print(THREE)
        decision = int(input(DECISION))
        if decision == 1:
            print(RESULT, countFiles(dir=os.getcwd(), list_of_files=[]))
        elif decision == 2:
            moveUp()
            print(RESULT, countFiles(dir=os.getcwd(), list_of_files=[]))
        elif decision == 3:
            moveDown(path=os.getcwd())
            print(RESULT, countFiles(dir=os.getcwd(), list_of_files=[]))
    elif command == 5:
        print(ONE)
        print(TWO)
        print(THREE)
        decision2 = int(input(DECISION2))
        if decision2 == 1:
            print(RESULT, countBytes(dir=os.getcwd(), size=0), BAIT)
        elif decision2 == 2:
            moveUp()
            print(RESULT, countBytes(dir=os.getcwd(), size=0), BAIT)
        elif decision2 == 3:
            moveDown(path=os.getcwd())
            print(RESULT, countBytes(dir=os.getcwd(), size=0), BAIT)
    elif command == 6:
        target = input(FOUND)
        print(findFiles(target, dir=os.getcwd()))


def printDirs(path):
    """Просмотр каталога"""
    list_dir = os.listdir(path)
    directory = []
    files = []
    print(RESULT)
    for b in list_dir:
        if os.path.isdir(b):
            directory.append(b)
        else:
            files.append(b)
    print(SUBDIRECTORY)
    print('\n'.join(directory))
    print(FILES)
    print('\n'.join(files))


def moveUp():
    """На уровень вверх"""
    path = os.getcwd()
    path = path.split('\\')
    path = path[:len(path) - 1]
    path = "\\".join(path)
    os.chdir(path)
    return path


def moveDown(path):
    """На уровень вниз"""
    while True:
        try:
            path = path + '\\' + input(FIND_SUBDIRECTORY)
            os.chdir(path)
            print(os.getcwd())
            break
        except FileNotFoundError:
            print(ERROR2)
    return path


def countFiles(dir, list_of_files):
    """Количество файлов"""
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            list_of_files.append(path)
        else:
            countFiles(path, list_of_files)
    return len(list_of_files)


def countBytes(dir, size):
    """Размер каталога + подкаталоги"""
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            size += os.path.getsize(path)
        else:
            countBytes(path, size)
    return size


def findFiles(target, dir):
    """Поиск файла в каталоге и подкаталогах"""
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path) and name == target:
            print(FOUND)
            return path
        else:
            return findFiles(target, dir)


main()