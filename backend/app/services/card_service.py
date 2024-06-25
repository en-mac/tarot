import random

class CardService:
    @staticmethod
    def draw_card():
        cards = [
            {"card_name": "00-TheFool", "fortune_text": "New beginnings and adventures."},
            {"card_name": "01-TheMagician", "fortune_text": "Skill, logic, and intellect."},
            {"card_name": "02-TheHighPriestess", "fortune_text": "Intuition, wisdom, and secrets."},
            {"card_name": "03-TheEmpress", "fortune_text": "Fertility, creation, and abundance."},
            {"card_name": "04-TheEmperor", "fortune_text": "Authority, structure, and control."},
            {"card_name": "05-TheHierophant", "fortune_text": "Tradition, conformity, and morality."},
            {"card_name": "06-TheLovers", "fortune_text": "Love, harmony, and relationships."},
            {"card_name": "07-TheChariot", "fortune_text": "Determination, control, and success."},
            {"card_name": "08-Strength", "fortune_text": "Courage, patience, and compassion."},
            {"card_name": "09-TheHermit", "fortune_text": "Introspection, solitude, and guidance."},
            {"card_name": "10-WheelOfFortune", "fortune_text": "Change, cycles, and fate."},
            {"card_name": "11-Justice", "fortune_text": "Fairness, truth, and law."},
            {"card_name": "12-TheHangedMan", "fortune_text": "Suspension, release, and new perspectives."},
            {"card_name": "13-Death", "fortune_text": "Transformation, endings, and new beginnings."},
            {"card_name": "14-Temperance", "fortune_text": "Balance, moderation, and purpose."},
            {"card_name": "15-TheDevil", "fortune_text": "Addiction, materialism, and playfulness."},
            {"card_name": "16-TheTower", "fortune_text": "Sudden change, upheaval, and revelation."},
            {"card_name": "17-TheStar", "fortune_text": "Hope, faith, and rejuvenation."},
            {"card_name": "18-TheMoon", "fortune_text": "Illusion, fear, and anxiety."},
            {"card_name": "19-TheSun", "fortune_text": "Positivity, fun, and success."},
            {"card_name": "20-Judgement", "fortune_text": "Judgement, rebirth, and inner calling."},
            {"card_name": "21-TheWorld", "fortune_text": "Completion, integration, and accomplishment."},
            {"card_name": "Cups01", "fortune_text": "Emotion, intuition, and relationships."},
            {"card_name": "Cups02", "fortune_text": "Partnership, love, and attraction."},
            {"card_name": "Cups03", "fortune_text": "Celebration, friendship, and creativity."},
            {"card_name": "Cups04", "fortune_text": "Apathy, contemplation, and disconnection."},
            {"card_name": "Cups05", "fortune_text": "Loss, regret, and disappointment."},
            {"card_name": "Cups06", "fortune_text": "Nostalgia, childhood, and memories."},
            {"card_name": "Cups07", "fortune_text": "Choices, fantasies, and imagination."},
            {"card_name": "Cups08", "fortune_text": "Abandonment, withdrawal, and moving on."},
            {"card_name": "Cups09", "fortune_text": "Contentment, satisfaction, and gratitude."},
            {"card_name": "Cups10", "fortune_text": "Harmony, joy, and family."},
            {"card_name": "Cups11", "fortune_text": "Creativity, compassion, and new relationships."},
            {"card_name": "Cups12", "fortune_text": "Emotional balance, generosity, and stability."},
            {"card_name": "Cups13", "fortune_text": "Emotional intelligence, compassion, and intuition."},
            {"card_name": "Cups14", "fortune_text": "Self-love, intuition, and emotional fulfillment."},
            {"card_name": "Pentacles01", "fortune_text": "New beginnings, prosperity, and abundance."},
            {"card_name": "Pentacles02", "fortune_text": "Balance, adaptability, and prioritization."},
            {"card_name": "Pentacles03", "fortune_text": "Collaboration, skill, and effort."},
            {"card_name": "Pentacles04", "fortune_text": "Security, stability, and control."},
            {"card_name": "Pentacles05", "fortune_text": "Hardship, lack, and insecurity."},
            {"card_name": "Pentacles06", "fortune_text": "Generosity, charity, and kindness."},
            {"card_name": "Pentacles07", "fortune_text": "Patience, investment, and growth."},
            {"card_name": "Pentacles08", "fortune_text": "Diligence, craftsmanship, and mastery."},
            {"card_name": "Pentacles09", "fortune_text": "Luxury, self-sufficiency, and financial gain."},
            {"card_name": "Pentacles10", "fortune_text": "Wealth, legacy, and family."},
            {"card_name": "Pentacles11", "fortune_text": "Ambition, diligence, and financial opportunity."},
            {"card_name": "Pentacles12", "fortune_text": "Financial security, investment, and family."},
            {"card_name": "Pentacles13", "fortune_text": "Success, financial stability, and generosity."},
            {"card_name": "Pentacles14", "fortune_text": "Wealth, abundance, and generosity."},
            {"card_name": "Swords01", "fortune_text": "Clarity, truth, and new ideas."},
            {"card_name": "Swords02", "fortune_text": "Decision, stalemate, and choice."},
            {"card_name": "Swords03", "fortune_text": "Heartbreak, pain, and suffering."},
            {"card_name": "Swords04", "fortune_text": "Rest, recovery, and contemplation."},
            {"card_name": "Swords05", "fortune_text": "Conflict, defeat, and loss."},
            {"card_name": "Swords06", "fortune_text": "Transition, change, and moving on."},
            {"card_name": "Swords07", "fortune_text": "Deception, strategy, and tactics."},
            {"card_name": "Swords08", "fortune_text": "Restriction, fear, and entrapment."},
            {"card_name": "Swords09", "fortune_text": "Anxiety, worry, and nightmares."},
            {"card_name": "Swords10", "fortune_text": "Endings, betrayal, and loss."},
            {"card_name": "Swords11", "fortune_text": "Intellect, authority, and truth."},
            {"card_name": "Swords12", "fortune_text": "Cleverness, intellect, and wit."},
            {"card_name": "Swords13", "fortune_text": "Power, truth, and intellectual strength."},
            {"card_name": "Swords14", "fortune_text": "Wisdom, authority, and truth."},
            {"card_name": "Wands01", "fortune_text": "Inspiration, potential, and new beginnings."},
            {"card_name": "Wands02", "fortune_text": "Planning, decisions, and progress."},
            {"card_name": "Wands03", "fortune_text": "Expansion, foresight, and leadership."},
            {"card_name": "Wands04", "fortune_text": "Celebration, harmony, and home."},
            {"card_name": "Wands05", "fortune_text": "Conflict, competition, and challenge."},
            {"card_name": "Wands06", "fortune_text": "Victory, success, and recognition."},
            {"card_name": "Wands07", "fortune_text": "Perseverance, challenges, and endurance."},
            {"card_name": "Wands08", "fortune_text": "Speed, action, and movement."},
            {"card_name": "Wands09", "fortune_text": "Resilience, courage, and persistence."},
            {"card_name": "Wands10", "fortune_text": "Burden, responsibility, and hard work."},
            {"card_name": "Wands11", "fortune_text": "Vision, creativity, and inspiration."},
            {"card_name": "Wands12", "fortune_text": "Discovery, enthusiasm, and exploration."},
            {"card_name": "Wands13", "fortune_text": "Courage, charm, and determination."},
            {"card_name": "Wands14", "fortune_text": "Charisma, leadership, and vision."}
        ]
        selected_card = random.choice(cards)
        return selected_card
