import random

class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self._health = health  # <--- Внимание на черточку!
        self._max_health = health # Запомним максимум
        self.damage = damage

    # Мы создаем "кнопку" для изменения здоровья
    def take_damage(self, damage):
        self._health -= damage
        # Внутри метода мы можем добавить ПРОВЕРКИ (Валидацию)
        if self._health < 0:
            self._health = 0
        print(f"💥 {self.name} получил {damage} урона. Текущее здоровье: {self._health}")

    def attack(self, other):
        print(f"⚔️ {self.name} наносит удар по {other.name}!")
        other.take_damage(self.damage)

    def heal(self):
        self._health += 10
        # Не даем вылечиться выше максимума!
        if self._health > self._max_health:
            self._health = self._max_health

     # Полезный метод, чтобы проверять, не закончилась ли игра
    def is_alive(self):
        return self._health > 0



class Hero(Character):
    # Мы не пишем __init__, он наследуется автоматически!
    
    def heal(self):
        # Лечим на 20% от текущего здоровья, но не больше 100 (условно)
        heal_amount = 10
        self._health += heal_amount
        print(f"✨ {self.name} применил магию и восстановил {heal_amount} HP. Теперь здоровья: {self._health}")

class Archer(Hero):
    def attack(self, other):
        if random.random < 0.2:
            print(f"Промах! {self.name} выстрелил мимо! Лох!")
        else:
            print(f"⚔️ {self.name} стреляет по {other.name}!")
            other.take_damage(self.damage)

class Paladin(Hero):
    def __init__(self, name, health, armour, damage):
        self.name = name
        self._health = health  
        self._armour = armour # Броня
        self._max_health = health 
        self.damage = damage
    
    def take_damage(self, damage, ):
        itog = (damage - self._armour)
        if itog > 0:
            self._health -= itog
            print(f"💥 {self.name} получил {itog} урона. Текущее здоровье: {self._health}")
        else:
            print(f"{self.name} не получает урона! Броня его уберегла!")

class Vampire(Character):
    def attack(self, other):
        print(f"⚔️ Вампир {self.name} наносит удар по {other.name}!")
        t = other._health
        other.take_damage(self.damage)
        self._health += ((t - other._health) / 10)
        if self._health > self._max_health:
            self._health = self._max_health
        print(f"{self.name} исцелился, испив крови! Теперь его здоровье {self._health} ")




import time

# Представим, что классы Character, Hero, Warrior, Mage, Enemy описаны выше

# 1. СОЗДАНИЕ БОЙЦОВ
# Игрок выбирает класс (в нашем коде жестко зададим Воина)
player = Paladin("Conan", 120, 5, 15)

# Генерируем врага
enemy = Vampire("Vamp", 100, 15)

print("--- 🔔 БОЙ НАЧИНАЕТСЯ! ---")
print(player)
print(enemy)
print("-" * 30)

# 2. ИГРОВОЙ ЦИКЛ
# Битва идет, пока оба живы (используем метод is_alive, который мы писали ранее)
while player.is_alive() and enemy.is_alive():
    time.sleep(1.5) # Пауза для драматизма
    
    # --- Ход Игрока ---
    # Нам не важно, Воин это или Маг. Метод attack() сам разберется, что делать.
    player.attack(enemy)
    
    # Проверка победы сразу после удара
    if not enemy.is_alive():
        print(f"\n🏆 {player.name} ОДЕРЖАЛ ПОБЕДУ!")
        break
    
    # --- Ход Врага ---
    enemy.attack(player)
    
    # Проверка поражения
    if not player.is_alive():
        print(f"\n💀 {player.name} пал в бою... Game Over.")
        break
    
    # --- Дополнительная логика (Фишка ООП) ---
    # Если герой сильно побит, он может попытаться полечиться
    # Проверяем: если здоровье меньше 30% и повезло с рандомом
    if player._health < 40 and random.random() < 0.3:
        print("   🚑 Герой пытается найти зелье...")
        player.heal() # Этот метод есть только у Hero и его наследников!

print("-" * 30)