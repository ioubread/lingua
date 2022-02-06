from googletrans import Translator
import pyperclip
import sys

# Initialisation
translator = Translator()

# Get the user's clipboard
userinput = pyperclip.paste()

# If an argument is supplied, assume the user wants to translate the content in their current clipboard to another language
# The argument should be the two-letter language code
if len(sys.argv) == 2:
    languageTo = sys.argv[1]
    pyperclip.copy((translator.translate(userinput, dest=languageTo)).text)

# If no language code (argument) was supplied, assume the user wants to translate the current clipboard contents to english
elif len(sys.argv) == 1:
    languageTo = "en"
    pyperclip.copy((translator.translate(userinput, dest=languageTo)).text)

# Language codes can be found on :
#   https://sites.google.com/site/opti365/translate_codes
#   https://gist.github.com/JT5D/a2fdfefa80124a06f5a9