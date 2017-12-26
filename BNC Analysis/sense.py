class Sense:

    def __init__(self, word, date, word_form, identifiers, categories, PoS):
        self.word = word
        self.date = self.date_normalizer(date)
        self.end_date = self.end_date_normalizer(date)
        self.word_form = word_form
        self.identifiers = identifiers
        self.categories = categories
        self.listed_cat = self.categorizer(self.categories)
        self.PoS = PoS

    def date_normalizer(self, date):
        """Takes a date, which may range in form from (OE-3271) or
    	(c1234 - 3210) or (a2574) or (1257) etc., and returns it
    	as a form 1234 as an starting date as an integer"""
        # retrieve the date as a string
        date = str(date)
        date = date[2::]  # Remove the initial "("
        if date[0] == "O":
            return "OE"
        dash_index = date.find("–") #only starting dates should be used
        if dash_index == -1:
            return False
        if date[0].isalpha():
            date = date[1::]
        return int(date[:4:]) #dates less than 4 digits are displayed as "OE"

    def end_date_normalizer(self, date):
        """Takes a date, which may range in form from (OE-3271) or
            (c1234 - 3210) or (a2574) or (1257) etc., and returns it
            as a form "3210" as an ending date as an integer or
            False if there is no such date"""
        date = str(date)
        end_date = 0
        if ("–" in date):
            index = date.index("–") + 1
            if date[index].isdigit() or date[index].isalpha():
                if not date[index].isdigit():                           #accounts for (1234-a1235)
                    index += 1
                while(date[index].isdigit()):
                    end_date = (end_date * 10) + int(date[index])
                    index += 1
                return end_date
            else:
                return 3000
        else:
            return False

    def categorizer(self, category):
        """Takes a category of form "01.02.03.04.05 n" and returns a
        list of lists of form ['01', '02', '03', '04', '05']
        This implementation ignores secondary meanings, which occur after
        a pipe (i.e. 01.02.03 | 04.05 n where 04.05 n is ignored)"""
        listed_cat, i = [], 0
        while(True):
            curr = ""
            while category[i].isdigit():
                curr += category[i]
                i += 1
            listed_cat.append(curr)
            if category[i+1].isalpha():
                break
            i += 1
        return listed_cat

    def __str__(self):
        return str(self.date)
