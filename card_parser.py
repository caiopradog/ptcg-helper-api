from pokemontcgsdk import Card
from collections import defaultdict
import re


def normalize_card_name(card_name):
    return re.sub(' \((.*?)\)', '', card_name)


def get_card_name(card):
    return ' '.join(card.split(' ')[1:-2])


def make_card_query(deck_list):
    query = ''
    for card in deck_list:
        card_name = get_card_name(card)
        query = query + f'(!name:"{card_name}") or '
    query = query[:-4]
    print(query)
    return query


def get_cards(card_query):
    card = Card.where(q=card_query)
    return card


def group_cards(cards):
    grouped_cards = defaultdict(list)
    for card in cards:
        grouped_cards[card.name].append(card)
    return dict(grouped_cards.items())


def parse_deck_list(deck_list):
    card_query = make_card_query(deck_list)
    cards = get_cards(card_query)
    grouped_cards = group_cards(cards)
    return grouped_cards


# if __name__ == "__main__":


# TODO: Tratar cartas fora do padrão (deixar consultar poucas ou incluir as padronizadas)
# TODO: Validar padrão de lista do PTCG Online e Live
# TODO: Traduzir nome das energias ({D} Energy => Darkness Energy)