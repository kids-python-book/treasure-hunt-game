from .models import Player
from .rooms import random_room_event, treasure_room


def run_game() -> None:
    print("🏝️ Welcome to Python Island! 🏝️")
    name = input("What's your adventurer's name? ").strip() or "Adventurer"

    player = Player(name=name)
    current_room = 1
    max_rooms = 5

    while player.health > 0 and current_room <= max_rooms:
        print()
        print("--- Room", current_room, "---")

        if current_room == max_rooms:
            treasure_room(player)
            break

        random_room_event(player)
        if player.health <= 0:
            break

        print("Status: Health:", player.health, "Gold:", player.gold)
        input("Press Enter to continue...")
        current_room += 1

    print()
    print("=== GAME OVER ===")
    if player.health <= 0:
        print("💀 Your adventure ends here...")
    elif player.has_treasure:
        print("🏆 You escaped with the treasure!")
    else:
        print("You leave the island for now...")

    print("Final Gold:", player.gold)

