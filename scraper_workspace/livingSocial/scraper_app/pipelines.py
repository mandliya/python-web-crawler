from sqlalchemy.orm import sessionmaker
from models import Deals,db_connect, create_deals_table

class LivingSocialPipeline(object):
    """Living Social Pipeline for storing scraped data to database"""
    def __init__ (self):
        """
        Initializes database connection and sessionmaker
        Creates deals tables
        """
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item (self, item, spider):
        """
        Save deals in database .
        This method is called for every item pipepline component
        """
        session = self.Session()
        deal = Deals(**item)
        try:
            session.add(deal)
            session.commit()
        except:
            session.rollback();
            raise
        finally:
            session.close()

        return item
