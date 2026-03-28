class Parser:
    def __init__(self, file):
        self.file = file

    def get_dict(self):
        with open(self.file, encoding="utf-8") as sub:
            subtitle = []
            lines = sub.readlines()
            for i, line in enumerate(lines[:-1]):
                if "-->" in line:
                    start, end = line.split("-->")
                    start = start.strip()
                    end = end.strip().split(" ")[0]
                    text = lines[i+1].strip()
                    if text != "" and (subtitle == [] or subtitle[-1]["text"]!= text):
                        subtitle.append({"start": start, "end": end, "text": text})
            return subtitle