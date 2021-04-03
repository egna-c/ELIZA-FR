#!/usr/bin/env python3
from eliza import Eliza

eliza = Eliza()
eliza.load('doctor-fr.txt')

print(eliza.initial())
while True:
    said = input('> ')
    response = eliza.respond(said)
    if response is None:
        break
    print(response)
print(eliza.final())
