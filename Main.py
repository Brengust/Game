from module1 import graphics

def introduction():
    print('''The year is 1923. The world was thrown into disarray after the assassination of \n
    Archduke Ferdinand in 1914. The nations of the world saw this as an opportunity to show\n
    the recent technological innovations of war, and make known their dominance. But, as with\n
    the creation of tools of destruction comes the naiveté of man. So prone is man to the\n
    belief that one can safely harness a destructive power against another, with little fear of the\n
    repercussions. The Miasma Expansion of 1915 marked the fall of humanity, a testament to the\n
    foolishness of man. Yet, still some cling to life, and even still whispers of hope can become\n
    heard through the streets. Even without king or country, humans still find the need to\n
    survive.''')




def rules():
    player_status = input('Is this your first time playing? If so, enter "RULES". If not enter "PLAY".\n')
    if player_status == 'RULES':
        rule_page = ''
        rule_book = {'1': '',
         '2': '',
          '3': '',
           '4': '',
            '5': '',
             '6': '',
              '7': '',
               '8': ''}
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
    return

def main(window, pyglet):
    introduction()




main()
