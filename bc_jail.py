import mechanize
import requests
import csv
from BeautifulSoup import BeautifulSoup
 
url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
 
def get_inmates():
    # Open the HTML file and turn it into a BeautifulSoup object for parsing
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)
 
    #scrape part
    only_table = soup.find('table', attrs={'class': 'resultsTable'})
 
    output_trs = []  # The list that's going to store all of our output rows
    column_titles = []
 
    # First we need to loop through all the rows in the table
    for tr in only_table.findAll('tr'):
        ths = tr.findAll('th')
        if len(ths) > 0:
            column_titles = [th.text for th in ths]
            
            continue
 
        # And next, we want to get all the cells within each of the rows
        tds = tr.findAll('td')
 
        # We'll store all of the values for each given row in a list, think of output_row 
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
    print get_inmates()

    ##