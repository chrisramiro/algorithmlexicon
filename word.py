import bs4
import numpy
import requests
from sense import *
numpy.seterr(all='raise')

class Word:
    """A word, as it exists in the HTE, and all of its corresponding senses."""

    def __init__(self, word, part_of_speech="all"):
        self.label = word
        self.PoS = part_of_speech
        self.senses = self.make_sense_list(word, part_of_speech)
        self.length = len(self.senses)
        self.viable = True
        if len(self.senses) <= 1:
            self.bl_senses = self.senses
            self.nb_senses = []
            self.start_date = self.senses[0].date
        else:
            index = 0
            while True:
                if index >= self.length:
                    break
                if self.senses[index].date != self.senses[index+1].date:
                    break
                index += 1
            self.bl_senses = self.senses[:index+1:]
            self.nb_senses = self.senses[index+1::]

        if self.nb_senses:
            self.num_nb_senses = len(self.nb_senses)
            self.num_bl_senses = self.length - self.num_nb_senses
            self.num_senses = self.num_nb_senses + self.num_bl_senses
            self.num_exist_senses = len([s for s in self.senses if s.end_date == 3000])
            self.nb_dates = [nb_sense.date for nb_sense in self.nb_senses]

    def __repr__(self):
        return self.label

    def __str__(self):
        return self.label
