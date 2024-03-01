#Specialisterne Academy - Uge 2 
# opgave - BlackJack

import numpy as np
import copy
import time
import PySimpleGUI as sg


playing_cards_dict = { 
    #dictionary of a set of playing cards (52 cards) with names and values for BlackJack.
    #Key: A:Ace, J:Jack, Q:Queen, K:King, H:Hearts, S:Spades, C:Clubs, D:Diamonds.
    'AH' : np.array([1,11]) , '2H' : np.array([2]) , '3H'  : np.array([3]) , 
    '4H' : np.array([4]) ,    '5H' : np.array([5]) , '6H'  : np.array([6]) , '7H' : np.array([7]),
    '8H' : np.array([8]) ,    '9H' : np.array([9]) , '10H' : np.array([10]) , 
    'JH' : np.array([10]),    'QH' : np.array([10]), 'KH'  : np.array([10]) , 
    'AS' : np.array([1,11]) , '2S' : np.array([2]) , '3S'  : np.array([3]) , 
    '4S' : np.array([4]) ,    '5S' : np.array([5]) , '6S'  : np.array([6]) , '7S' : np.array([7]),
    '8S' : np.array([8]) ,    '9S' : np.array([9]) , '10S' : np.array([10]) , 
    'JS' : np.array([10]),    'QS' : np.array([10]), 'KS'  : np.array([10]) , 
    'AC' : np.array([1,11]) , '2C' : np.array([2]) , '3C'  : np.array([3]) , 
    '4C' : np.array([4]) ,    '5C' : np.array([5]) , '6C'  : np.array([6]) , '7C' : np.array([7]),
    '8C' : np.array([8]) ,    '9C' : np.array([9]) , '10C' : np.array([10]) , 
    'JC' : np.array([10]),    'QC' : np.array([10]), 'KC'  : np.array([10]) , 
    'AD' : np.array([1,11]) , '2D' : np.array([2]) , '3D'  : np.array([3]) , 
    '4D' : np.array([4]) ,    '5D' : np.array([5]) , '6D'  : np.array([6]) , '7D' : np.array([7]),
    '8D' : np.array([8]) ,    '9D' : np.array([9]) , '10D' : np.array([10]) , 
    'JD' : np.array([10]),    'QD' : np.array([10]), 'KD'  : np.array([10]) , 
                                                                                
    }
image_dict = { 
    #dictionary mapping cards to representative PNG files
    #Key: A:Ace, J:Jack, Q:Queen, K:King, H:Hearts, S:Spades, C:Clubs, D:Diamonds.
    'AH' : 'card_imgs/ace_of_hearts.png' ,   '2H' : 'card_imgs/2_of_hearts.png' ,      '3H' : 'card_imgs/3_of_hearts.png' , 
    '4H' : 'card_imgs/4_of_hearts.png' ,     '5H' : 'card_imgs/5_of_hearts.png' ,      '6H' : 'card_imgs/6_of_hearts.png' ,   '7H' : 'card_imgs/7_of_hearts.png',
    '8H' : 'card_imgs/8_of_hearts.png' ,     '9H' : 'card_imgs/9_of_hearts.png' ,      '10H' : 'card_imgs/10_of_hearts.png' , 
    'JH' : 'card_imgs/jack_of_hearts2.png',  'QH' : 'card_imgs/queen_of_hearts2.png',  'KH' : 'card_imgs/king_of_hearts2.png' , 
    'AS' : 'card_imgs/ace_of_spades.png' ,   '2S' : 'card_imgs/2_of_spades.png' ,      '3S' : 'card_imgs/3_of_spades.png' , 
    '4S' : 'card_imgs/4_of_spades.png' ,     '5S' : 'card_imgs/5_of_spades.png' ,      '6S' : 'card_imgs/6_of_spades.png' ,   '7S' : 'card_imgs/7_of_spades.png',
    '8S' : 'card_imgs/8_of_spades.png' ,     '9S' : 'card_imgs/9_of_spades.png' ,      '10S' : 'card_imgs/10_of_spades.png' , 
    'JS' : 'card_imgs/jack_of_spades2.png',  'QS' : 'card_imgs/queen_of_spades2.png',  'KS' : 'card_imgs/king_of_spades2.png' , 
    'AC' : 'card_imgs/ace_of_clubs.png' ,    '2C' : 'card_imgs/2_of_clubs.png' ,       '3C' : 'card_imgs/3_of_clubs.png' , 
    '4C' : 'card_imgs/4_of_clubs.png' ,      '5C' : 'card_imgs/5_of_clubs.png' ,       '6C' : 'card_imgs/6_of_clubs.png' ,    '7C' : 'card_imgs/7_of_clubs.png',
    '8C' : 'card_imgs/8_of_clubs.png' ,      '9C' : 'card_imgs/9_of_clubs.png' ,       '10C' : 'card_imgs/10_of_clubs.png' , 
    'JC' : 'card_imgs/jack_of_clubs2.png',   'QC' : 'card_imgs/queen_of_clubs2.png',   'KC' : 'card_imgs/king_of_clubs2.png' , 
    'AD' : 'card_imgs/ace_of_diamonds.png' , '2D' : 'card_imgs/2_of_diamonds.png' ,    '3D' : 'card_imgs/3_of_diamonds.png' , 
    '4D' : 'card_imgs/4_of_diamonds.png' ,   '5D' : 'card_imgs/5_of_diamonds.png' ,    '6D' : 'card_imgs/6_of_diamonds.png' , '7D' : 'card_imgs/7_of_diamonds.png',
    '8D' : 'card_imgs/8_of_diamonds.png' ,   '9D' : 'card_imgs/9_of_diamonds.png' ,    '10D' : 'card_imgs/10_of_diamonds.png' , 
    'JD' : 'card_imgs/jack_of_diamonds2.png','QD' : 'card_imgs/queen_of_diamonds2.png','KD' : 'card_imgs/king_of_diamonds2.png' , 
    
    }


