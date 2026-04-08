import random

from .encounters import battle, create_random_monster
from .models import Player


def random_room_event(player: Player) -> None:
    event = random.choice(["monster", "treasure", "trap", "nothing"])

    if event == "monster":
        battle(player, create_random_monster())
    elif event == "treasure":
        found = random.randint(5, 20)
        player.gold += found
        print("💰 You found", found, "gold coins!")
    elif event == "trap":
        dmg = random.randint(5, 15)
        player.take_damage(dmg)
        print("🪤 Trap! You lose", dmg, "health.")
    else:
        print("The room is quiet. Nothing happens.")


def treasure_room(player: Player) -> None:
    print("🏛️ You reach the Treasure Chamber!")
    print("A golden chest sits in the center...")
    player.has_treasure = True
    player.gold += 100
    print("💎 You claim the treasure worth 100 gold!")

