import urllib2


def main():


# Setup for Banggood version of 4 x 8x8 LED Matrix (https://bit.ly/2Gywazb)

    data = urllib2.urlopen("http://www.google.com").read(20000) # read only 20 000 chars
    data = data.split("\n") # then split it into lines

    for line in data:
        print line

if __name__ == "__main__":
        main()