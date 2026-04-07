'''
Name -> "PinSight"
Description -> A tool for visualizing and analyzing bowling data
File Description -> Database access and management functions for PinSight application
Start Date -> April 6th 2026 (4/6/2026)
Lead Developer -> Chris Herriman Jr
Other Developers -> N/A
'''
import sqlite3 as sqlite                # SQLite database access
from utils import helpers as help       # Helper functions for data processing

DB_PATH = help.resource_path("data/PinSight.db") # Path to the SQLite database file, using helper function to get correct path in both dev and PyInstaller environments

# Database connection helper function
def get_connection():
    conn = sqlite.connect(DB_PATH) # Connect to the SQLite database at the specified path
    conn.execute("PRAGMA foreign_keys = ON;") # Enable foreign key support for SQLite
    return conn # Return the database connection object for use in other functions

# Function to retrieve all bowlers from the database, ordered by last name and first name
def get_all_bowlers():
    conn = get_connection() # Get a database connection
    cursor = conn.cursor() # Create a cursor object to execute SQL queries
    cursor.execute("""SELECT bowler_id, first_name, last_name, nickname, dominant_hand, notes
                   FROM BOWLERS
                   ORDER BY last_name, first_name""") # Execute SQL query to retrieve all bowlers ordered by last name and first name
    rows = cursor.fetchall() # Fetch all results from the executed query
    conn.close() # Close the database connection
    return rows # Return the list of bowlers as tuples (bowler_id, first_name

#, last_name, nickname, dominant_hand, notes)
def get_bowler_by_id(bowler_id):
    conn = get_connection() # Get a database connection
    cursor = conn.cursor() # Create a cursor object to execute SQL queries
    cursor.execute("""SELECT bowler_id, first_name, last_name, nickname, dominant_hand, notes
                   FROM BOWLERS
                   WHERE bowler_id = ?""", (bowler_id,)) # Execute SQL query to retrieve a specific bowler by their unique ID
    row = cursor.fetchone() # Fetch the single result from the executed query
    conn.close() # Close the database connection
    return row # Return the bowler data as a tuple (bowler_id, first_name, last_name, nickname, dominant_hand)

# Function to add a new bowler to the database
def add_bowler(first_name, last_name, nickname=None, dominant_hand=None, notes=None):
    conn = get_connection() # Get a database connection
    cursor = conn.cursor() # Create a cursor object to execute SQL queries
    cursor.execute(
        """INSERT INTO Bowlers (first_name, last_name, nickname, dominant_hand, notes)
        VALUES (?, ?, ?, ?, ?)""",
        (first_name, last_name, nickname, dominant_hand, notes)
    )
    conn.commit() # Commit the transaction to save changes to the database
    conn.close()  # Close the database connection

# Function to update an existing bowler's information in the database
def update_bowler(bowler_id, first_name, last_name, nickname=None, dominant_hand=None, notes=None):
    conn = get_connection() # Get a database connection
    cursor = conn.cursor() # Create a cursor object to execute SQL queries
    cursor.execute("""UPDATE Bowlers
                   SET first_name = ?, last_name = ?, nickname = ?, dominant_hand = ?, notes = ?
                   WHERE bowler_id = ?""", (first_name, last_name, nickname, dominant_hand, notes, bowler_id)) # Execute SQL query to update the specified bowler's information in the database based on their unique ID
    conn.commit() # Commit the transaction to save changes to the database
    conn.close() # Close the database connection