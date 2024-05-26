# Ohce Kata

## Descripción
Ohce es una aplicación de consola que ecoa el reverso de lo que ingresas a través de la consola.

Aunque parece una aplicación tonta, ohce sabe algunas cosas.

Cuando inicias ohce, te saluda de manera diferente dependiendo de la hora actual, pero solo en español:
- Entre las 20 y las 6 horas, ohce te saludará diciendo: ¡Buenas noches <tu nombre>!
- Entre las 6 y las 12 horas, ohce te saludará diciendo: ¡Buenos días <tu nombre>!
- Entre las 12 y las 20 horas, ohce te saludará diciendo: ¡Buenas tardes <tu nombre>!

Cuando introduces un palíndromo, a ohce le gusta y después de ecoar su reverso, agrega ¡Bonita palabra!

ohce sabe cuándo detenerse, solo tienes que escribir Stop! y él responderá Adiós <tu nombre> y terminará.

## Instrucciones de instalación

1. Clona el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución del programa

```bash
python -m src.main <nombre>

Reemplaza `<nombre>` con tu nombre.

```

## Ejecución de pruebas

```bash
python -m unittest discover tests
```

## Esctructura del proyecto

```
ohce-kata/
├── src/
│   └── ohce.py
│   └── main.py
├── tests/
│   └── test_ohce.py
├── README.md
└── requirements.txt
