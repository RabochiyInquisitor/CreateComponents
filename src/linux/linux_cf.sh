read -p "Название компонента: " name

rest_of_name=$(echo "$name" | cut -c 2-)

first_symbol=$(echo "$name" | cut -c 1 | tr '[:lower:]' '[:upper:]')

echo "import { View, Text } from 'react-native'\nimport ${first_symbol}${rest_of_name}Style from './$name.style'\n\nexport const ${first_symbol}${rest_of_name} = () => {\n    return(\n        <View style={${first_symbol}${rest_of_name}Style.main}>\n            <Text>Hello world!</Text>\n        </View>\n    )\n}" > $name.tsx


echo "import { StyleSheet } from 'react-native'\n\n export const ${first_symbol}${rest_of_name}Style = StyleSheet.create({\n    main: {\n        flex: 1\n    }\n})" > $name.style.ts
