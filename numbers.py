# Напишите программу для слияния нескольких словарей в один.

my_friends = {
 "Joomart": "+996555246810",
 "Adinai": "+996555013579",
 "Ermek": "+996777013579",
 "Atai": "+996777246810",
 "Aslan": "+996999246810",
 }

his_her_friends = {
 "Lyazat": "+996551123456",
 "Salavat": "+996552234567",
 "Daniyar": "+996553345678",
 "Bolot": "+996554456789",
 "Alymbek": "+996555501234",
 "Dastan": "+996556678912",
 "Maksat": "+996557789012",
 "Aibek": "+996558890123",
 }

our_friends = my_friends | his_her_friends

print(our_friends)
