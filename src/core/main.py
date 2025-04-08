import argparse
from "config.py" import { extension, framework } 

parser = argparse.ArgumentParser(description="main")

parser.add_argument('need_style', '--ws', type="string", help="Наличие флага отключает создание стилей")

parser.add_argument('name', '--name', type="string", help="Устанавливает имя компонента и стиля")

args = parser.parse_args()

if args.name: 
    if framework == "react":
        if args.need_style:
            createReactComponent(extension, args.name)
    else if framework == "react-native"



def createReactComponent(extension, name, need_style):
    with open(f"{name} + {extension}", "import React, { useState } from 'react'\n\nexport const {name[0].upper() + name[1:]} = () => {\n    return(\n        <div class='main'>\n          <p>Hello from cf!</p>\n        </div>\n    )\n}")
    with open(f"{name} + .style + .css", "main { \n\n}") if need_style else pass

