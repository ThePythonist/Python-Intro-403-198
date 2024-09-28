lines = open("words.txt").read().split("\n")
open("oneline_words.txt", "w").writelines(lines)
