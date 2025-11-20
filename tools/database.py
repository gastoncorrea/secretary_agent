import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional
import logging

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

class DatabaseManager:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.database = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.connection = None
        self.logger = logging.getLogger(__name__)
        
    def connect(self):
        """Establish a database connection."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password,
                charset=os.getenv("DB_CHARSET", "utf8mb4")
            )
            if self.connection.is_connected():
                self.logger.info("Successfully connected to the database")
                return True
        except Error as e:
            self.logger.error(f"Error connecting to database: {e}")
            return False
        
    def query(self, sql, params=None):
        """Run SELECT queries"""
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(sql, params)
        return cursor.fetchall()

    def execute(self, sql, params=None):
        """Run INSERT/UPDATE/DELETE"""
        cursor = self.connection.cursor()
        cursor.execute(sql, params)
        self.connection.commit()
        return cursor.lastrowid
        
    def disconnect(self):
            """Close the database connection."""
            if self.connection and self.connection.is_connected():
                self.connection.close()
                self.logger.info("Database connection closed")
     