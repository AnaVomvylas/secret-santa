import random

emails = ['1','2','3']

def execute_secret_santa(senders: list) -> dict:
    remaining_receivers = senders.copy()
    pairs = {}

    for sender in senders:
        if remaining_receivers == [sender]:
            return {}
        receiver = get_random_receiver(sender,remaining_receivers)
        remaining_receivers.remove(receiver)
        pairs[sender] = receiver
    return pairs

def get_random_receiver(sender:str ,receivers:list) -> str:
    receivers_excluding_sender = list.copy(receivers)
    if sender in receivers_excluding_sender:
        receivers_excluding_sender.remove(sender)
    return random.choice(receivers_excluding_sender)


if __name__ == "__main__":
    pairs = {}
    while len(pairs) == 0:
        pairs = execute_secret_santa()
    
    