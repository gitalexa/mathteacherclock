import urllib2


def main():
    data = urllib2.urlopen("https://raw.githubusercontent.com/gitalexa/mathteacherclock/master/clock.ini").read(20000) # read only 20 000 chars
    data = data.split("\n") # then split it into lines

    for line in data:
        print line

if __name__ == "__main__":
        main()