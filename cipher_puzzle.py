import random
from string import ascii_uppercase

class Puzzle:
    def __init__(self, difficulty="medium"):
        self.difficulty = difficulty
        self.message, self.solution, self.cipher_type = self.generate_puzzle()
        self.attempts = 0
        self.max_attempts = 5 if difficulty == "hard" else 10
        
    def generate_puzzle(self):
        # Генерируем сообщение и ключ
        messages = [
            "ПОИЩИТЕ В ВОСТОЧНОЙ СТЕНЕ",
            "КЛЮЧ СПРЯТАН ПОД КАМНЕМ",
            "ТАЙНАЯ КОМНАТА ЗА КАРТИНОЙ",
            "ОТВЕТ НАЙДЕТЕ В КНИГЕ",
            "ПРОХОД ОТКРОЕТСЯ НОЧЬЮ"
        ]
        message = random.choice(messages).replace(' ', '')
        
        # Выбираем тип шифра в зависимости от сложности
        if self.difficulty == "easy":
            cipher_type = "shift"
            shift = random.randint(1, 5)
            solution = self.caesar_cipher(message, shift)
            return solution, shift, cipher_type
            
        elif self.difficulty == "medium":
            cipher_type = "substitution"
            key = self.generate_substitution_key()
            solution = self.substitution_cipher(message, key)
            return solution, key, cipher_type
            
        else:  # hard
            cipher_type = "vigenere"
            keyword = random.choice(["KEY", "SECRET", "HIDDEN", "CODE"])
            solution = self.vigenere_cipher(message, keyword)
            return solution, keyword, cipher_type
    
    def caesar_cipher(self, text, shift):
        result = ""
        for char in text:
            if char in ascii_uppercase:
                idx = (ascii_uppercase.index(char) + shift) % 26
                result += ascii_uppercase[idx]
            else:
                result += char
        return result
    
    def generate_substitution_key(self):
        alphabet = list(ascii_uppercase)
        random.shuffle(alphabet)
        return ''.join(alphabet)
    
    def substitution_cipher(self, text, key):
        result = ""
        for char in text:
            if char in ascii_uppercase:
                idx = ascii_uppercase.index(char)
                result += key[idx]
            else:
                result += char
        return result
    
    def vigenere_cipher(self, text, keyword):
        result = ""
        keyword_repeated = (keyword * (len(text) // len(keyword) + 1))[:len(text)]
        for i, char in enumerate(text):
            if char in ascii_uppercase:
                shift = ascii_uppercase.index(keyword_repeated[i])
                idx = (ascii_uppercase.index(char) + shift) % 26
                result += ascii_uppercase[idx]
            else:
                result += char
        return result
    
    def display(self):
        print(f"Зашифрованное сообщение: {self.message}")
        print(f"Тип шифра: {self.get_cipher_name()}")
        print(f"Попыток осталось: {self.max_attempts - self.attempts}")
        
        if self.cipher_type == "shift":
            print("Это шифр Цезаря. Введите ключ (число от 1 до 25):")
        elif self.cipher_type == "substitution":
            print("Это шифр замены. Введите алфавит замены (26 букв):")
        else:  # vigenere
            print("Это шифр Виженера. Введите ключевое слово:")
    
    def get_cipher_name(self):
        names = {
            "shift": "Шифр Цезаря",
            "substitution": "Шифр замены",
            "vigenere": "Шифр Виженера"
        }
        return names.get(self.cipher_type, "Неизвестный шифр")
    
    def handle_input(self, input_str):
        self.attempts += 1
        
        try:
            if self.cipher_type == "shift":
                key = int(input_str)
                decrypted = self.caesar_cipher(self.message, -key)
                return decrypted == self.solution
                
            elif self.cipher_type == "substitution":
                if len(input_str) != 26 or not input_str.isalpha():
                    return False
                decrypted = ""
                for char in self.message:
                    if char in ascii_uppercase:
                        idx = input_str.index(char)
                        decrypted += ascii_uppercase[idx]
                    else:
                        decrypted += char
                return decrypted == self.solution
                
            else:  # vigenere
                decrypted = self.vigenere_cipher(self.message, input_str.upper(), decrypt=True)
                return decrypted == self.solution
                
        except Exception:
            return False
    
    def is_solved(self):
        return self.attempts < self.max_attempts and self.handle_input.solved
    
    def vigenere_cipher(self, text, keyword, decrypt=False):
        result = ""
        keyword_repeated = (keyword * (len(text) // len(keyword) + 1))[:len(text)]
        for i, char in enumerate(text):
            if char in ascii_uppercase:
                shift = ascii_uppercase.index(keyword_repeated[i])
                if decrypt:
                    idx = (ascii_uppercase.index(char) - shift) % 26
                else:
                    idx = (ascii_uppercase.index(char) + shift) % 26
                result += ascii_uppercase[idx]
            else:
                result += char
        return result