phrase =  str(input('Enter the phrase.\n')).strip().upper()
words = phrase.split()
nospace = ''.join(words)
invert = ''
#invert = nospace[::-1]
print('You sent this phrase:\n{}'.format(nospace))
for lyric in range(len(nospace) -1, -1, -1):
#    print(nospace[lyric])
    invert = invert + nospace[lyric]
print(nospace, invert)
if nospace == invert:
    print('\nThe inverse of {} is the same.'.format(nospace))
else:
    print('\nThe inverse of {} is not the same.'.format(nospace))