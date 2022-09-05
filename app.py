from flask_cors import CORS
from flask import Flask, request
from card_parser import parse_deck_list

app = Flask(__name__)
CORS(app)


@app.route("/get_deck_cards")
def get_deck_cards():
    deck_list = request.args.get('deck_list', '').split(';')
    if len(deck_list) == 0:
        return {
            "error": "Deck não encontrado"
        }

    grouped_cards = parse_deck_list(deck_list)
    return grouped_cards


if __name__ == "__main__":
    app.run()