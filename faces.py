#   # SMS EmojiConverter
import sys

def main():
    prompt = input('Type a message:')

    while True:
        try:
            if prompt.isdigit() or prompt.isalpha():
                raise ValueError("Use SMS language")

        except ValueError as e:
            sys.exit(e)
        
        else:
            break
  
    dictionary = {
        ':)': '\U0001F642', ':(': '\U0001F641', ':D': '\U0001F600',
        ':O': '\U0001F632', ':P': '\U0001F61B', ':|': '\U0001F610',
        ':*': '\U0001F618', ':3': '\U0001F617', ':x': '\U0001F621',
        ':/': '\U0001F615', ':@': '\U0001F620', ':S': '\U0001F616',
        ':$': '\U0001F633', ':!': '\U0001F631', ':#': '\U0001F635',
        ':&': '\U0001F636', ':;': '\U0001F61C', ':Z': '\U0001F612',
        ':L': '\U0001F61D', ':R': '\U0001F61E', ':C': '\U0001F61F',
        ':T': '\U0001F624', ':U': '\U0001F622', ':V': '\U0001F623',
        ':W': '\U0001F625', ':N': '\U0001F626', ':K': '\U0001F627',
        ':Y': '\U0001F628', ':Q': '\U0001F629', ':J': '\U0001F62A',
        ':G': '\U0001F62B', ':H': '\U0001F62C', ':I': '\U0001F62D',
        ':F': '\U0001F62E', ':B': '\U0001F62F', ':M': '\U0001F630',
        ':A': '\U0001F634', ':X': '\U0001F637', ':D': '\U0001F638',
        ':E': '\U0001F639', ':^': '\U0001F63A', ':+': '\U0001F63B',
        ':<': '\U0001F63C', ':>': '\U0001F63D', ':?': '\U0001F63E',
        ':[': '\U0001F640', ':]': '\U0001F641'
    }

    print(prompt.replace(prompt, dictionary[prompt]))


if __name__ == '__main__':
    main()
