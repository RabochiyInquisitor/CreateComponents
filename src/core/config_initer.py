import os

current_directory = os.getcwd()

osList = {'1': 'Windows', '2': 'Linux'}
languages = {'1': 'Русский', '2': 'English'}
extensions = {'1': '.tsx', '2': '.jsx'}
frameworks = {'1': 'react', '2': 'react-native'}


print("\nДобро пожаловать в componentFactory!\n\nДавайте настроим работу фабрики под ваши предпочтения: ")


os_number = input("\n\nВаша операционная система:\n\n1. Windows\n2. Linux\n(Номер): ")
while os_number != '1' and os_number != '2':
    os_number = input(f"\n\n1. Windows\n2. Linux\n(Номер): ")


language_number = input("\n\nВаш язык: \n\n1. Русский\n2. English\n(Номер): ")
while language_number != '1' and language_number != '2':
    language_number = input(f"\n\nВаш язык: \n\n1. Русский\n2. English\n(Номер): ")


extensions_number = input("\n\nРасширение компонентов: \n\n1. tsx\n2. jsx\n(Номер): ")
while extensions_number != '1' and extensions_number != '2':    
    extensions_number = input(f"Расширение компонентов: \n\n1. tsx\n2. jsx\n(Номер): ")


frameworks_number = input("\n\nФреймворк: \n\n1. react\n2. react-native\n(Номер): ")
while frameworks_number != '1' and frameworks_number != '2':              
    frameworks_number = input(f"\n\nФреймворк: \n\n1. react\n2. react-native\n(Номер): ")
if frameworks_number == '1':
    style_extension = input("\n\nРасширение для стилей: \n\n1. css\n2. scss\n(Номер): ")
    while style_extension != '1' and style_extension != '2':
        style_extension = input("\n\nРасширение для стилей: \n\n1. css\n2. scss\n(Номер): ")
    with open('config.py', 'a', encoding='utf-8') as f:
        f.write(f"\nstyle_extension = '{style_extension}'")

with open('config.py', 'w', encoding='utf-8') as f:
    f.write(f"osName = '{osList[os_number]}'\nlanguage = '{languages[language_number]}'\nextension = '{extensions[extensions_number]}'\nframework = '{frameworks[frameworks_number]}'")


print("\n\nНастройки успешно применены. Теперь вы можете использовать фабрику командой cf. Удачного программирования!")
