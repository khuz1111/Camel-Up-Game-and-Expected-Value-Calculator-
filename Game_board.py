import random
import colorama
from colorama import init, Fore, Back, Style
from itertools import permutations
from copy import deepcopy


class Game_board:
    def __init__(self) -> None:
        self.available_cards = {'yellow' : [2, 2, 3, 5 ], 'green' : [2, 2, 3, 5 ], 
                                'red' : [2, 2, 3, 5 ], 'blue' : [2, 2, 3, 5 ], 'purple' : [2, 2, 3, 5 ]}
        self.camel_location = {}
        self.board = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 
                      9: [], 10: [], 11:[], 12: [], 13: [], 14: [], 15: [], 16: []}
        self.to_move= ['yellow', 'green', 'red', 'blue', 'purple']

    def setup_camels(self):
        initial = ['yellow', 'green', 'red', 'blue', 'purple']

        while initial:
            camel, move = random.choice(initial), random.choice([1,2,3])
            initial.remove(camel)
            self.board[move].append(camel)
            self.camel_location[camel] = move
        
    def get_next_move(self) -> tuple:
        camel, move = random.choice(self.to_move), random.choice([1,2,3])
        self.to_move.remove(camel)

        return (camel, move)
    
    def update_move(self, move_pair):
        camel, move = move_pair

        stack = []
        index = self.camel_location[camel]

        while self.board[index][-1] != camel:
            stack.append(self.board[index].pop())
        
        stack.append(self.board[index].pop())

        new_index = index + move

        for camel in stack:
            self.camel_location[camel] = new_index

        while stack:
            self.board[new_index].append(stack.pop())

    def move(self):
        move_pair = self.get_next_move()
        self.update_move(move_pair)

    def reset_for_round(self):
        self.to_move= ['yellow', 'green', 'red', 'blue', 'purple']
        self.available_cards = {'yellow' : [2, 2, 3, 5 ], 'green' : [2, 2, 3, 5 ], 
                                'red' : [2, 2, 3, 5 ], 'blue' : [2, 2, 3, 5 ], 'purple' : [2, 2, 3, 5 ]}

    def return_camel_order(self) -> list[str]:
        to_check = ['yellow', 'green', 'red', 'blue', 'purple']
        order = []
        
        while len(to_check) > 0:
            min_index = min([self.camel_location[camel] for camel in to_check])
            temp = self.board[min_index]
            
            # finish returning camel order
            for camel in temp:
                to_check.remove(camel)
                order.append(camel)
                
            
        return order

    def get_board(self):
        to_check = ['yellow', 'green', 'red', 'blue', 'purple']
        output = []
        
        while len(to_check) > 0:
            min_index = min([self.camel_location[camel] for camel in to_check])
            
            # finish returning camel order
            temp = [min_index]

            for camel in self.board[min_index]:
                temp.append(camel)
                to_check.remove(camel)
                
            output.append(tuple(temp))

        return output
    
    def print_term(self, output):
        printout = ""
        cameldict = {"red":Back.RED + "🐪 " + Style.RESET_ALL, "blue":Back.BLUE + "🐪 " + Style.RESET_ALL, "green":Back.GREEN + "🐪 " + Style.RESET_ALL,
                     "yellow":Back.YELLOW + "🐪 " + Style.RESET_ALL, "purple":Back.MAGENTA + "🐪 " + Style.RESET_ALL }
        spacediff = 0
        spaces = ""
        for t in output:
            pos = 0
            numcamels = len(t)-1
            if numcamels>1:
                k=1
                while k<numcamels+1:
                    printout += cameldict[output[pos][k]]
                    k+=1
                pos += 1
                continue
            else:
                if pos < len(output):
                    spacediff = output[pos+1][0]-output[pos][0]
                printout = printout + (spaces * spacediff) + cameldict[output[pos][[1]]]
                pos += 1
                continue
#2, red, green, purple
            
        return printout

    def print_cards(self):
         to_check = ['yellow', 'green', 'red', 'blue', 'purple']

         for camel in to_check:
            if self.available_cards == []:
                 print(f'There are no {camel} betting cards')
            else:
                print(f'The top {camel} betting card is {self.available_cards[camel][-1]}')
    
    def get_all_possible_rolls(self):
        orders = list(permutations(self.to_move))
        length = len(self.to_move)

        def recurse(order, output, temp, index):
            if index == length:
                output.append(temp[:length])
            else:
                color = order[index]
                for i in range(1,4):
                    temp.append((color, i))
                    recurse(order, output, temp, index + 1)
                    temp.pop()

        output = []
        for order in orders:
            temp = []
            recurse(order, output, temp, 0)
        
        return output
    
    def get_probabilities(self):
        rolls = self.get_all_possible_rolls()
        final_orders = []

        for roll in rolls:
            board_copy = deepcopy(self)
            for pair in roll:
                board_copy.update_move(pair)
            order = board_copy.return_camel_order()
            final_orders.append(order)
        
        length = len(final_orders)
        
        camel_dict_first = {'yellow' : 0, 'green': 0, 'red': 0, 'blue': 0, 'purple': 0}
        camel_dict_second = {'yellow' : 0, 'green': 0, 'red': 0, 'blue': 0, 'purple': 0}
        camel_dict_lose = {'yellow' : 0, 'green': 0, 'red': 0, 'blue': 0, 'purple': 0}

        for order in final_orders:
            camel_dict_first[order[-1]] += 1
            camel_dict_second[order[-2]] += 1
            for i in range(0, 4):
                camel_dict_lose[order[i]] += 1
        
        to_check= ['yellow', 'green', 'red', 'blue', 'purple']
        probs = []
        for camel in to_check:
            probs.append((camel, camel_dict_first[camel] / length, camel_dict_second[camel] / length, camel_dict_lose[camel] / length))
        
        output = []
        for i in range(5):
            five_card = 5 * probs[i][1] + probs[i][2] - probs[i][3]
            three_card = 3 * probs[i][1] + probs[i][2] - probs[i][3]
            two_card = 2 * probs[i][1] + probs[i][2] - probs[i][3]
            output.append((to_check[i], five_card, three_card, two_card))
        
        return output

            
        

    
        

