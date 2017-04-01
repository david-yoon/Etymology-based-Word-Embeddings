import os
import codecs

list_file = os.listdir('raw_crawl')
len(list_file)


f = codecs.open('chinesetools_synonym_merge', 'w', encoding='utf-8')

for f_name in list_file:
    print f_name
    with codecs.open('raw_crawl/' + f_name,'r', encoding='utf-8') as tmp_f:
        for line in tmp_f:
            f.write(line)