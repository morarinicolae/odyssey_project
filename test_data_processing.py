import unittest
from data_processing import extract_movie_type, extract_duration_period, extract_name, extract_genre

class TestMovieDataExtraction(unittest.TestCase):

    def test_extract_movie_type(self):
        """Function for testing the extract_movie_type function"""
        # Test for extracting movie type from different entries
        entry_1 = "Movie Type: Action"
        self.assertEqual(extract_movie_type(entry_1), "Action")

        entry_2 = "Type: Comedy"
        self.assertEqual(extract_movie_type(entry_2), "Comedy")

        entry_3 = "Type: Drama"
        self.assertEqual(extract_movie_type(entry_3), "Drama")

    def test_extract_duration_period(self):
        """Function for testing the extract_duration_period function"""
        # Test for extracting duration period from different entries
        entry_1 = "Duration: 120 minutes"
        self.assertEqual(extract_duration_period(entry_1), (120, "minutes"))

        entry_2 = "Duration: 90 min"
        self.assertEqual(extract_duration_period(entry_2), (90, "min"))

    def test_extract_name(self):
        """Function for testing the extract_name function"""
        # Test for extracting movie name from different entries
        entry_1 = "Movie Name: The Avengers"
        self.assertEqual(extract_name(entry_1), "The Avengers")

        entry_2 = "Title: Titanic"
        self.assertEqual(extract_name(entry_2), "Titanic")

    def test_extract_genre(self):
        """Function for testing the extract_genre function"""
        # Test for extracting movie genre from different entries
        entry_1 = "Genre: Action, Adventure"
        self.assertEqual(extract_genre(entry_1), "Action, Adventure")

        entry_2 = "Category: Comedy"
        self.assertEqual(extract_genre(entry_2), "Comedy")

if __name__ == '__main__':
    unittest.main()
