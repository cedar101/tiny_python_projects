from collections.abc import Generator
import random

ADJECTIVES = """
bankrupt base caterwauling corrupt cullionly detestable dishonest false
filthsome filthy foolish foul gross heedless indistinguishable infected
insatiate irksome lascivious lecherous loathsome lubbery old peevish
rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
thin-faced toad-spotted unmannered vile wall-eyed
""".strip().split()

NOUNS = """
Judas Satan ape ass barbermonger beggar block boy braggart butt
carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
gull harpy jack jolthead knave liar lunatic maw milksop minion
ratcatcher recreant rogue scold slave swine traitor varlet villain worm
""".strip().split()


def insult(adjectives: int = 2, number: int = 3, seed: int = None) -> Generator[str]:
    random.seed(seed)
    for _ in range(number):
        adjs = ", ".join(random.sample(ADJECTIVES, k=adjectives))
        yield f"You {adjs} {random.choice(NOUNS)}!"