def shuffle_cards(cards_dict):
    #Takes key values from the playing_cards_dict and returns them in random order
    SC_deck = list(cards_dict.keys())
    np.random.shuffle(SC_deck)
    return SC_deck




def deal_card(hand, deck):
    #Removes first card from deck and adds it to hand
    hand.append(deck[0])
    deck.pop(0)
    return hand, deck




def initialize_game(cards_dict):
    #Sets initial deck and hands by drawing 2 cards to both player and dealer
    init_player_hand = []
    init_dealer_hand = []
    init_deck = shuffle_cards(cards_dict)
    
    init_player_hand, init_deck = deal_card(init_player_hand, init_deck)
    
    init_dealer_hand, init_deck = deal_card(init_dealer_hand, init_deck)
    
    init_player_hand, init_deck = deal_card(init_player_hand, init_deck)
    
    init_dealer_hand, init_deck = deal_card(init_dealer_hand, init_deck)
    
    #print(init_deck)
    #print(init_player_hand)
    #print(init_dealer_hand)
    
    return init_player_hand, init_dealer_hand, init_deck




def compute_score(hand, cards_dict):
    # Given a blackjack hand, computes score, including ambiguous scores with Aces in hand

    CS_hand_values = []
    # Find card values from dictionary
    for i in range(len(hand)):
        CS_hand_values.append(cards_dict[hand[i]])
       
    #print(CS_hand_values)
    # adds up score of cards in hand, making sure to account for possibilities
    # offered by any aces present in hand
    CS_hand_sum = np.array([0])
    for i in range(len(hand)):
        if len(CS_hand_values[i]) == 1:
            CS_hand_sum += CS_hand_values[i]
        else:
            CS_temp1 = copy.deepcopy(CS_hand_sum) + CS_hand_values[i][0]
            CS_temp2 = copy.deepcopy(CS_hand_sum) + CS_hand_values[i][1]
            CS_hand_sum = CS_temp1
            CS_hand_sum = np.append(CS_hand_sum, CS_temp2)
    
    # Sorts potential scores in descending order
    CS_score=0
    CS_hand_sum = np.sort(CS_hand_sum)
    CS_hand_sum = CS_hand_sum[::-1]
    #print('Sorted possible scores: '+ str(CS_hand_sum))
    
    # Returns the highest potential score that doesn't violate the 21 score limit.
    # If no such score exists returns highest (only) score.
    for i in range(len(CS_hand_sum)):
        CS_score = CS_hand_sum[i]
        if CS_hand_sum[i] <=21:
            break
    #if CS_score >= 22:
    #    print(str(CS_score) + ', you lose')
    #else:
    #    print('Score: '+str(CS_score))    
    #print('Score: '+str(CS_score))
    return CS_score




