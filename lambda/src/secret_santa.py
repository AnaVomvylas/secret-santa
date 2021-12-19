import random
import boto3
import src.handler.event as event_handler
import src.handler.lambda_response as lambda_response


def execute_secret_santa(senders: list) -> dict:
    remaining_receivers = senders.copy()
    pairs = {}

    for sender in senders:
        if remaining_receivers == [sender]:
            return {}
        receiver = get_random_receiver(sender, remaining_receivers)
        remaining_receivers.remove(receiver)
        pairs[sender.name] = receiver.name
    return pairs


def get_random_receiver(sender: str, receivers: list) -> str:
    receivers_excluding_sender = list.copy(receivers)
    if sender in receivers_excluding_sender:
        receivers_excluding_sender.remove(sender)
    return random.choice(receivers_excluding_sender)


def lambda_handler(event, context):
    participants = event_handler.get_participants_from_event(event)
    pairs = {}

    if len(participants) <= 1:
        return lambda_response.bad_request("Participant count must be at least 2")

    while len(pairs) == 0:
        pairs = execute_secret_santa(participants)
    return lambda_response.ok(pairs)
