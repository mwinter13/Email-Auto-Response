#! Python3

import sys, pyperclip

TEXT = {'agree':'''Yes!  I agree.  That sounds good to me''',
'busy':'''Sorry, can we do this later in the week?''',
'upsell':'''Would you consider making a monthly donation?'''}

if len(sys.argv) < 2:
    print('Usage: python emailAutoResponses.py [keyphrase] copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]  #the first command line argument is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Your text ' + keyphrase + ' has been copied to the clipboard')
else:
    print('Sorry, there is no text for ' keyphrase)