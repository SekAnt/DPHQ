import random

class Puzzle:
    def __init__(self, difficulty="medium"):
        self.difficulty = difficulty
        self.solution = self.generate_solution()
        self.puzzle = self.generate_puzzle()
        self.original_puzzle = [row[:] for row in self.puzzle]

    def generate_solution(self):
        # Создаем валидное решение Судоку
        base = 3
        side = base * base
        
        def pattern(r, c): 
            return (base * (r % base) + r // base + c) % side
        
        def shuffle(s): 
            return random.sample(s, len(s))
        
        r_base = range(base)
        rows = [g * base + r for g in shuffle(r_base) for r in shuffle(r_base)]
        cols = [g * base + c for g in shuffle(r_base) for c in shuffle(r_base)]
        nums = shuffle(range(1, base * base + 1))
        
        return [[nums[pattern(r, c)] for r in rows for c in cols]

    def generate_puzzle(self):
        puzzle = [row[:] for row in self.solution]
        
        # Убираем цифры в зависимости от сложности
        diffs = {
            "easy": 30,
            "medium": 40,
            "hard": 50
        }
        
        squares = 9 * 9
        empties = min(diffs.get(self.difficulty, 40), squares - 20)
        
        for p in random.sample(range(squares), empties):
            puzzle[p // 9][p % 9] = 0
            
        return puzzle

    def display(self):
        for i, row in enumerate(self.puzzle):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            print(" ".join(str(x) if x != 0 else "." for x in row[i*3:i*3+3]), 
                  "|", 
                  " ".join(str(x) if x != 0 else "." for x in row[i*3+3:i*3+6]),
                  "|",
                  " ".join(str(x) if x != 0 else "." for x in row[i*3+6:i*3+9]))

    def is_solved(self):
        return self.puzzle == self.solution

    def make_move(self, row, col, value):
        if self.original_puzzle[row][col] != 0:
            return False  # Нельзя изменить исходную цифру
            
        if 1 <= value <= 9:
            self.puzzle[row][col] = value
            return True
            
        return False