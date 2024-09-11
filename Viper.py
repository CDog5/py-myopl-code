import ViperLang as Viper
import sys
while True:
    text = input('Viper> ')
    if text.lower()=="exit" or text.lower() == "quit" or text.lower() == "close":
        sys.exit(0)
    result, error = Viper.run('ViperShell', text)

    if error: print(error.as_string())
    else: print(result)
