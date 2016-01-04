#
# Problem Set 6, Problem 3
#

def is_valid_word(word, hand, points_dict):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    freq = get_frequency_dict(word)
    for letter in word:
        if freq[letter] > hand.get(letter, 0):
            return False
    return points_dict.get(word, None) != None

def pick_best_word(hand, points_dict):
    """
        Return the highest scoring word from points_dict that can be made with the given hand.
        Return '.' if no words can be made with the given hand.
    """
    bestWord = None
    bestPoint = 0
    for key in points_dict:
        if is_valid_word(key, hand, points_dict):
            #print key, points_dict[key]
            if bestPoint < points_dict[key]:
                bestWord = key
                bestPoint = points_dict[key]
                return bestWord
    #print bestWord, bestPoint
    return '.'

def get_time_limit(points_dict, k):
         """
         Return the time limit for the computer player as a function of the
         multiplier k.
         points_dict should be the same dictionary that is created by
         get_words_to_points.
         """
         start_time = time.time()
         # Do some computation. The only purpose of the computation is so we can
         # figure out how long your computer takes to perform a known task.
         for word in points_dict:
             get_frequency_dict(word)
             get_word_score(word, HAND_SIZE)
         end_time = time.time()
         return (end_time - start_time) * k

#
# Playing a hand
#
def play_hand(hand, word_list):
    time_limit = get_time_limit(points_dict, 1)
    total = 0
    initial_handlen = sum(hand.values())
    time_left = time_limit

    while pick_best_word(hand, points_dict) != '.':
        print 'Current Hand:',
        display_hand(hand)
        start_time = time.time()
        computerWord = pick_best_word(hand, points_dict)
        end_time = time.time()
        total_time = end_time - start_time

        time_left -= total_time
        if time_left >= 0:
            points = get_word_score(computerWord, initial_handlen)
            total += points
            hand = update_hand(hand, computerWord)
            print "Answer: '%s';" % computerWord, "It took %0.8f seconds to provide an answer." % total_time
            print '"%s" earned %0.2f points. Total: %0.2f points.' %(computerWord, points, total)
            print "Remaining time: ", time_left
        else:
            print "It took %0.8 seconds to provide an answer." % total_time
            print "Total time exceeds %0.8f seconds." % time_limit,
            break
    print 'You scored %.02f points in total.' % total

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    get_words_to_point(word_list)
    play_game(word_list)
