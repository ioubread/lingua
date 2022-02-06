-------
|ABOUT|
-------
-> Instantly translate text you copied onto your clipboard to/from english
-> Useful for on-the-spot translation
-> You could just browse google translate for this, but it's particularly useful if you also need to translate your reply on the spot to the target language
-> Personally, I prepare this program to be ready to be used at a notice by linking this program (and to-be-supplied arguments) with a .bat program so I can run it from Win+R (Windows RUN programme)

--------------
|DEPENDENCIES|
--------------
googletrans==3.1.0a0
pyperclip==1.8.2

-------
|USAGE|
-------
When running the program, the arguments depend on your intention:
	-> Translating TO English: No arguments required, just copy your target text onto your clipboard and run the program
	-> Translating FROM English to target language: Supply the two-letter code as your sole argument.

Either way, the program output will be copied back to your clipboard. (Note: If you need to preserve your original clipboard contents, it'll be lost in the process, so paste it somewhere for yourself.)

Language codes can be found on :
  https://sites.google.com/site/opti365/translate_codes
  https://gist.github.com/JT5D/a2fdfefa80124a06f5a9