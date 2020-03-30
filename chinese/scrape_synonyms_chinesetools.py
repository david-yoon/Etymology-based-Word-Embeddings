'''
date  : 2017. 04. 01
author: dato
where : SNU milab
what  : crawl synonym data from "chinesetool.eu" web page
        use chinese dictionary data as query words
'''
from bs4 import BeautifulSoup
import urllib
import networkx as nx
import codecs
import argparse
import csv
import chardet


def run_code():

    print ( "process from {} to {}".format(args.start, args.end) )
    
    G = nx.read_graphml('../data/graphs/chinese_graph.graphml', unicode)
    words = list(G.node[a]['chinese'] for a in G.node.keys() if 'chinese' in G.node[a])

    base_url = "https://www.chinesetools.eu/tools/synonym/"

    def url_encoding(data) :
        tmp = ''
        for i in xrange( len(data) ):
            tmp = tmp + '&#' + str(ord(data[i])) + ';'

        return urllib.quote(tmp)


    #f = codecs.open('chinesetools_synonym_' + str(args.start) + '-' + str(args.end) + '.csv','w', encoding='utf-8')
    f = codecs.open('chinesetools_synonym_' + str(args.start) + '-' + str(args.end) + '.csv','wb')
    writer = csv.writer(f, delimiter=',')
    
    syn_counter = 0
    index = 0
        
    for i in xrange(len(words)):
        
        index = i + args.start
        w = words[index]

        if index > args.end:
            break    
            
        print str(index) + "/" + str(args.end) + " target:  " + w        

        query = base_url + '?q=' + url_encoding(w) + '&Submit=Search'
        r = urllib.urlopen(query)
        soup = BeautifulSoup(r, 'lxml')

        parse = soup.find_all('div', 'arrondi_10')

        if ( len(parse) < 2 ):
            continue

        # find the 'divs' which contain the synonym 
        divs = parse[1].find_all('div')

        # check if the html has synonyms 
        inner_finder = -1

        for i, dv in enumerate(divs):
            if dv.string == 'Click on the synonyms to see it on the Chinese dictionary:' :
                inner_finder = i

        if inner_finder is -1:
            continue            

        # grap synonym information
        for dv in divs[inner_finder + 1].find_all('div'):
            for a in dv.find_all('a'):
                print 'syn : ' + a.string.strip()
                writer.writerow( [ unicode(w).encode('utf-8').strip(), unicode(a.string).encode('utf-8').strip() ] )
                syn_counter = syn_counter + 1
                break

    f.close()


    #with codecs.open('chinesetools_synonym.csv','w', encoding='utf-8') as f:
    #    for item in syn_pairs:
    #        print item[0]
    #        f.write("%s\n" % item[0])


if __name__ == '__main__':

    p = argparse.ArgumentParser()
    p.add_argument('--start', type=int, default=0)
    p.add_argument('--end', type=int, default=0)
    args = p.parse_args()
    
    run_code()
