import unittest
from config_provider import ConfigProvider
from error_handling import ErrorHandling
import file_handler


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # ARRANGE
        self.config = ConfigProvider.load_from_file("config.json")

    def test_write_file(self):
        # ACT
        ErrorHandling.write_file(self.config["file_path"], self.config["content"])
        # ASSERT
        self.assertTrue(f"{self.config["file_path"]}")

    def test_content_of_writing_file(self):
        # ACT
        with open("check_path", "r") as file:
            check = file.read()
        # ASSERT
        self.assertEqual(check, self.config["content"])

    def test_read_file(self):
        # ACT
        ErrorHandling.read_file(self.config["file_path_for_read"])
        # ASSERT
        self.assertEqual(ErrorHandling.read_file(self.config["file_path_for_read"]),
                         self.config["file_path_for_read_content"])


if __name__ == '__main__':
    unittest.main()
