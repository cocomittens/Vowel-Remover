word_list = ["cat", "glasses", "headband", "stars", "oblique", "black", "semicolon", "blue", "pink", "purple", "table", "mouse", "mittens", "bright"]
devoweled_list = []
vowels = ('a', 'e', 'i', 'o', 'u')

def show_list(list):
  count = 1
  for word in list:
    print("{}".format(word))
    count += 1

for word in word_list:
  new_word = ""
  new_word = ''.join([l for l in word if l not in vowels])
  new_word = new_word.capitalize();
  devoweled_list.append(new_word)
  
show_list(devoweled_list)