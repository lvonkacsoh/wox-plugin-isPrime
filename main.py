# encoding=utf8
from wox import Wox


class Main(Wox):
    def isPrime(self, number):
        if number % 2 == 0:
            return False
        # start at 3 and only check odd number up to sqrt(n)+1
        for i in range(3, int(number**0.5)+1, 2):
            if number % i == 0:
                return False
        return True

    def getNumberValue(self, text):
        try:
            return (True, int(text))
        except ValueError:
            return (False, text)

    # part of the Wox lifecycle, 'key' is a single string of whatever you type after "isPrime "
    def query(self, key):
        if len(key) == 0:
            return

        results = []
        numbers = key.split(" ")
        for number in numbers:
            subTitle = ""
            isNumber, value = self.getNumberValue(number)
            if isNumber:
                isPrime = self.isPrime(value)
                title = "{} is {}a prime.".format(
                    value, "" if isPrime else "not ")
                img = "success" if isPrime else "failure"
            else:
                title = "ERROR: \"{}\" is not an integer!".format(value)
                subTitle = "Note: numbers like 18.4 or 17,1 are no integers."
                img = "failure"
            # these are the items which are finally shown in the result list
            results.append({
                "Title": title,
                "SubTitle": subTitle,
                "IcoPath": "Images/{}.png".format(img),
                "JsonRPCAction": {  # actually no clue what this is, leaving it in for now..
                    "dontHideAfterAction": True
                }
            })

        return results


# part of the Wox lifecycle, entry point
if __name__ == "__main__":
    Main()
