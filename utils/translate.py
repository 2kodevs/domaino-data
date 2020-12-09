translate = [
    # Strategies
    ('BigDrop', 'Bota Gorda'),
    ('SmallDrop', 'Bota Flaca'),
    ('AlwaysDouble', 'Siempre doble'),
    ('DataDropper', 'Gastar la data'),
    ('DataKeeper', 'No gastar la data'),
    ('LessPlayed', 'Menos Jugada'),
    ('Passer', 'Pasador'),
    ('Repeater', 'Repetidor'),
    ('Frequent', 'Más Frecuente'),
    ('Random', 'Aleatorio'),
    ('SimpleHybrid', 'Inteligente'),
    ('TableCounter', 'Contador de la mesa'),
    ('Supportive', 'Cooperativo'),

    # Behaviors
    ('BestAccompanied', 'Mejor acompañada'),
    ('Higher', 'Más alta'),
    ('Best', 'Más alta mejor acompañada'),
    ('FakeStart', 'Salida a la falla'),

    # Rules
    ('OneGame', 'Un juego'),
    ('TwoOfThree', 'Dos de Tres'),
    ('FirstToGain100', 'Partida a ganar 100'),
    ('FirstDouble', 'Primera doble'),
    ('CapicuaDoble', 'Capicúa doble'),
]


file = input('Enter the path of the file to translate:\n')
text = open(file, 'r').read()
for english, spanish in translate:
    text = text.replace(english, spanish)
file = input('Enter the path for the output file:\n')
open(file, 'w').write(text)