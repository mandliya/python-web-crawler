from scrapy.item import Item, Field

class LivingSocialDeal(Item):
    '''
      Livingsocial container (dictionary-like object) for scrapped data
      LivingSocialDeal inherits from Item class, which basically takes
      some takes some pre-defined object which scrapy has just built for it
    '''
    title = Field()
    link  = Field()
    location = Field()
    original_price = Field()
    price = Field()
    end_date = Field()
