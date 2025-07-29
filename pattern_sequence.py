import random
import time

class Puzzle:
    def __init__(self, difficulty="medium"):
        self.difficulty = difficulty
        self.sequence = self.generate_sequence()
        self.player_sequence = []
        self.display_time = 0.5 if difficulty == "easy" else 0.3 if difficulty == "medium" else 0.2
        self.step = 0
        
    def generate_sequence(self):
        symbols = ['★', '●', '▲', '◆', '■']
        lengths = {"easy": 4, "medium": 6, "hard": 8}
        sequence = []
        
        for _ in range(lengths[self.difficulty]):
            sequence.append(random.choice(symbols))
        
        return sequence
    
    def display(self):
        print("Запомните последовательность:")
        for symbol in self.sequence:
            print(symbol, end=' ', flush=True)
            time.sleep(self.display_time)
            print('\r' + ' ' * 50, end='\r', flush=True)
            time.sleep(0.1)
        print("\nПовторите последовательность:")
    
    def handle_input(self, symbol):
        if symbol in ['1', '2', '3', '4', '5']:
            symbols = ['★', '●', '▲', '◆', '■']
            selected = symbols[int(symbol)-1]
            self.player_sequence.append(selected)
            print(selected, end=' ')
            
            # Проверка соответствия
            if self.player_sequence[self.step] != self.sequence[self.step]:
                print("\nОшибка!")
                return False
                
            self.step += 1
            if self.step == len(self.sequence):
                return True
        return False
    
    def is_solved(self):
        return self.step == len(self.sequence)