import unittest
from src.YD import upload, file_path, token


class TestFolderCreate(unittest.TestCase):
    def test_folder_create(self):
        self.assertEqual(upload(file_path, token), 201)

    def test_folder_create_error(self):
        self.assertEqual(upload(file_path, token), 409)

    @unittest.expectedFailure
    def test_folder_create_error_1(self):
        self.assertEqual(upload(file_path, token), 400)

    @unittest.expectedFailure
    def test_folder_create_error_2(self):
        self.assertEqual(upload(file_path, token), 401)
