import urllib.request as urllib

def main(url):
    print("checking connectivity")

    response = urllib.urlopen(url)
    print("connected to ", url, "successfully")
    print("the response code was: ", response.getcode())

print("site connectivity checker")
inputUrl = input("input URL")

main(inputUrl)
