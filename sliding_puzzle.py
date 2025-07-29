import random
import numpy as np

class Puzzle:
    def __init__(self, size=4):
        self.size = size
        self.board = np.arange(1, size*size + 1).reshape(size, size)
        self.board[-1, -1] = 0  # Пустая клетка
        self.empty_pos = (size-1, size-1)
        self.scramble()
        
    def scramble(self, moves=100):
        """Перемешивает пазл"""
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Вправо, вниз, влево, вверх
        
        for _ in range(moves):
            valid_moves = []
            for dx, dy in directions:
                nx, ny = self.empty_pos[0] + dx, self.empty_pos[1] + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    valid_moves.append((dx, dy))
            
            if valid_moves:
                dx, dy = random.choice(valid_moves)
                self.move_tile(self.empty_pos[0] + dx, self.empty_pos[1] + dy)
    
    def move_tile(self, x, y):
        """Перемещает плитку на пустое место"""
        if abs(x - self.empty_pos[0]) + abs(y - self.empty_pos[1]) != 1:
            return False  # Можно двигать только соседние плитки
            
        # Меняем местами плитку и пустую клетку
        self.board[self.empty_pos[0], self.empty_pos[1]] = self.board[x, y]
        self.board[x, y] = 0
        self.empty_pos = (x, y)
        return True
        
    def display(self):
        """Отображает текущее состояние пазла"""
        for row in self.board:
            print(" | ".join(f"{num:2d}" if num != 0 else "  " for num in row))
            print("-" * (self.size * 4 - 1))
            
    def is_solved(self):
        """Проверяет, решена ли головоломка"""
        flat = self.board.flatten()
        for i in range(1, self.size*self.size):
            if flat[i-1] != i:
                return False
        return flat[-1] == 0