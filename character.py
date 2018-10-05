class Character(object):

    def __init__(self, name, gender, race, house):
        self.name = name
        self.gender = gender
        self.race = race
        self.house = house

    def _set_gender_(self):
        print('\nGreat, ' + self.name + ', what a fantastic name!\n')

        gender_is_invalid = True
        while gender_is_invalid:
            self.gender = input('Are you a MAN or a WOMAN?\n')

            if self.gender.lower() == 'man' or self.gender.lower() == 'woman':
                gender_is_invalid = False
            else:
                print('\nI know this can be hard, but try again.\n')
        return self.gender

    def _set_race_(self):
        race_is_invalid = True
        while race_is_invalid:
            self.race = input('\nAre you a HUMAN, ELF, or DWARF?\n')

            if self.race.lower() == 'human' or self.race.lower() == 'elf' or self.race.lower() == 'dwarf':
                race_is_invalid = False
            else:
                print('\nFunny, those are not one of the known races.  Give it another go.\n')
        return self.race

    def _set_house_(self):
        house_is_invalid = True
        while house_is_invalid:
            self.house = input('\nWhich House are you from?  STARK, TARGARYEN, or LANNISTER? \n')

            if self.house.lower() == 'stark' or self.race.lower() == 'targaryen' or self.race.lower() == 'lannister':
                house_is_invalid = False
            else:
                print('\nI know of no such house, pick one of the existing houses.\n')

        return self.house

    def _announce_new_player_(self):
        announcement = '\nYou shall hence be know as ' + self.name.capitalize() + ' the ' + self.race.lower()\
                       + ' from House ' + self.house.capitalize() + '!'
        return print(announcement)