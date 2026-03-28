class Practice:
    def __init__(self, subtitles):
        self.current_index = 0
        self.subtitles = subtitles

    def run(self):
        print("按enter繼續,輸入q結束")
        while self.current_index < len(self.subtitles):
            print(self.subtitles[self.current_index]["text"])
            user_input = input()
            if user_input == "q":
                print("逐字稿請稍候")
                break
            else:
                self.current_index += 1