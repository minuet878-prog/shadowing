from downloader import Downloader
from parser import Parser
from practice import Practice

def main():
    url = input("URL: ")
    d = Downloader(url)
    path = d.get_sub()
    p = Parser(path)
    subtitles = p.get_dict()
    c = Practice(subtitles)
    c.run()

if __name__ == "__main__":
    main()
