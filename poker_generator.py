#!/usr/bin/env python
faces = [face for face in '23456789TJQKA']
suits = [suit for suit in 'SCDH']  
all_cards = [face + suit for face in faces for suit in suits]
for i1, c1 in enumerate(all_cards): 
    for i2, c2 in enumerate(all_cards[i1+1:]):
        for i3, c3 in enumerate(all_cards[i1+i2+2:]): 
            for i4, c4 in enumerate(all_cards[i1+i2+i3+3:]): 
                for c5 in all_cards[i1+i2+i3+i4+4:]: 
                    hand = ('%s,%s,%s,%s,%s' % (c1, c2, c3, c4, c5))
