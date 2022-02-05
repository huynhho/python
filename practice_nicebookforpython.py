##import collections
##Card = collections.namedtuple('Card', ['rank','suit'])
##
##class FrenchDeck:
##    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
##    suits = 'spades diamonds clubs hearts'.split()
##
##
##    def __init__(self):
##        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
##    def __len__(self):
##        return len(self._cards)
##    def __getitem__(self, position):
##        return self._cards[position]
##                                                

                                                  
                                                  
# Build a list of Unicode codepoints from a string 
##symbols = '!@#$%^&*'
##codes =[]
##setOfSymbols = []
##for symbol in symbols:
##    codes.append(ord(symbol))
##    setOfSymbols.append(symbol)
##print(codes)
##print(setOfSymbols)
    


##codes = [ord(symbol) for symbol in symbols if ord(symbol)>= 35]
##print('codes is:', codes)
##hoaniscute = tuple(ord(symbol) for symbol in symbols if ord(symbol)>=35)
##print('hoaniscute:', hoaniscute)
##
##
##import array
##print(array.array('I', (ord(symbol) for symbol in symbols if  ord(symbol)>=35)))

# Cartesian product using a list comprehension

##colors = ['black', 'white']
##sizes = ['S', 'M', 'L']
##tshirts = [(color, size) for size in sizes for color in colors ]
##print(tshirts)
##for size in sizes:
##    for color in colors:
##        print((color, size))
##colors = ['black', 'white']
##sizes = ['S', 'M', 'L']
##for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
##    print(tshirt)
##lax_coordinates = (33.9425, -118.408056)
##city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
##traveler_ids = [('USA', '31195855'), ('BRA', 'CE34256'), ('ESP', 'XDA205856')]
##for passport in sorted(traveler_ids):
##    print( '%s/%s' % passport)
##for country, hoan in traveler_ids:
##    print(country)

##metro_areas = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)), ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
##               ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)), ('New Your-Newark', 'US', 20.104, (40.808611, -74.020386)),
##               ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]
##print('{:15} | {:^9} |{:^9}'.format('', 'lat.', 'long.'))
##fmt = '{:15} | {:9.4f} |{:9.4f}'
##for name, cc, pop, (latitude, longitude) in metro_areas:
##    if longitude <= 0:
##        print(fmt.format(name, latitude, longitude))
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
#print(tokyo)
#metro_areas.items()
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi)
print(delhi._asdict())


