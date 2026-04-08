from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Player:
    name: str
    max_health: int = 100
    health: int = 100
    gold: int = 0
    has_treasure: bool = False

    def heal(self, amount: int) -> None:
        self.health = min(self.max_health, self.health + amount)

    def take_damage(self, amount: int) -> None:
        self.health = max(0, self.health - amount)


@dataclass
class Monster:
    name: str
    max_health: int
    health: int
    attack_min: int
    attack_max: int
    gold_reward: int

    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, amount: int) -> None:
        self.health = max(0, self.health - amount)

