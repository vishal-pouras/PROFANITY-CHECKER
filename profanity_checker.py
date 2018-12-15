import urllib

def read_text():
    fh = open("movie_quotes.txt", "r")
    contents = fh.read()
    print(contents)
    fh.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    if output=='true':
        print("Cuss words are present")
    else:
        print("No cuss words!!!")
    connection.close()

read_text()