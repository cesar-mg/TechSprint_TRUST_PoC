import spacy
import re
import pandas as pd
class ContractEntityExtractor:
    """
    A class to extract entities (persons or organizations) and associated monetary amounts from text,
    and store them in a pandas DataFrame.
    
    Attributes:
    -----------
    nlp : spacy.language.Language
        A spaCy language model for processing Spanish text.
    amount_pattern : re.Pattern
        A compiled regular expression pattern for detecting monetary amounts in RD$ format.
    entity_pattern : re.Pattern
        A compiled regular expression pattern for detecting entities following the specific pattern.
    
    Methods:
    --------
    extract_entities_and_amounts(text: str) -> pd.DataFrame:
        Extracts entities and corresponding amounts from the given text and returns them in a DataFrame.
    """
    
    def __init__(self, model: str = "es_core_news_sm"):
        """
        Initializes the ContractEntityExtractor with a specified spaCy model.
        
        Parameters:
        -----------
        model : str, optional
            The name of the spaCy model to use for entity recognition (default is "es_core_news_sm").
        """
        # Load the specified spaCy model
        self.nlp = spacy.load(model)
        
        # Regular expression pattern to detect monetary amounts in RD$ format
        self.amount_pattern = re.compile(r'RD\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?')
        
        # Regular expression pattern to detect entities (either organization or full names)
        self.entity_pattern = re.compile(r'\d+-\s*([\w\s,.]+?S\.R\.L\.|[\w\s,.]+?S\.A\.|[\w\s]+)\s*,')
    
    def extract_entities_and_amounts(self, text: str) -> pd.DataFrame:
        """
        Extracts entities and associated monetary amounts from the provided text,
        and stores them in a pandas DataFrame.
        
        Parameters:
        -----------
        text : str
            The text from which entities and amounts are to be extracted.
        
        Returns:
        --------
        pd.DataFrame
            A DataFrame with columns "Entity" and "Amount" containing the extracted entities and their corresponding amounts.
        """
        doc = self.nlp(text)
        entities_and_amounts = []
        
        # Iterate through each sentence in the processed text
        for sent in doc.sents:
            entity = None
            amount = None
            
            # Extract entity name based on the specific pattern
            entity_match = self.entity_pattern.search(sent.text)
            if entity_match:
                entity = entity_match.group(1).strip()
            
            # Extract the amount from the sentence using the regular expression pattern
            match = self.amount_pattern.search(sent.text)
            if match:
                amount = match.group()
            
            # If both entity and amount are found, add them to the result list
            if entity and amount:
                entities_and_amounts.append((entity, amount))
        
        # Convert the results to a pandas DataFrame
        df = pd.DataFrame(entities_and_amounts, columns=["Entity", "Amount"])
        
        return df