class Puzzle:
    def __init__(self):
        self.riddles = [
            {
                "question": "Что можно сломать, даже не трогая и не видя?",
                "options": ["Сердце", "Обещание", "Секрет", "Мысль"],
                "answer": "Обещание"
            },
            {
                "question": "Чем больше вы берете, тем больше вы оставляете позади. Что это?",
                "options": ["Деньги", "Следы", "Время", "Шаги"],
                "answer": "Шаги"
            },
            {
                "question": "Что принадлежит вам, но другие используют это чаще, чем вы?",
                "options": ["Имя", "Телефон", "Дом", "Одежда"],
                "answer": "Имя"
            }
        ]
        self.current_riddle = random.choice(self.riddles)
        self.solved = False
    
    def display(self):
        """Отображает загадку и варианты ответов"""
        print("\n" + "=" * 80)
        print("ЗАГАДКА:")
        print(self.current_riddle["question"])
        print("\nВарианты ответов:")
        for i, option in enumerate(self.current_riddle["options"], 1):
            print(f"{i}. {option}")
        print("=" * 80)
    
    def check_answer(self, answer):
        """Проверяет ответ игрока"""
        try:
            choice = int(answer)
            if 1 <= choice <= len(self.current_riddle["options"]):
                selected = self.current_riddle["options"][choice-1]
                if selected == self.current_riddle["answer"]:
                    self.solved = True
                    return True, "Правильно!"
                return False, "Неправильно! Попробуйте еще раз."
        except ValueError:
            pass
        return False, "Недопустимый выбор. Попробуйте еще раз."
    
    def is_solved(self):
        return self.solved