import unittest
import os
import rafi

class TestSimpleRandomFiles(unittest.TestCase):
    def setUp(self):
        # Remove any existing test files before running the tests
        for file in os.listdir():
            if file.startswith("testfile"):
                os.remove(file)

    def test_file_creation(self):
        # Run the script
        simple_random_files.main()
        
        # Check that 5 files were created
        files = [f for f in os.listdir() if f.startswith("testfile")]
        self.assertEqual(len(files), 5)
        
        # Check that each file has the correct extension
        for file in files:
            extension = file.split(".")[-1]
            self.assertIn(extension, simple_random_files.extensions)
            
        # Check that each file has a size of 1024 bytes
        for file in files:
            self.assertEqual(os.path.getsize(file), 1024)
    
    def tearDown(self):
        # Remove any test files after running the tests
        for file in os.listdir():
            if file.startswith("testfile"):
                os.remove(file)

if __name__ == '__main__':
    unittest.main()
