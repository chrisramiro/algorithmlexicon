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

    def make_sense_list(self, label, part_of_speech):
        """Takes a word and searches for it within the HTE database,
        returning a list with the same information in a sense
        object with, ordered a date, word_form, identifiers, and
        categories"""

        if part_of_speech == "a":
            part_of_speech = "aj"
        if part_of_speech == "adv":
            part_of_speech = "av"

        if part_of_speech == "v":
            url = "http://historicalthesaurus.arts.gla.ac.uk/category-selection/?word=" + label + "&pos%5B%5D=allv&pos%5B%5D=v&pos%5B%5D=vi&pos%5B%5D=vm&pos%5B%5D=vp&pos%5B%5D=vr&pos%5B%5D=vt&label=&category=&startf=&endf=&startl=&endl="
        elif part_of_speech == "all":
            url = "http://historicalthesaurus.arts.gla.ac.uk/category-selection/?word=" + label + "&label=&category=&startf=&endf=&startl=&endl="
        else:
            url = "http://historicalthesaurus.arts.gla.ac.uk/category-selection/?word=" + label + "&pos%5B%5D=" + part_of_speech + "&label=&category=&startf=&endf=&startl=&endl="

        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.content, "html.parser")
        for a in soup.find_all("a"):
            del a['href']

        catOdds, catEvens = soup.find_all("p", "catOdd"), soup.find_all("p", "catEven")
        allCat = catOdds + catEvens

        sense_list = []

        for index in range(0, len(allCat)):
            indexed_sense = Sense(label, allCat, index)
            # Skip past the current selection if the date is not a starting date
            if not indexed_sense.date:
                continue
            sense_list.append(indexed_sense)

        # this separation is done so that we can sort the list with OE at the beginning instead of the end
        OE_list = [sense for sense in sense_list if sense.date == "OE"]
        non_OE_list = [sense for sense in sense_list if sense.date != "OE"]
        sense_list = OE_list + sorted(non_OE_list, key=lambda x: x.date)

        return sense_list

    def __repr__(self):
        return self.label

    def __str__(self):
        return self.label