def dealer_logic(player_hand, dealer_hand, deck):
    # Decision 'AI' for dealer; draws on 16 or below, stands on 17 or above.
    
    #Calculate scores and check if player went bust
    DL_player_score = compute_score(player_hand, playing_cards_dict)
    DL_dealer_score = compute_score(dealer_hand, playing_cards_dict)
    if DL_player_score >=22:
        print('House Wins\nYour Score: '+str(DL_player_score)+'\nDealer Score: '+str(DL_dealer_score))
        return
    
    # Dealer draws card if below 16, stops when at 17 or above.
    while DL_dealer_score <= DL_player_score or DL_dealer_score <= 16:
        
        if DL_dealer_score >= 17:
            break
        
        dealer_hand, deck = deal_card(dealer_hand, deck)
        print('Dealer drew '+str(dealer_hand[-1])+'\n')
        DL_dealer_score = compute_score(dealer_hand, playing_cards_dict)
        time.sleep(0.7)
    # Evaluate result; Win, lose or push.
    if DL_dealer_score <= DL_player_score-1 or DL_dealer_score >= 22:
        print('YOU WIN!!!\n\nYour Score: '+str(DL_player_score)+'\n\nDealer Score: '+str(DL_dealer_score))
    elif DL_dealer_score >= DL_player_score+1:
        print('House Wins\n\nYour Score: '+str(DL_player_score)+'\n\nDealer Score: '+str(DL_dealer_score))
    else:
        print('It´s a push!\n\nYour Score: '+str(DL_player_score)+'\n\nDealer Score: '+str(DL_dealer_score))
    return



def play_blackjack(cards_dict):
    # Initialize dictionary, deck and hands:
    PBJ_cards_dict = cards_dict
    PBJ_player_hand, PBJ_dealer_hand, PBJ_deck = initialize_game(PBJ_cards_dict)
    
    PBJ_player_score = compute_score(PBJ_player_hand, PBJ_cards_dict)
    PBJ_dealer_score = compute_score(PBJ_dealer_hand, PBJ_cards_dict)
    
    #Show player hand and open dealer card
    print('Your cards are '+str(PBJ_player_hand[0])+' and '+str(PBJ_player_hand[1]) + ' with a current score of '+str(PBJ_player_score)+'\n')
    print('Dealers open card is '+str(PBJ_dealer_hand[1])+'\n')
    
    
    while PBJ_player_score <= 22:
        
        PBJ_input = input('HIT/STAND\n\n')
        
        time.sleep(0.7)
        
        if PBJ_input == 'HIT':
            
            PBJ_player_hand, PBJ_deck = deal_card(PBJ_player_hand, PBJ_deck)
            
            PBJ_player_score = compute_score(PBJ_player_hand, PBJ_cards_dict)
            
            print('\n You drew '+str(PBJ_player_hand[-1])+'!\n')
            
            print('\n Your current score is '+str(PBJ_player_score)+'\n')
        elif PBJ_input == 'STAND':
            break
        
        else:
            print('\nERROR: invalid input\n')
        
    print('\nDealers hidden card is '+str(PBJ_dealer_hand[0])+'\n')
    
    time.sleep(0.7)
    
    dealer_logic(PBJ_player_hand, PBJ_dealer_hand, PBJ_deck)
    
    
    return

#play_blackjack(playing_cards_dict)





#frames = 7








