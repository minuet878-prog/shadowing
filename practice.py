class Practice:
    def __init__(self, subtitles):
        self.current_index = 0
        self.subtitles = subtitles

    def run(self):
        while self.current_index < len(self.subtitles):
            print(self.subtitles[self.current_index]["text"])
            input()
            self.current_index += 1