import random

print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!")
poka_count = 0

while True:
    user_input = input()
    if user_input != user_input.upper():
        print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
        poka_count = 0
    elif user_input == "ПОКА!":
        poka_count += 1
        if poka_count == 3:
            print("ДО СВИДАНИЯ, МИЛЫЙ!")
            break
        else:
            year = random.randint(1930, 1950)
            print(f"НЕТ, НИ РАЗУ С {year} ГОДА!")
    else:
        year = random.randint(1930, 1950)
        print(f"НЕТ, НИ РАЗУ С {year} ГОДА!")
        poka_count = 0
