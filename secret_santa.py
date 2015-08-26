import argparse
from random import shuffle
from sender import Sender

parser = argparse.ArgumentParser(
    description="Create a series of matches from a list of people."
)
parser.add_argument(
    'server', metavar='server',
    help="""SMTP server address and port to use to send matches
    (ex: smtp.gmail.com:587)"""
)
parser.add_argument(
    'email', metavar='e-mail address',
    help='the e-mail address to send matches from'
)
parser.add_argument(
    'password', metavar='password',
    help='the password for the email-address specified'
)
parser.parse_args()
args = parser.parse_args()


def shuffle_and_verify(seq):
    """Shuffle a list and verify that it is not the same."""
    old_seq = list(seq)
    while seq == old_seq:
        shuffle(seq)
    return seq

with open('participants.txt') as f:
    participants = [
        tuple(line.strip().split('|')) for line in f.readlines()
        if line != '\n'
    ]

shuffle_and_verify(participants)

client = Sender(args.server, args.email, args.password)
client.login()

f = open('matches.txt', 'w')

for i in range(len(participants)):
    giver = participants[i]
    getter = participants[(i + 1) % len(participants)]
    f.write(giver[0] + ' --> ' + getter[0] + '\n')
    client.send(
        giver[1], 'Secret Santa',
        'Your match is: %s' % getter[0]
    )

f.close()
client.logout()
