__author__ = 'Yoonsang'

# Problem 6 in Problem Set 5: Ghost

WORDLIST_FILENAME = "words.txt"

#given code

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

#given code ends

def lose(player, fragment, word_list):
    if fragment in word_list:
        if len(fragment) > 3:
            print player, "loses because '%s' is a word" % fragment
            return True
        else:
            if not any(word.startswith(fragment) for word in word_list if len(word) > len(fragment)):
                print player, "loses because no word begins with '%s'" % fragment
                return True
    else:
       if not any(word.startswith(fragment) for word in word_list):
           print player, "loses because no word begins with '%s'" % fragment
           return True

    return False


def is_input_valid(input):
    if len(input) == 1 and input in string.ascii_letters:
        return True
    else: return False


def display_fragment_player(fragment, player):
    print "Current word fragment is: ", "'%s'" % fragment
    print "%s's turn." % (player)


def update_player(player):
    if player == 'Player 1':
        return 'Player 2'
    else:
        return 'Player 1'


def update_fragment(letter, fragment): #returns an updated fragment
    # fragment variable = previous fragment, string
    # letter = new letter
    return fragment + letter


def play_round(word_list):
    fragment = ''
    player = 'Player 1'

    print 'Welcome to Ghost!'
    print 'Player 1 goes first'

    while True:
        display_fragment_player(fragment, player)
        letter = raw_input("%s says: " % player)
        print #to add a blank line

        if not is_input_valid(letter):
            print 'Invalid input! Please try again. Only a single letter is valid'
            print
            continue

        letter = letter.lower()
        fragment = update_fragment(letter, fragment)

        if not lose(player, fragment, word_list):
            player = update_player(player)

        else:
            lose(player, fragment, word_list)
            player =  update_player(player)
            print player, 'wins!'
            break


def play_game():
    wordlist = load_words()
    while True:
        cmd = raw_input('Enter n to play a new round, or e to end game: ')
        if cmd == 'n':
            play_round(wordlist)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

play_game()
