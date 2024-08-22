import re
from typing import Optional, Tuple
class TextDataExtractor:
    def __init__(self):
        """
        Initializes the TextDataExtractor class.
        """
        # Compile regular expressions as they are static patterns used multiple times.
        self.amount_pattern = re.compile(r'\b(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\b')
        self.person_pattern = re.compile(r'\b\d{11}\s+([\w\s]+)')

    def extract_amount_and_person(self, text: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Extracts the amount and the person's name from the given text.

        :param text: The text from which to extract the amount and person's name.
        :return: A tuple containing the amount as a string and the person's name, or None if not found.
        """
        # Search for the amount in the text
        amount_match = self.amount_pattern.findall(text)
        # Assuming the largest number found is the amount
        if amount_match:
            amount = max(amount_match, key=lambda x: float(x.replace(',', '')))
        else:
            amount = None

        # Search for the person's name in the text
        person_match = self.person_pattern.search(text)
        person = person_match.group(1).strip() if person_match else None

        return amount, person