import random

tarot_card_meanings = {
    "The Fool": "You are beginning a new journey or adventure. Take risks, be spontaneous, and trust your instincts.",
    "The Magician": "You have the power to manifest your desires into reality. Focus on your goals and use your skills to achieve them.",
    "The High Priestess": "Trust your intuition and inner voice. Secrets and mysteries may be revealed to you.",
    "The Empress": "Nurture and care for yourself and others. Fertility, creativity, and abundance are highlighted.",
    "The Emperor": "Be a leader and take control of your life. Use your power and authority wisely.",
    "The Hierophant": "Seek guidance and wisdom from a mentor or teacher. Traditional values and beliefs may be important.",
    "The Lovers": "Make choices that align with your values and heart. Love, partnership, and harmony are emphasized.",
    "The Chariot": "Move forward with confidence and determination. Success and victory are possible.",
    "Strength": "Use your inner strength and courage to overcome obstacles. Compassion and patience may be needed.",
    "The Hermit": "Take time for introspection and reflection. Solitude and spiritual growth may be necessary.",
    "The Wheel of Fortune": "Life is full of ups and downs. Embrace change and be open to new opportunities.",
    "Justice": "Fairness, balance, and honesty are key. Seek the truth and act with integrity.",
    "The Hanged Man": "Surrender and let go of control. A shift in perspective may be necessary.",
    "Death": "A major transformation or ending is coming. Embrace the change and let go of the past.",
    "Temperance": "Find balance and harmony in all areas of your life. Moderation and self-control are important.",
    "The Devil": "Beware of temptation and negative influences. Materialism and addiction may be present.",
    "The Tower": "A sudden and unexpected change or upheaval is coming. Release attachments and embrace new beginnings.",
    "The Star": "Hope, inspiration, and optimism are present. Follow your dreams and have faith in the future.",
    "The Moon": "Listen to your intuition and pay attention to your dreams. Emotions and subconscious thoughts may be heightened.",
    "The Sun": "Joy, happiness, and success are possible. Embrace positivity and gratitude.",
    "Judgment": "A call to action or awakening is coming. Embrace change and transformation.",
    "The World": "Completion, fulfillment, and achievement are possible. Celebrate your accomplishments."
}

random_card = random.choice(list(tarot_card_meanings.keys()))

print("Your daily tarot card is:", random_card)
print("Meaning:", tarot_card_meanings[random_card])