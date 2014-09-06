import requests
import csv
from BeautifulSoup import BeautifulSoup
 
url = 'http://www.mutigers.com/sports/m-footbl/mtt/miss-m-footbl-mtt.html'
 
def get_players():
    # Open the HTML file and turn it into a BeautifulSoup object for parsing
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)
 
    #scrape part
    only_table = soup.find('table', id={'sortable_roster'})
 
    output_trs = []  # The list that's going to store all of our output rows
    column_titles = [th.text for th in only_table.find('thead').find('tr').findAll('th')]
    
 
    # First we need to loop through all the rows in the table, tr is table row
    for tr in only_table.findAll('tr'):
        # Get all headers in this row.
        ths = tr.findAll('th')
 
        # And next, we want to get all the cells within each of the rows, td is table cell, 
        tds = tr.findAll('td')
 
        # We'll store all of the values for each given row in a list
        output_tds = []
        for td in tds:
            # Delete annoying tab character
            output_tds.append(td.text.replace('&nbsp;', ''))
        
        if len(output_tds) == len(column_titles):
            row = dict()
            for idx, th in enumerate(column_titles):
                row[th] = output_tds[idx]
            # And we'll add that list to our broader list of results
            output_trs.append(row)
 
    # Finally, we'll write our results to a file
 
    return output_trs
 
if __name__=='__main__':
    print get_players()