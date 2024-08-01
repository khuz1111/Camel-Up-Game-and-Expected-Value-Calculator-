from Player import Player
from Game_board import Game_board

class Game_Manager():
    def __init__(self, players):
        self.players = players

        for i in range(len(players)):
            self.players[i] = Player(players[i])
        
        self.board = Game_board()
        self.rolls = 0
        self.last_move = len(players) - 1
    
    def setup_game(self):
        self.board.setup_camels()

    def get_move(self):
        if self.last_move == len(self.players) - 1:
            cur_player = self.players[0]
            self.last_move = 0
        else:
            cur_player = self.players[self.last_move + 1]
            self.last_move += 1
        
        
        print(f'it is {cur_player}s turn.\n')

        self.board.print_cards()

        cur_board = self.board.get_board()
        print(cur_board, 'n')

        print('the expected value of a 5, 3, or 2 betting card are: \n')
        print(self.board.get_probabilities())

        isnt_valid = True

        while isnt_valid:
            response = input('Type 1 to bet, or 2 to roll:    ')
            if response == '1' or response == '2':
                isnt_valid = False
            else:
                print('type a valid response its not that hard')

        if response == '1':
            valid_response = set()
            to_check = ['yellow', 'green', 'red', 'blue', 'purple']

            for camel in to_check:
                if self.board.available_cards[camel] != []:
                    valid_response.add(camel)
            
            camel = 0
            while camel not in valid_response:
                camel = input('which VALID camel?')

            card_pair = (camel, self.board.available_cards[camel].pop())

            cur_player.cards.append(card_pair)
            print('\n')
        
        elif response == '2':
            self.rolls += 1
            cur_player.coins += 1
            move = self.board.get_next_move()
            print(move, '\n')
            self.board.update_move(move)

    def play_round(self):
        while self.rolls < 5:
            self.get_move()

    def end_round(self):
        response = input('Do you want to play another round? [y/n]:   ')
        if response == 'y':
            self.board.reset_for_round()
            self.rolls = 0
            final_order = self.board.return_camel_order()
            winner = final_order[-1]
            second = final_order[-2]

            for player in self.players:
                for betting_card in player.cards():
                    if betting_card[0] == winner:
                        player.coins += betting_card[1]
                    elif betting_card[0] == second:
                        player.coins += 1
                    else:
                        player.coins -= 1
            return 0
        else:
            final_order = self.board.return_camel_order()
            winner = final_order[-1]
            second = final_order[-2]

            for player in self.players:
                for betting_card in player.cards():
                    if betting_card[0] == winner:
                        player.coins += betting_card[1]
                    elif betting_card[0] == second:
                        player.coins += 1
                    else:
                        player.coins -= 1
            return 1
    
    def play_game(self):
        end_round = 0
        while end_round == 0:
            coin_values = [(player.coins, player.name) for player in self.players]
            print(f'the final results are {coin_values}')
            self.play_round()
            end_round = self.end_round()
        
        self.end_game()

    def end_game(self):
        coin_values = [(player.coins, player.name) for player in self.players]
        print(f'the final results are {coin_values}')
        


            



        
