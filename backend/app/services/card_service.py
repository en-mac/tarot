import random

class CardService:
    @staticmethod
    def draw_card():
        cards = ["The Fool", "The Magician", "The High Priestess"]
        selected_card = random.choice(cards)
        # Logic to generate fortune text for the selected card
        fortune_text = f"The card you drew is {selected_card}. It signifies..."
        return {"card_name": selected_card, "fortune_text": fortune_text}
