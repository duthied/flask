# movies.py

from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

MOVIES = {
  "The Shawshank Redemption": {
    "name": "The Shawshank Redemption",
    "cast": ["Tim Robbins", "Morgan Freeman", "Bob Gunton"],
    "genres": ["Drama"],
    "timestamp": get_timestamp(),
  },
  "The Godfather": {
  "name": "The Godfather",
  "cast": ["Marlon Brando", "Al Pacino", "James Caan"],
  "genres": ["Crime", "Drama"],
  "timestamp": get_timestamp(),
  },
  "The Dark Knight": {
    "name": "The Dark Knight",
    "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
    "genres": ["Action", "Crime", "Drama"],
    "timestamp": get_timestamp(),
  },
  "Pulp Fiction": {
    "name": "Pulp Fiction",
    "cast": ["John Travolta", "Samuel L. Jackson", "Uma Thurman"],
    "genres": ["Crime", "Drama"],
    "timestamp": get_timestamp(),
  },
  "The Return of the King": {
    "name": "The Lord of the Rings: The Return of the King",
    "cast": ["Elijah Wood", "Viggo Mortensen", "Ian McKellen"],
    "genres": ["Adventure", "Drama", "Fantasy"],
    "timestamp": get_timestamp(),
  }
}

def read_all():
  return list(MOVIES.values())
