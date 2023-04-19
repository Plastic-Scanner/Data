# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:08:40 2020

@author: Patrick
"""

import matplotlib.ticker as mticker
'''
(c) 2018, D.D.Land <d.d.land@hhs.nl>
Module om figuren weer te geven zoals aangegeven in het Rapportage document
van de afdeling Technische Natuurkunde van de Haagse Hogeschool.
versie: 1.1
20180317: herschreven naar class structuur om meerdere (sub)figuren hun eigen
aantal digits op de assen te kunnen geven.
'''


class TNFormatter(mticker.Formatter):
    ''' Class om een vast aantal significante getallen weer te geven in de
        assen van een figuur.
    Class wordt aangeroepen vanuit de axis formatter van een matplotlibfiguur.
    '''

    def __init__(self, length=3):
        ''' argumenten:
                lengte: Geeft aan hoeveel significante getallen weergegeven
                        moeten worden.
        '''
        self.length = length

    def __call__(self, x, pos=None):
        ''' Functie die vanuit matplotlib aangeroepen wordt als een figuur
            gemaakt (of bekeken) wordt.
        Herschrijft de getallen op de assen naar getallen met een vast aantal
        digits.
        '''
        s = '%.10e' % x
        tup = s.split('e')
        signif = tup[0].rstrip('.')
        neg = ''
        if signif[0] == '-':
            neg = '-'
            signif = signif[1:]
        sign = tup[1][0].replace('+', '')  # verwijder +
        expo = tup[1][1:].lstrip('0')
        if expo:  # getal groter dan 10
            if self.length <= abs(int(expo)):  # schrijf als 10 macht
                expon = '10^{%s%s}' % (sign, expo)
                if self.length == 1:  # allen getal voor de . houden...
                    splt = signif.split('.')
                    signif = splt[0]
                else:  # meer dan 1 cijfer significant
                    signif = signif[:self.length+1]
                    if len(signif) < self.length+1:
                        signif += '0' * (self.length + 1 - len(signif))
                s = r'%s%s{\cdot}%s' % (neg, signif, expon)
            else:  # schrijf als getal
                s = '%.10f' % x
                extra0 = 0
                if s[0] == '-':
                    s = s[1:]
                if s[0] == '0':  # kleiner dan 1
                    splt = s.split('.')
                    zeros = splt[1].lstrip('0')
                    num = len(splt[1]) - len(zeros)
                    s = r'%s%s%s' % (neg, s[:self.length+2], '0'*num)
                else:
                    s = r'%s%s' % (neg, s[:self.length+1])
        else:  # exponent is 0
            if len(signif) >= self.length:
                if self.length == 1:
                    s = r'%s%s' % (neg, signif[:self.length])
                else:
                    s = r'%s%s' % (neg, signif[:self.length+1])
            else:
                s = r'%s%s%s' % (neg, signif, '0'*(self.length-len(signif)))
        if s[-1] == '.':  # laatste teken een ., mag dus weg.
            s = s[:-1]
        # vervang punten door komma's. Extra witruimte rond komma met {} uit string weggehaald.
        return "${}$".format(s.replace('.', '.'))

    def legenda(self, x, pos=None):
        return self.__call__(x, pos)

def label_x(grootheid, eenheid, ax, haak='[]', text=''):
    ''' Zet label van de as op een (relatief) makkelijke manier. '''
    ax.xaxis.set_label_text('%s $\,%s \, %s\mathrm{%s}%s$' % (text,
                            grootheid, haak[0], eenheid, haak[1]))


def label_y(grootheid, eenheid, ax, haak='[]', text=''):
    ''' Zet label van de as op een (relatief) makkelijke manier. '''
    ax.yaxis.set_label_text('%s $\,%s \, %s\mathrm{%s}%s$' % (text,
                            grootheid, haak[0], eenheid, haak[1]))

# nodig voor backwards compatibility
PRECISION_X = 2
PRECISION_Y = 2


def fix_axis(ax):
    ''' Functie die de nieuwe Class implementatie beschikbaar houdt
        voor de oude functie definities.
    '''
    ax.yaxis.set_major_formatter(TNFormatter(length=PRECISION_Y))
    ax.xaxis.set_major_formatter(TNFormatter(length=PRECISION_X))