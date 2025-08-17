# #1) a += dla listy i stringa oznacza „rozbij string na literki i dodaj każdą literkę osobno do listy”
# WHY ERROR?
# heroes_names to lista.
# character_name to string.
# += w tym przypadku oznacza „dodaj każdy znak stringa osobno do listy” → działa, ale nie tak jak chcesz.
# heroes_health to lista.
# character_health to float.
# tutaj += nie działa, bo float nie jest iterowalny → stąd błąd: not supported for types list and float.

# heroes_names = []
# heroes_names += "Aria"
# print(heroes_names)  
# # wynik: ['A', 'r', 'i', 'a']

#2) To add a whole object to the list 👉 Rozwiązanie: zamiast += użyj .append():

# heroes_names.append(character_name)
# heroes_health.append(character_health)
# heroes_attack.append(character_strength)


#3) Saving hero as a DICTIONARY!!
# hero = {
#         "name": character_name,
#         "type": character_type,
#         "health": character_health,
#         "attack": character_strength
#     }
    
#     heroes.append(hero)

#4) Hero as a CLASS! I will not use it,because i only need 2 characters per battle, easier to do so with dictionary
# class Character:
#     def __init__(self, name, type_, health, attack):
#         self.name = name
#         self.type = type_
#         self.health = health
#         self.attack = attack

# heroes = []

# for i in range(2):
#     name, type_ = generate_character()
#     h = health()
#     a = attack()
#     hero = Character(name, type_, h, a)
#     heroes.append(hero)

# # dostęp:
# print(heroes[0].name, "vs", heroes[1].name)
# print(heroes[0].name, "has", heroes[0].health, "HP")
