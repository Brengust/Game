from module1 import graphics

def introduction(game):
    print('''The year is 1923. The world was thrown into disarray after the assassination of \n
    Archduke Ferdinand in 1914. The nations of the world saw this as an opportunity to show\n
    the recent technological innovations of war, and make known their dominance. But, as with\n
    the creation of tools of destruction comes the naiveté of man. So prone is man to the\n
    belief that one can safely harness a destructive power against another, with little fear of the\n
    repercussions. The Miasma Expansion of 1915 marked the fall of humanity, a testament to the\n
    foolishness of man. Yet, still some cling to life, and even still whispers of hope can become\n
    heard through the streets. Even without king or country, humans still find the need to\n
    survive.''')

    game.difficulty = rules()
    print(game.difficulty)
    game.player1.faction= faction_selection()
    game.player2.faction= faction_selection()

def rules():
    player_status = input('Is this your first time playing? If so, enter "RULES". If not enter "PLAY".\n')
    if player_status == 'RULES':
        rule_page = ''
        rule_book = {'1': '',
         '2': 'a',
          '3': 'a',
           '4': 'a',
            '5': 'a',
             '6': 'a',
              '7': 'a',
               '8': 'a'}
        while rule_book != 'PLAY':
            print('''Pages: (1) Nation Management, (2) Diplomacy, (3) Military, (4) Combat, (5) Events, (6) Miasma,
            (7) Terrain, (8) Victory Conditions. Enter 'PLAY' when done with rules.''')
            rule_page = input('Enter page number:')
            for rule_page in rule_book:
                print(rule_book(rule_page))

    if player_status == 'PLAY':
        print("Difficulty will affect certain aspects of gameplay, from starting resources to opponent's strength.")
        difficulty = input('ENTER DIFFICULTY: (hard/medium/easy)\n')
        return difficulty

def faction_selection():
    print('''An era of turmoil has gripped this land. Humanity has become the catalyst of
    destruction once again, and only the strong shall remain. Shall your name strike fear
    in the hearts of man, or shall it inspire praise? Will your nation stand the test of
    time or perish and scatter to the wind?''')
    faction = input('Which nation shall you bring to greatness, oh promised leader?\n')
    return faction

def main():
    class Game:
        def __init__(self):
            self.difficulty = 'easy'


            class Player:
                def __init__(self): #creates the baseline player. Add attributes as seen fit. Note: be careful of the scope
                    self.faction = ''
                    self.reserve = 100 #using int for easy math
                    #add player's city, add player's manpower, add player's influence, add player's faith, add player's resources,
                    #add player's income
#create a dictionary of faction objects each with their own default values for Wealth, Favor, Reputation, Armaments, and Members
#Upon faction selection assign the default values to the values of the player
                def displayStats(self):
                    #use graphics to display player attributes
                    print('yeet')

            self.player1 = Player()
            self.player2 = Player()

    game = Game()
    introduction(game)
    print('\n' + game.difficulty)
    print('\n' + game.player1.faction)
    print('\n' + game.player2.faction)


main()
# Wealth
# Favor
# Reputation
# Armaments
# Members

# Workers' League
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# _ _ _ _ _ _ _ _ _ _ x x x x x x x x x x x x x x x x x x x x x _ _ _ _ _ _ _ _ _ x x x _ _ _ #
# _ _ _ _ _ _ _ _ _ x x x x x x x x x x x x x x x x x x x x _ _ _ _ _ _ _ _ _ x x x x O x x _ #
# _ _ _ _ _ _ x x x x x x x x x x x x x x x x x x x x x O x x x x _ _ _ _ _ _ _ _ x x x x x _ #
# _ _ _ _ x x x x x x x x x x x _ _ _ _ _ _ _ _ _ _ _ x x x x x _ _ _ _ _ _ _ _ _ _ x x _ _ _ #
# _ _ x x x x x x x x x x x x x x _ _ _ _ _ _ _ _ _ _ x x x x _ _ _ _ _ _ _ _ _ _ _ _ x _ _ _ #
# _ x x x x x x x x x x x x x x x _ _ _ _ _ _ _ _ _ _ _ _ x x _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ #
# x O x x x x x x x x x x x x x x x _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ #
# x x x x x x x x x x x x x x x x x x x _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ #
# x x x x x x x x x x x x x x x x x x x x x _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ #
# x x x x x x x x x x x x x x x x x x x x x _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ #
# x x x x x x x x x x x x x x x x O x x _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ #
# x x x x x x x x x x x x x x x x _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ #
# x x x x x x x _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ #
# x x _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ x #
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ x x x x x #
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ x x x x x x x O x x #
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ x x x x x x x x x x x x x #
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ x x x x x x x x x x x x #
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ x x x x x x x x x #
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ x x x x x x x x x x x #
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ x x x x x x x x x x x x x x x x x x x #
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ x x x x x x x x x x x x x x x x x x x #
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ x x x x x x x x x x x x x x x x x x x #
# x x x x x x x x x x x _ _ _ _ _ _ _ _ _ _ _ _ _ x x x x x x x x x x x x x x x x x x x x x x #
# x x x x x x x x x x x x _ _ _ _ _ _ _ _ _ _ x x x x x x x x x x x x x x x x x x x x x x x x #
# x x x O x x x x x x x x x x x _ _ _ x x x x x x x x x x x x x x x x x x x x x x x x x x x x #
# x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x O x x x x x x x x x x x #
# x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x #
