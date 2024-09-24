import random

i = 0

class Hero():
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        power = random.randint(1, self.attack_power)
        print(f'Шаг {i}:\nИгрок "{self.name}" атаковал "{other.name}" силой {power}')
        other.health -= power
        print(f'Игрок "{other.name}" сохранил "{other.health}" единиц здорвья\n---------------')

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            print(f'💀 ИГРОК "{self.name}" УБИТ! 💀')
            return False

class Game():
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        global i
        while self.player.is_alive() and self.computer.is_alive():
            i += 1
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                break

            self.computer.attack(self.player)
            if not self.player.is_alive():
                break

# Инициализация игры
men = Hero("Человек", health=100, attack_power=20)
comp = Hero("Машина", health=100, attack_power=15)

# Запуск игры
game = Game(men, comp)
game.start()