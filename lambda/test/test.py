import unittest
import src.secret_santa
from src.model.participant import Participant
from src.handler import event as event_handler

participant_a = Participant(name="a", email="a@a.com")
participant_b = Participant(name="b", email="b@b.com")


class SecretSantaTest(unittest.TestCase):
    def test_get_participants_from_event(self):
        event = {"participants": [participant_a]}
        participants = event_handler.get_participants_from_event(event)
        expected = [participant_a]
        self.assertListEqual(participants, expected)

    # Should not return sender as receiver
    def test_get_random_receiver(self):
        sender = participant_a
        receivers = [participant_a, participant_b]
        receiver = src.secret_santa.get_random_receiver(sender, receivers)
        self.assertNotEqual(receiver, sender)

    def test_execute_secret_santa(self):
        participants = [participant_a, participant_b]
        pairs = src.secret_santa.execute_secret_santa(participants)
        expected_pairs = {
            participant_a.name: participant_b.name,
            participant_b.name: participant_a.name,
        }
        self.assertEqual(pairs, expected_pairs)

    # Should return empty pair with only 1 participant
    def test_execute_secret_santa_2(self):
        participants = [participant_a]
        pairs = src.secret_santa.execute_secret_santa(participants)
        self.assertEqual(pairs, {})

    # def test_lambda_handler(self):
    #     event = {"participants": [participant_a, participant_b]}
    #     response = src.secret_santa.lambda_handler(event, None)
    #     self.assertEqual(response["statusCode"], 200)

    # def test_lambda_handler_2(self):
    #     event = {"participants": [participant_a]}
    #     response = src.secret_santa.lambda_handler(event, None)
    #     self.assertEqual(response["statusCode"], 400)

