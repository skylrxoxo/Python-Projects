#START 

#intro to program, then gather user input

print ("Welcome to my Balatro calculator. The goal of this program is to help you reach 300 points in hand 1.")

def read_hand():
    hand = []

    for (i) in range(5):
        card = input("Enter card " + str(i + 1) + " (e.g. 'KD' for King of Diamonds): ")
        hand.append(card)

    return hand



#target score = 300 for first blind

target_score = 300

#store hand score data

hand_score = 0; 


#store player hand

hand = read_hand()

ranks = []
suits = []

for card in hand:

    rank = card[0]
    suit = card[1]
    ranks.append(rank)
    suits.append(suit)
    print("Card:", card, "| Rank:", rank, "| Suit:", suit)

print("Ranks:", ranks)
print("Suits:", suits)



#count how many of each rank exists

rank_counts = {}

for card in hand:
    rank = card[0]

    if rank in rank_counts:
        rank_counts[rank] += 1
    else:
        rank_counts[rank] = 1

counts = list(rank_counts.values())
counts.sort()

    #print(counts)


#store ranks as values for straight detection

rank_values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

values = []


for rank in ranks:
    values.append(rank_values[rank])

values.sort()

if values == [2, 3, 4, 5, 14]:
    is_straight = True
else:
    is_straight = True

    for i in range(len(values) - 1):
        if values[i + 1] != values[i] + 1:
            is_straight = False

#detect flush

if  suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
    is_flush = True
else:
    is_flush = False

#detect hand type

if counts == [1,1,1,2]:
    hand_type = "pair"

elif counts == [1,2,2]:
    hand_type = "two_pair"

elif counts == [1,1,3]:
    hand_type = "three_kind"

elif is_straight == True and is_flush == False:
    hand_type = "straight"  

elif is_straight == False and is_flush == True:
    hand_type = "flush"

elif counts == [1,2,2]:
    hand_type = "full_house"

elif is_straight == True and is_flush == True:
    hand_type = "straight_flush"    

else:
    hand_type = "high_card"


#evaluate hand, then store hand and card scoring values
    
hand_scores = {

    "high_card": {"chips": 5, "mult": 1},
    "pair": {"chips": 10, "mult": 2},
    "two_pair": {"chips": 20, "mult": 2},
    "three_kind": {"chips": 30, "mult": 3},
    "straight": {"chips": 30, "mult": 4},
    "flush": {"chips": 35, "mult": 4},
    "full_house": {"chips": 40, "mult": 4},
    "four_kind": {"chips": 60, "mult": 7},
    "straight_flush": {"chips": 100, "mult": 8}
}

card_scores = {

    "A": 11,
    "K": 10,
    "Q": 10,
    "J": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

#retrieve base chips and multiplier of hand

base_chips = hand_scores[hand_type]["chips"]
multiplier = hand_scores[hand_type]["mult"] 

#calculate chips from cards in hand
card_chips = 0

for card in hand:
    rank = card[0]
    card_chips += card_scores[rank]

#calcuate total chips
total_chips = base_chips + card_chips
total_score = total_chips * multiplier

print("Hand type:", hand_type)
print("Base chips:", base_chips)
print("Card chips:", card_chips)
print("Total chips:", total_chips)
print("Multiplier:", multiplier)
print("Score:", total_score)

#compare to target score

if total_score >= target_score:

    print("Beats the first blind!")
else:

    print("Does not beat the first blind!")    

#print result

#END