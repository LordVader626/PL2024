import re

def main(file_name):
    res = 0
    somador = False

    with open(file_name, 'r') as texto:
        for line in texto:
            on = '[Oo][Nn]'
            off = '[Oo][Ff][Ff]'
            num = '\d+'
            result = '='

            regex = f"(?P<on>{on})|(?P<off>{off})|(?P<num>{num})|(?P<result>{result})"

            matches = re.finditer(regex, line)

            for match in matches:
                if match.lastgroup == 'num':
                    if somador:
                        res += int(match.group('num'))
                        print(f"Soma: {match.group('num')}")
                elif match.lastgroup == 'on':
                    somador = True
                    print("Somador ON.")
                elif match.lastgroup == 'off':
                    somador = False
                    print("Somador OFF.")
                elif match.lastgroup == 'result':
                    print(f"Result: {res}")

if __name__ == '__main__':
    main('texto.txt')
