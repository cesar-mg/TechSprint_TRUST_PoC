import sqlite3
import re
from typing import Optional, Tuple
import sys
import os
from document_analysis_module_nlp.nlp_entity_extraction import TextDataExtractor

class DataExtractor:
    def __init__(self, db_name: str = 'extracted_data.db'):
        """
        Initializes the DataExtractor class with a connection to the SQLite database.

        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """
        Creates the extracted_info table in the database if it doesn't already exist.
        """
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS extracted_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount TEXT,
            person TEXT
        )
        ''')
        self.conn.commit()

    def insert_data(self, amount: Optional[str], person: Optional[str]):
        """
        Inserts the extracted data into the database.

        :param amount: The extracted amount as a string.
        :param person: The extracted person's name.
        """
        if amount and person:
            self.cursor.execute('''
            INSERT INTO extracted_info (amount, person)
            VALUES (?, ?)
            ''', (amount, person))
            self.conn.commit()

    def fetch_all_data(self) -> list:
        """
        Fetches all the data from the database.

        :return: A list of tuples containing the data from the extracted_info table.
        """
        self.cursor.execute('SELECT * FROM extracted_info')
        return self.cursor.fetchall()

    def close_connection(self):
        """
        Closes the connection to the SQLite database.
        """
        self.conn.close()
