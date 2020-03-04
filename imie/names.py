#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def losowe_imie():
    global name
    name = random.choice(list(open('lista.txt')))
    print(f'Losowo wygenerwane imię to: {name}')



while True:
    losowe_imie()
    program_end = input('Wybrać kolejne imię? (Tak/Nie): ')

    if not (program_end == 'Tak' or program_end == 'tak'):
        print(f'Wybraliście imię {name} zapraszam do kancelarii.')
        break
