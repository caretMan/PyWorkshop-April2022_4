# Default Dict and Counter

text = '''I've become so numb
I can't feel you there
Become so tired
So much more aware
I'm becoming this
All I want to do
Is be more like me
And be less like you
And I know
I may end up failing too
But I know
You were just like me with someone disappointed in you'''

text_list = text.split()

# setdefault
freq_dict = {}
for word in text_list:
  freq_dict.setdefault(word, 0)
  freq_dict[word] += 1

print(freq_dict)
print(freq_dict['AAAAAAAAA'])  # KeyError / Not Added

index_dict = {}
for index, word in enumerate(text_list):
  index_dict.setdefault(word, []).append(index)

print(index_dict)

# default dict
from collections import defaultdict

freq_ddict = defaultdict(int)

for word in text_list:
  freq_ddict[word] += 1

print(freq_ddict)
print(freq_ddict['AAAAAAAAA'])  # No Error / Missing value is added
print(freq_ddict)  # See it added to Dict
  
freq_dict = defaultdict(list)

# Counter
from collections import Counter

freq_counter = Counter(text_list)

print(freq_counter)  # use it like normal dict
print(freq_counter.most_common)
print(freq_counter.most_common(2))
