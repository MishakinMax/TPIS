import NumToWords.libs.converter
dir()
import phrases
dir()
help(phrases)
phrases.greetings.hello()

from phrases import greetings
dir()
dir(greetings)
greetings.morning()

from phrases.greetings import  hi
dir()
hi()
