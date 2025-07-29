import random
import time

class Puzzle:
    def __init__(self, difficulty="medium"):
        self.difficulty = difficulty
        self.sequence = []
        self.player_sequence = []
        self.current_step = 0
        self.generate_sequence()
        
    def generate_sequence(self):
        # Определяем длину последовательности в зависимости от сложности
        lengths = {
            "easy": 4,
            "medium": 6,
            "hard": 8
        }
        length = lengths.get(self.difficulty, 6)
        
        # Генерируем случайную последовательность
        symbols = ['A', 'B', 'C', 'D']
        self.sequence = [random.choice(symbols) for _ in range(length)]
    
    def display(self):
        # Показываем последовательность игроку
        print("Запоминайте последовательность:")
        for symbol in self.sequence:
            print(symbol, end=' ', flush=True)
            time.sleep(1)
            print('\r' + ' ' * len(self.sequence * 2), end='\r', flush=True)
            time.sleep(0.3)
        
        print("\nВремя повторить последовательность!")
    
    def handle_input(self, key):
        # Обрабатываем ввод игрока
        if key.upper() in ['A', 'B', 'C', 'D']:
            self.player_sequence.append(key.upper())
            print(key.upper(), end=' ')
            
            # Проверяем соответствие последовательности
            if self.player_sequence[self.current_step] != self.sequence[self.current_step]:
                print("\nОшибка! Неверный символ.")
                return False
            
            self.current_step += 1
            
            # Проверяем завершение
            if self.current_step == len(self.sequence):
                return True
        return False
    
    def is_solved(self):
        return self.current_step == len(self.sequence)