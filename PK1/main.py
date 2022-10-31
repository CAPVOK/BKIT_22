from operator import itemgetter

# Язык программирования
# Средство разработки

class Language:
    def __init__(self, name, id, diificulity):
        self.name = name
        self.id = id
        self.diificulity = diificulity

class IDE:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class LanguageIDE:
    def __init__(self, language_id, ide_id):
        self.language_id = language_id
        self.ide_id = ide_id

languages = [
    Language('Python', 1, 1),
    Language('C++', 2, 2),
    Language('C#', 3, 3),
    Language('Java', 4, 4),
    Language('JavaScript', 5, 5),
    Language('PHP', 6, 6),
    Language('Ruby', 7, 7),
    Language('Swift', 8, 8),
    Language('Go', 9, 9),
    Language('Rust', 10, 10),
    Language('Kotlin', 11, 11),
    Language('Scala', 12, 12),
]

ides = [
    IDE('PyCharm', 1),
    IDE('Visual Studio', 2),
    IDE('Visual Studio Code', 3),
    IDE('IntelliJ IDEA', 4),
    IDE('Eclipse', 5),
    IDE('NetBeans', 6),
    IDE('Xcode', 7),
    IDE('Android Studio', 8),
    IDE('Rider', 9),
    IDE('CLion', 10),
    IDE('AppCode', 11),
    IDE('GoLand', 12),
]

language_ide = [
    LanguageIDE(1, 1),
    LanguageIDE(2, 2),
    LanguageIDE(3, 2),
    LanguageIDE(4, 4),
    LanguageIDE(5, 3),
    LanguageIDE(6, 5),
    LanguageIDE(7, 1),
    LanguageIDE(8, 7),
    LanguageIDE(9, 12),
    LanguageIDE(10, 10),
    LanguageIDE(11, 8),
    LanguageIDE(12, 4),
]

# Language and IDE соединены соотношением один-ко-многим.
# Вывести все среды разработки, содержащие "Studio"
# и соответствующие им языки программирования, согласно language_ide.

def task1():
    res = []    # Итог
    for ide in ides:
        mid_res = []    # Промежуточный итог
        if "Studio" in ide.name:
            for lang_ide in language_ide:
                if lang_ide.ide_id == ide.id:
                    for lang in languages:
                        if lang.id == lang_ide.language_id:
                            mid_res.append(lang.name)
            res.append([ide.name, mid_res])
    return res

# Language and IDE соединены соотношением один-ко-многим.
# Выведите список IDE со средней сложностью Language в каждом IDE,
# отсортированный по средней сложности.
# Средняя сложность должна быть округлена до 2 знака после запятой

def task2():
    res = []
    for ide in ides:
        mid_res = []
        sum = 0
        count = 0
        for lang_ide in language_ide:
            if lang_ide.ide_id == ide.id:
                for lang in languages:
                    if lang.id == lang_ide.language_id:
                        sum += lang.diificulity
                        count += 1
        try:
            mid_res.append(ide.name)
            mid_res.append(round(sum / count, 2))
            res.append(mid_res)
        except ZeroDivisionError:
            pass
    return sorted(res, key=itemgetter(1), reverse=False)

# «IDE» и «Language» связаны соотношением многие-ко-многим.
# Выведите список всех language, у которых название начинается с буквы «S»,
# и названия их IDE

def task3():
    res = []
    for lang in languages:
        mid_res = []
        if lang.name.startswith('S'):
            for lang_ide in language_ide:
                if lang_ide.language_id == lang.id:
                    for ide in ides:
                        if ide.id == lang_ide.ide_id:
                            mid_res.append(ide.name)
            res.append([lang.name, mid_res])
    return res

def main():
    print("Task 1: ")
    print(task1())

    print("Task 2: ")
    print(task2())

    print("Task 3: ")
    print(task3())

if __name__ == "__main__":
    main()