def BLACKJACK(cards_dict,imgs_dict):
    # Initialize dictionary, deck and hands:
    sg.theme('Dark Green 1')
    A = ''
    B = ''
    BJ_dealer_hand = []
    BJ_player_hand = []
    BJ_deck = []
    BJ_pot = 0
    BJ_bet = 0
    BJ_stash = 500
    BJ_player_score = 0
    BJ_dealer_score = 0
    BJ_split_score = 0
    stand = False
    split = False
    split_turn = False
    split_end = False
    split_stand = False
    
    layout = [
        [ sg.Text('Dealer´s Hand',key='text_dealer_hand',visible=False)],
        
        [sg.Image(key='dummy_imga1'), sg.Image(key='dummy_imga2'), sg.Image(key='dummy_imga3'), sg.Image(key='dummy_imga4'), 
         sg.Image(key='dummy_imga5'), sg.Image(key='dummy_imga6'), 
         sg.Image(key='dealer_card1'),sg.VPush(),sg.Image(key='dealer_card2'), sg.Image(key='dealer_card3'), sg.Image(key='dealer_card4'),
         sg.Image(key='dealer_card5'), sg.Image(key='dealer_card6'), sg.Image(key='dealer_card7'), sg.Image(key='dealer_card8')],
        [ sg.Text('BLACK JACK',key='text_mid', font=('Courier New', 30))],
        
        [sg.Text('You´ve gone broke, stash has been reset at 500', font=('Arial Bold', 10,'italic'),key='broke',visible=False)],
        [ sg.Text('Player´s Hand',key='text_player_hand',visible=False,justification='center')],
        
        [sg.Image(key='dummy_imgb1'), sg.Image(key='dummy_imgb2'), sg.Image(key='dummy_imgb3'), sg.Image(key='dummy_imgb4'), 
         sg.Image(key='dummy_imgb5'), sg.Image(imgs_dict['AS'],key='dummy_imgb6'), 
         sg.Image(imgs_dict['AH'],key='player_card1'), sg.Image(imgs_dict['AC'],key='player_card2'), 
         sg.Image(imgs_dict['AD'],key='player_card3'), sg.Image(key='player_card4'),
         sg.Image(key='player_card5'), sg.Image(key='player_card6'), sg.Image(key='player_card7'), sg.Image(key='player_card8')],
        
        [  sg.Button('PLAY',key='play_button'),sg.Input('Bet',key='bet',size=(6,1)),],
        
        [sg.Button('SPLIT CARDS',key='split_button',visible=False),sg.Button('DOUBLE DOWN',key='double_button',visible=False), 
         sg.Button('HIT',key='hit_button',visible=False), sg.VPush(), sg.Button('STAND',key='stand_button',visible=False),sg.Image(key='dummy_imgc')],
        
        [sg.Image('poker_chip3.png'),sg.Text('Stash: '+str(BJ_stash),key='stash'),sg.Push(),sg.Text('Pot: '+str(BJ_pot),key='pot',visible=False)]
        
        ]    
    
    window = sg.Window('Black Jack',layout, size=(900, 475),icon='BlackJack_icon.ico', element_justification='c')
    
    while True:
        
        event, values = window.read(timeout = 1000)
        
        BJ_cards_dict = cards_dict
        BJ_imgs_dict = imgs_dict
        
        if event == sg.WIN_CLOSED:
            break
        
        
        if event == 'play_button':
            window['broke'].update(visible=False)
            stand = False
            try:
                BJ_bet = int(values['bet'])
                
            except:
                window['text_mid'].update('Please select a valid bet', font=('Arial Bold', 10,'italic'))
                
                
            BJ_player_hand, BJ_dealer_hand, BJ_deck = initialize_game(BJ_cards_dict)
    
            BJ_player_score = compute_score(BJ_player_hand, BJ_cards_dict)
            BJ_dealer_score = compute_score(BJ_dealer_hand, BJ_cards_dict)

            
            if isinstance(BJ_bet, int)==False:
                
                window['text_mid'].update('Please select a valid bet', font=('Arial Bold', 10,'italic'))
                
            elif BJ_bet >= BJ_stash+1:
                window['text_mid'].update('Insufficient funds, please lower your bet', font=('Arial Bold', 10,'italic'))
                
            
            elif isinstance(BJ_bet, int)==True and BJ_bet>=1:
            
                BJ_pot = 0
                
                BJ_pot+=2*BJ_bet
                BJ_stash-=BJ_bet
                window['pot'].update('Pot: '+str(BJ_pot))
                window['stash'].update('Stash: '+str(BJ_stash))
                
                #Show cards and clear old cards
                window['dealer_card1'].update('card_imgs/backside.png')
                window['dealer_card2'].update(BJ_imgs_dict[BJ_dealer_hand[1]])
                window['dealer_card3'].update('')
                window['dealer_card4'].update('')
                window['dealer_card5'].update('')
                window['dealer_card6'].update('')
                window['dealer_card7'].update('')
                window['dealer_card8'].update('')
                
                window['dummy_imgb1'].update('')
                window['dummy_imgb2'].update('')
                window['dummy_imgb3'].update('')
                window['dummy_imgb4'].update('')
                window['dummy_imgb5'].update('')
                window['dummy_imgb6'].update('')
                window['player_card1'].update(BJ_imgs_dict[BJ_player_hand[0]])
                window['player_card2'].update(BJ_imgs_dict[BJ_player_hand[1]])
                window['player_card3'].update('')
                window['player_card4'].update('')
                window['player_card5'].update('')
                window['player_card6'].update('')
                window['player_card7'].update('')
                window['player_card8'].update('')
                
                #adjust visible text and buttons
                window['text_dealer_hand'].update(visible=True)
                window['text_player_hand'].update(visible=True)
                window['hit_button'].update(visible=True)
                window['stand_button'].update('STAND',visible=True)
                if BJ_stash >= BJ_bet:
                    window['double_button'].update(visible=True)
                
                window['pot'].update(visible=True)
                window['bet'].update('Bet',visible=False)
                
                
                window['text_mid'].update('Dealer must hit on 16 and stand on soft 17', font=('Arial Bold', 10,'italic'))
                
                window['play_button'].update(visible=False)
                

                if BJ_player_hand[0][0] == BJ_player_hand[1][0]:
                    window['split_button'].update(visible=True)
                    
                    
        if event == 'split_button' and BJ_stash >= BJ_bet:
            window['split_button'].update(visible=False)
            BJ_pot=2*BJ_pot
            BJ_stash-=BJ_pot//2
            split = True
            BJ_split_hand = [BJ_player_hand[0]]
            BJ_player_hand.pop(0)
            BJ_split_hand, BJ_deck = deal_card(BJ_split_hand, BJ_deck)
            BJ_player_hand, BJ_deck = deal_card(BJ_player_hand,BJ_deck)
            
            window['text_mid'].update('Dealing to right hand', font=('Arial Bold', 10,'italic'))

            
            window['player_card1'].update(BJ_imgs_dict[BJ_player_hand[0]])
            window['player_card2'].update(BJ_imgs_dict[BJ_player_hand[1]])
            
            window['dummy_imgb1'].update(BJ_imgs_dict[BJ_split_hand[0]])
            window['dummy_imgb2'].update(BJ_imgs_dict[BJ_split_hand[1]])
            stand = False
            
            
        if event == 'hit_button' and split_turn == False:
                
            BJ_player_hand, BJ_deck = deal_card(BJ_player_hand, BJ_deck)
                
            BJ_player_score = compute_score(BJ_player_hand, BJ_cards_dict)
                
            window['player_card'+str(len(BJ_player_hand))].update(BJ_imgs_dict[BJ_player_hand[-1]])
            window['double_button'].update(visible=False)
            window['split_button'].update(visible=False)
            if split == True and BJ_player_score >=22:
                split = False
                split_turn = True
                
                
        if event == 'double_button':
            
            BJ_stash -= BJ_pot//2
            BJ_pot = 2*BJ_pot
            
            window['pot'].update('Pot: '+str(BJ_pot))
            window['stash'].update('Stash: '+str(BJ_stash))
            window['double_button'].update(visible=False)
            stand = False
            
            
        if  BJ_player_score >= 22 and split == False or BJ_player_score >= 22 and split_turn==False:
            
            if BJ_stash == 0:
                
                window['text_mid'].update('House Wins', font=('Arial Bold', 20))
                window['broke'].update(visible=True)
                BJ_stash = 500
            
                window['dealer_card1'].update(BJ_imgs_dict[BJ_dealer_hand[0]])
                
                window['hit_button'].update(visible=False)
                window['stand_button'].update(visible=False)            
                
                window['play_button'].update(visible=True)     
                window['bet'].update(visible=True)
                window['double_button'].update(visible=False)
                window['split_button'].update(visible=False)
                BJ_pot = 0
                window['pot'].update('Pot: '+str(BJ_pot))
                window['stash'].update('Stash: '+str(BJ_stash))
                BJ_player_score = 0
                stand = False
                
            else:
                
                window['dealer_card1'].update(BJ_imgs_dict[BJ_dealer_hand[0]])
                
                window['hit_button'].update(visible=False)
                window['stand_button'].update(visible=False)            
                
                window['play_button'].update(visible=True)     
                window['bet'].update(visible=True)
                window['double_button'].update(visible=False)
                window['split_button'].update(visible=False)
                
                window['text_mid'].update('House Wins', font=('Arial Bold', 20)) 
                BJ_pot = 0
                window['pot'].update('Pot: '+str(BJ_pot))
                window['stash'].update('Stash: '+str(BJ_stash))
                stand = False
                
            
        if event == 'stand_button'and split == False and split_end == False:
            
            stand = True
            window['dealer_card1'].update(BJ_imgs_dict[BJ_dealer_hand[0]])
            window['double_button'].update(visible=False)
            window['split_button'].update(visible=False)
            window['hit_button'].update(visible=False)
            window['stand_button'].update(visible=False)
            
        if event == 'stand_button'and split == True and split_end == False:
            
            window['split_button'].update(visible=False)
            split = False
            split_turn = True
            window['text_mid'].update('Dealing to left hand', font=('Arial Bold', 10,'italic'))
            
            
            
        if event == 'hit_button' and split_turn == True:
            
            BJ_split_hand, BJ_deck = deal_card(BJ_split_hand, BJ_deck)
                
            BJ_split_score = compute_score(BJ_split_hand, BJ_cards_dict)
                
            window['dummy_imgb'+str(len(BJ_split_hand))].update(BJ_imgs_dict[BJ_split_hand[-1]])
            window['double_button'].update(visible=False)
            window['split_button'].update(visible=False)
            
            split_end = True
            if BJ_split_score >= 22:
                split_turn = False
                window['hit_button'].update(visible=False)
                window['stand_button'].update(visible=False)
                split_stand = True
            
        
        if event == 'stand_button' and split_end == True:
            
            split_end = False
            split_turn = False
            window['dealer_card1'].update(BJ_imgs_dict[BJ_dealer_hand[0]])
            window['double_button'].update(visible=False)
            window['split_button'].update(visible=False)
            window['hit_button'].update(visible=False)
            window['stand_button'].update(visible=False)
            split_stand = True
        
            
        if  BJ_split_score >= 22:
            
            split_stand = True
        
        
        if event == sg.TIMEOUT_KEY and split_stand == True:
        
            if BJ_dealer_score >= 17:
                
                
                split_end = False
                split_stand = False
                window['play_button'].update(visible=True)
                window['stand_button'].update(visible=False)
                window['bet'].update(visible=True)
                stand = False
                
                
                if BJ_dealer_score >= 22 and BJ_player_score <=21 and BJ_split_score <=21:
                    
                    A = 'W'
                    B = 'W'
                    
                if BJ_player_score <=21 and BJ_player_score >= BJ_dealer_score+1:
                    
                    A = 'W'
                
                if BJ_dealer_score >= BJ_player_score+1 and BJ_dealer_score<=21:
                    
                    A = 'L'
                
                if BJ_player_score == BJ_dealer_score and BJ_player_score <=21:
                    
                    A = 'X'
                    
                if BJ_split_score <=21 and BJ_split_score >= BJ_dealer_score+1:
                    
                    B = 'W'
                
                if BJ_dealer_score >= BJ_split_score+1 and BJ_dealer_score<=21:
                    
                    B = 'L'
                
                if BJ_split_score == BJ_dealer_score and BJ_split_score <=21:
                    
                    B = 'X'  
                    
                if (A,B) == ('W','W'):
                    window['text_mid'].update('DOUBLE WIN!!!!', font=('Arial Bold', 20))
                    BJ_stash +=BJ_pot

                    
                if (A,B) == ('X','X'):
                    window['text_mid'].update('It´s a push on both hands!', font=('Arial Bold', 20))
                    BJ_stash += BJ_pot//2

                if (A,B) == ('L','L'):
                    if BJ_stash == 0:
                        window['text_mid'].update('House Wins both hands', font=('Arial Bold', 20))
                        window['broke'].update(visible=True)
                        BJ_stash = 500

                    else:
                        window['text_mid'].update('House Wins both hands', font=('Arial Bold', 20))

                if (A,B) == ('W','X') or (A,B) == ('X','W'):
                    window['text_mid'].update('One win, one draw!!', font=('Arial Bold', 20))
                    BJ_stash +=3*BJ_pot//4

                if (A,B) == ('W','L') or (A,B) == ('L','W'):
                    window['text_mid'].update('You win some, you lose some', font=('Arial Bold', 20))
                    BJ_stash +=BJ_pot//2

                    
                if (A,B) == ('X','L') or (A,B) == ('L','X'):
                    window['text_mid'].update('Could be worse', font=('Arial Bold', 20))
                    BJ_stash +=BJ_pot//4

                    
                BJ_pot = 0
                window['pot'].update('Pot: '+str(BJ_pot))
                window['stash'].update('Stash: '+str(BJ_stash))
                split_stand = False
                BJ_split_score = 0
                

                
            if BJ_dealer_score <=16:
               BJ_dealer_hand, BJ_deck = deal_card(BJ_dealer_hand, BJ_deck)
           
               BJ_dealer_score = compute_score(BJ_dealer_hand, BJ_cards_dict)
               window['dealer_card'+str(len(BJ_dealer_hand))].update(BJ_imgs_dict[BJ_dealer_hand[-1]])
           
            
            #if BJ_dealer_score >= 17:
             #   if BJ_dealer_score >= 22:
              #      
               #     A = 'w'
                #    B = 'w'
        
        
        if event == sg.TIMEOUT_KEY and stand == True:
            
        
            window['dealer_card1'].update(BJ_imgs_dict[BJ_dealer_hand[0]])
            window['hit_button'].update(visible=False)
            window['stand_button'].update(visible=False)  
            window['double_button'].update(visible=False)
            window['split_button'].update(visible=False)
            if BJ_dealer_score >= 17:
                
                window['play_button'].update(visible=True) 
                window['stand_button'].update(visible=False)
                window['bet'].update(visible=True)
                stand = False
                
                
                
                
                if BJ_dealer_score <= BJ_player_score-1 or BJ_dealer_score >= 22:
                    window['text_mid'].update('YOU WIN!!!!', font=('Arial Bold', 20))

                    BJ_stash +=BJ_pot


    
                elif BJ_dealer_score >= BJ_player_score+1 and BJ_dealer_score <= 21:
                    if BJ_stash == 0:
                        window['text_mid'].update('House Wins', font=('Arial Bold', 20))
                        window['broke'].update(visible=True)
                        BJ_stash = 500


                    else:
                        window['text_mid'].update('House Wins', font=('Arial Bold', 20))

                
                else:
                    window['text_mid'].update('It´s a push!', font=('Arial Bold', 20))

                    BJ_stash +=BJ_pot//2
                 
                BJ_pot = 0
                window['pot'].update('Pot: '+str(BJ_pot))
                window['stash'].update('Stash: '+str(BJ_stash))
                stand = False    


                    
                    
            if BJ_dealer_score <=16:
                BJ_dealer_hand, BJ_deck = deal_card(BJ_dealer_hand, BJ_deck)
            
                BJ_dealer_score = compute_score(BJ_dealer_hand, BJ_cards_dict)
                window['dealer_card'+str(len(BJ_dealer_hand))].update(BJ_imgs_dict[BJ_dealer_hand[-1]])
                
                
                
            if BJ_dealer_score >= 17:
                
                window['play_button'].update(visible=True) 
                window['stand_button'].update(visible=False)
                window['bet'].update(visible=True)
                stand = False
                
                
                if BJ_dealer_score <= BJ_player_score-1 or BJ_dealer_score >= 22:
                    window['text_mid'].update('YOU WIN!!!!', font=('Arial Bold', 20))

                    BJ_stash +=BJ_pot


                elif BJ_dealer_score >= BJ_player_score+1 and BJ_dealer_score <= 21:
                    if BJ_stash == 0:
                        window['text_mid'].update('House Wins', font=('Arial Bold', 20))
                        window['broke'].update(visible=True)
                        BJ_stash = 500


                    else:
                        window['text_mid'].update('House Wins', font=('Arial Bold', 20))


                else:
                    window['text_mid'].update('It´s a push!', font=('Arial Bold', 20))
                    
                    BJ_stash += BJ_pot//2
                
                BJ_pot = 0
                window['pot'].update('Pot: '+str(BJ_pot))
                window['stash'].update('Stash: '+str(BJ_stash))
                stand = False

                
            
            # Decision 'AI' for dealer; draws on 16 or below, stands on 17 or above.
            
   
            # Evaluate result; Win, lose or push.

                
    window.close()

    return  
            
            
            
            
            
            
            
BLACKJACK(playing_cards_dict,image_dict)        
            




