import character
import random

print('\nWelcome to Deity, this is where your epic journey will begin.\n\nBut first, I require some information from '
      'you...')


new_player = character.Character('', '', '', '')

new_player.name = input('\nWhat do you call yourself?\n')

new_player._set_gender_()

print('\nPerfect!\n')

new_player._set_race_()

print('\nWhat a lovely thing to be in this day and age!\n')

new_player._set_house_()

new_player._announce_new_player_()

print('\n\nIt is now up to the Gods of Old to decide your fate...\n\n' + new_player.name.capitalize() +
      ' the Gods have decided.\n\n')

print('Strength: ' + str(random.randint(1, 21)) +
      '\nIntelligence: ' + str(random.randint(1, 21)) +
      '\nDexterity: ' + str(random.randint(1, 21)) +
      '\nCharisma: ' + str(random.randint(1, 21)) +
      '\nWisdom: ' + str(random.randint(1, 21)) +
      '\nConstitution: ' + str(random.randint(1, 21))
)
