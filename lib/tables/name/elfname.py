"""

pet.py

"""

from .. import meta

class ElfName(meta.Table):

    def lookup(self):
        # Generate the first name based on gender
        if self._ctx['gender'] == 'female':
            fname = self.get_female_name()
        else:
            fname = self.get_male_name()

        # Generate a surname
        lname = self.get_surname()

        # Set the new context and return the formated name
        self._ctx['name'] = '{} {}'.format(fname, lname)
        return '{name}'.format(**self._ctx)


    def get_male_name(self):
        table = meta.WeightedTable([
            { "w":1, "v":"Annaeleth"},
            { "w":1, "v":"Caresta"},
            { "w":1, "v":"Celenwe"},
            { "w":1, "v":"Celorfin"},
            { "w":1, "v":"Cirdaere"},
            { "w":1, "v":"Cirdire"},
            { "w":1, "v":"Cirdore"},
            { "w":1, "v":"Danore"},
            { "w":1, "v":"Delemmak"},
            { "w":1, "v":"Dirinor"},
            { "w":1, "v":"Dorophil"},
            { "w":1, "v":"Eahtadan"},
            { "w":1, "v":"Egoron"},
            { "w":1, "v":"Egos"},
            { "w":1, "v":"Elegnos"},
            { "w":1, "v":"Elel"},
            { "w":1, "v":"Elered"},
            { "w":1, "v":"Ellas"},
            { "w":1, "v":"Elromior"},
            { "w":1, "v":"Elurir"},
            { "w":1, "v":"Endinwel"},
            { "w":1, "v":"Enengod"},
            { "w":1, "v":"Enereg"},
            { "w":1, "v":"Erelmil"},
            { "w":1, "v":"Erodh"},
            { "w":1, "v":"Finaeli"},
            { "w":1, "v":"Finare"},
            { "w":1, "v":"Finasaer"},
            { "w":1, "v":"Findire"},
            { "w":1, "v":"Finerdhil"},
            { "w":1, "v":"Finethil"},
            { "w":1, "v":"Galadher"},
            { "w":1, "v":"Galebre"},
            { "w":1, "v":"Galegal"},
            { "w":1, "v":"Galure"},
            { "w":1, "v":"Golemmoth"},
            { "w":1, "v":"Golineth"},
            { "w":1, "v":"Gonethin"},
            { "w":1, "v":"Hilore"},
            { "w":1, "v":"Ingon"},
            { "w":1, "v":"Ladore"},
            { "w":1, "v":"Lemmaegli"},
            { "w":1, "v":"Lionerdhon"},
            { "w":1, "v":"Mironwe"},
            { "w":1, "v":"Olond"},
            { "w":1, "v":"Ophin"},
            { "w":1, "v":"Oron"},
            { "w":1, "v":"Penlador"},
            { "w":1, "v":"Thilenwe"}
        ])
        return table.choice()


    def get_female_name(self):
        table = meta.WeightedTable([
            { "w":1, "v":"Adriel"},
            { "w":1, "v":"Alotel"},
            { "w":1, "v":"Aloth"},
            { "w":1, "v":"Altalas"},
            { "w":1, "v":"Alwel"},
            { "w":1, "v":"Amas"},
            { "w":1, "v":"Anelyen"},
            { "w":1, "v":"Anen"},
            { "w":1, "v":"Aninyel"},
            { "w":1, "v":"Anithren"},
            { "w":1, "v":"Aredhel"},
            { "w":1, "v":"Arelel"},
            { "w":1, "v":"Arelen"},
            { "w":1, "v":"Arwel"},
            { "w":1, "v":"Atiel"},
            { "w":1, "v":"Celaser"},
            { "w":1, "v":"Earwenen"},
            { "w":1, "v":"Ellaloth"},
            { "w":1, "v":"Elwindith"},
            { "w":1, "v":"Elyel"},
            { "w":1, "v":"Enwenen"},
            { "w":1, "v":"Eris"},
            { "w":1, "v":"Erwel"},
            { "w":1, "v":"Finde"},
            { "w":1, "v":"Findelye"},
            { "w":1, "v":"Finduilye"},
            { "w":1, "v":"Galaser"},
            { "w":1, "v":"Gilme"},
            { "w":1, "v":"Gilmirie"},
            { "w":1, "v":"Idrinden"},
            { "w":1, "v":"Ilmindel"},
            { "w":1, "v":"Iming"},
            { "w":1, "v":"Imithren"},
            { "w":1, "v":"Imrodel"},
            { "w":1, "v":"Inding"},
            { "w":1, "v":"Inyelyen"},
            { "w":1, "v":"Iririen"},
            { "w":1, "v":"Ladrilye"},
            { "w":1, "v":"Laserie"},
            { "w":1, "v":"Minimrie"},
            { "w":1, "v":"Neladrie"},
            { "w":1, "v":"Nelalwe"},
            { "w":1, "v":"Nelaser"},
            { "w":1, "v":"Nerduilye"},
            { "w":1, "v":"Nimlalwe"},
            { "w":1, "v":"Nimlenwe"},
            { "w":1, "v":"Serilye"},
            { "w":1, "v":"Serode"},
            { "w":1, "v":"Tanye"},
            { "w":1, "v":"Tarielye"}
        ])
        return table.choice()


    def get_surname(self):
        table = meta.WeightedTable([
            { "w":1, "v":"Aeraagamae"},
            { "w":1, "v":"Aerabriniel"},
            { "w":1, "v":"Aldarina"},
            { "w":1, "v":"Aldaviel"},
            { "w":1, "v":"Bertanonel"},
            { "w":1, "v":"Birdiir"},
            { "w":1, "v":"Birlond"},
            { "w":1, "v":"Cromelon"},
            { "w":1, "v":"Cromviel"},
            { "w":1, "v":"Dlaralthor"},
            { "w":1, "v":"Dlarraithar"},
            { "w":1, "v":"Elendiir"},
            { "w":1, "v":"Eleneth"},
            { "w":1, "v":"Elervir"},
            { "w":1, "v":"Falavaul"},
            { "w":1, "v":"Gadilinion"},
            { "w":1, "v":"Galamin"},
            { "w":1, "v":"Galarina"},
            { "w":1, "v":"Galathaniel"},
            { "w":1, "v":"Garaitinu"},
            { "w":1, "v":"Gwamiel"},
            { "w":1, "v":"Haelond"},
            { "w":1, "v":"Isilielenion"},
            { "w":1, "v":"Kevadirtinu"},
            { "w":1, "v":"Kithollal"},
            { "w":1, "v":"Lantaththar"},
            { "w":1, "v":"Laranonel"},
            { "w":1, "v":"Larentansel"},
            { "w":1, "v":"Lithtaur"},
            { "w":1, "v":"Maerethar"},
            { "w":1, "v":"Maltanthir"},
            { "w":1, "v":"Mithanmae"},
            { "w":1, "v":"Mithanmyr"},
            { "w":1, "v":"Mithmirelen"},
            { "w":1, "v":"Nalllithe"},
            { "w":1, "v":"Nellynnthar"},
            { "w":1, "v":"Nhaendrin"},
            { "w":1, "v":"Noroelwa"},
            { "w":1, "v":"Orren"},
            { "w":1, "v":"Orrina"},
            { "w":1, "v":"Rhuivaul"},
            { "w":1, "v":"Runelenrin"},
            { "w":1, "v":"Runlithmae"},
            { "w":1, "v":"Sharondalan"},
            { "w":1, "v":"Taldilindar"},
            { "w":1, "v":"Talraidal"},
            { "w":1, "v":"Talthanryl"},
            { "w":1, "v":"Tathviel"},
            { "w":1, "v":"Wervanion"},
            { "w":1, "v":"Yraudhen"}
        ])
        return table.choice()

if __name__ == '__main__':
    from random import choice
    print(ElfName({'gender': choice(['male', 'female'])}).lookup())