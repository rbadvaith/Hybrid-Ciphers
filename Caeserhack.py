message = input("Enter Encrypted Message")#encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = 'abcdefghijklmnopqrstuvwxyz'

for key in range(len(LETTERS)):
   translated = ''
   for symbol in message:
      if symbol in LETTERS:
         num = LETTERS.find(symbol)
         num = num - key
         if num < 0:
            num = num + len(LETTERS)
         translated = translated + LETTERS[num]
      elif symbol in letters:
         num = letters.find(symbol)
         num = num - key
         if num < 0:
            num = num + len(letters)
         translated = translated + letters[num]         
      else:
         translated = translated + symbol
   print('Hacking key #%s: %s' % (key, translated))
