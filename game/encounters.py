import random

from .models import Monster, Player


def create_random_monster() -> Monster:
    monster_types = [
        ("Goblin", 40, (6, 12), 10),
        ("Orc", 55, (8, 14), 15),
        ("Skeleton Warrior", 45, (7, 13), 12),
    ]
    name, hp, (a_min, a_max), gold = random.choice(monster_types)
    return Monster(
        name=name,
        max_health=hp,
        health=hp,
        attack_min=a_min,
        attack_max=a_max,
        gold_reward=gold,
    )


def battle(player: Player, monster: Monster) -> None:
    print("⚔️ A wild " + monster.name + " appears!")

    while player.health > 0 and monster.is_alive():
        print()
        print(monster.name + " Health:", monster.health, "/", monster.max_health)
        print("Your Health:", player.health, "/", player.max_health)
        print("1. Attack")
        print("2. Heal")
        choice = input("Choose (1-2): ").strip()

        if choice == "1":
            dmg = random.randint(10, 18)
            monster.take_damage(dmg)
            print("💥 You attack for", dmg, "damage!")
        elif choice == "2":
            heal = random.randint(10, 20)
            player.heal(heal)
            print("✨ You heal for", heal, "health!")
        else:
            print("You hesitate...")

        if monster.is_alive():
            mdmg = random.randint(monster.attack_min, monster.attack_max)
            player.take_damage(mdmg)
            print("🔥 " + monster.name + " attacks for", mdmg, "damage!")

    if player.health <= 0:
        print("💀 You were defeated...")
        return

    print("🎉 You defeated the " + monster.name + "!")
    player.gold += monster.gold_reward
    print("You earned", monster.gold_reward, "gold.")

