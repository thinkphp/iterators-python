class myContainer:

    def __init__(self, data):

        self.data = data

        self.len = len(data)

        self.index = self.len

    def __iter__(self):

         return self

    def __next__(self):

         if self.index == 0:

             raise StopIteration

         self.index -= 1

         return self.data[ self.index ]

class myPrimes:

     def __init__( self, n ):

         self.n = n

         self.index = -1

         self.data = self.aggregateData(n)

         self.len = len(self.data)

     def __iter__(self):

         return self

     def isPrime(self,n):

        #first statement
        prime = True
        #second statement
        i = 2
        #third statement
        while i * i <= n and prime is True:
              prime = n % i != 0
              i += 1
        #return value
        return prime

     def aggregateData(self,n):

         list = []

         for i in range(2, n + 1):

             if self.isPrime(i):

                 list.append(i)

         return list

     def __next__(self):

        if self.index >= self.len - 1:
             raise StopIteration

        self.index += 1

        return self.data[ self.index ]

def main():

    ob = myPrimes(100)

    result = [x for x in ob]

    print(result)

    ob2 = myContainer("spam")

    result2 = [x for x in ob2]

    print(result2)

main()
