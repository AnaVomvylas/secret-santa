import unittest
import src.secret_santa

class SecretSantaTest(unittest.TestCase):

    def test_get_random_receiver(self):
        sender = 'me'
        receivers = ['me','someone_else']
        receiver = src.secret_santa.get_random_receiver(sender,receivers)
        self.assertEqual(receiver, 'someone_else')

    def test_execute_secret_santa(self):
        emails = ['a@a.com','b@b.com']
        pairs = src.secret_santa.execute_secret_santa(emails)
        expected_pairs= {'a@a.com': 'b@b.com', 'b@b.com': 'a@a.com'}
        self.assertEqual(pairs, expected_pairs)
    
    def test_execute_secret_santa_2(self):
        emails = ['a@a.com']
        pairs = src.secret_santa.execute_secret_santa(emails)
        self.assertEqual(pairs, {})