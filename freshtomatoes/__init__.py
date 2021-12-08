import requests as rq
from bs4 import BeautifulSoup as bs


class FreshTomatoes:
    def __init__(self):
        self.base_url = "https://www.rottentomatoes.com/m/"
        self.info={}
    try:
        def Scores(self, name,year=None):
            space_name=name.replace(" ","_")
            if year!=None:
                url=self.base_url+space_name+"_"+str(year)
            else:
                url=self.base_url+space_name

            
            res = rq.get(url)
            soup = bs(res.text, "html.parser")
            rows = soup.select('score-board')
            # print(rows)
            for x in rows:
                self.info={"audiencescore":x.get('audiencescore'),"tomatometerscore":x.get('tomatometerscore')}
            return self.info
    except Exception as e:
        print(e)

