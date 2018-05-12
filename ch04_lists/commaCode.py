spam = ['apples', 'bananas', 'tofu', 'cats']

def list_thing(words):
     if len(words) == 1:
         return words[0]
     return '{} and {}'.format(', '.join(words[:-1]), words[-1])

print list_thing(spam[:1])

print map(''.join, zip(*spam))