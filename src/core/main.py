import argparse
from config import extension, framework

def textConstructor(name, framework, need_style):
    if framework == "react-native": 
        if need_style:
            return [f"import {{ View, Text }} from 'react-native'\nimport {name[0].upper() + name[1:]}Style from './{name}.style'\n\nexport const {name[0].upper() + name[1:]} = () => {{\n    return(\n        <View style={{{name[0].upper() + name[1:]}Style.main}}>\n          <Text>Hello from cf!</Text>\n        </View>\n    )\n}}", f"import {{ StyleSheet }} from 'react-native'\n\nexport const {name[0].upper() + name[1:]}Style = StyleSheet.create({{\n    main: {{\n\n    }}\n}})"]
        else:
            return [f"import {{ View, Text }} from 'react-native'\n\nexport const {name[0].upper() + name[1:]} = () => {{\n    return(\n        <View>\n          <Text>Hello from cf!</Text>\n        </View>\n    )\n}}"]
   
    else:
        return f"import React, {{ useState }} from 'react'\n\nexport const {name[0].upper() + name[1:]} = () => {{\n    return(\n        <div class='main'>\n          <p>Hello from cf!</p>\n        </div>\n    )\n}}"

def createReactComponent(extension, name, need_style):
    with open(f"{name}{extension}", 'w') as f:
        f.write(textConstructor(name, 'react'))
    if need_style:
        with open(f"{name}.style.css", "a") as f:
            f.write("main { \n\n}")


def createReactNativeComponent(extension, name, need_style):
    if need_style:
        with open(f"{name}{extension}", 'w') as f:
            f.write(textConstructor(name, 'react-native', True)[0])
        with open(f"{name}.style{extension}", "a") as f:
            f.write(textConstructor(name, 'react-native', True)[1])
    else:
        with open(f"{name}{extension}", 'w') as f:
            f.write(textConstructor(name, 'react-native', False)[0])

parser = argparse.ArgumentParser(description="main", prog="cf")
subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

parser.add_argument('--ws', action='store_true', help="Наличие флага отключает создание стилей")

parser.add_argument('--name', type=str, help="Устанавливает имя компонента и стиля")

args = parser.parse_args()

if args.name: 
    if framework == "react":
        if args.ws:
            createReactComponent(extension, args.name, False)
        else:
            createReactComponent(extension, args.name, True)
    elif framework == "react-native":
        if args.ws:
            createReactNativeComponent(extension, args.name, False)
        else:
            createReactNativeComponent(extension, args.name, True)
else:
    name = input("Имя вашего компонента: ")
    if framework == "react":
        if args.ws:
            createReactComponent(extension, name, False)
        else:
            createReactComponent(extension, name, True)
    elif framework == "react-native":
        if args.ws:
            createReactNativeComponent(extension, name, False)
        else:
            createReactNativeComponent(extension, name, True)





