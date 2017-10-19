import hashlib, requests
import time, json

base_url = 'https://gateway.marvel.com/v1/public/'
k_priv = 'fdf9c8bc5c83cbe565fdd6ddc4df9d0fb1e38a83'
k_pub = '7f39855a0661b5fe55f842d7afa8cd9f'

def compute_hash():
    m = hashlib.md5()
    ts = str(time.time())
    m.update(ts.encode('utf-8'))
    m.update(k_priv.encode('utf-8'))
    m.update(k_pub.encode('utf-8'))
    h = m.hexdigest()
    return (ts, h)
 

def marvel_get(endpoint, params=None):
    ts, h = compute_hash()
    data = {'ts':ts, 'hash': h, 'apikey': k_pub}
    if params:
        data.update(params)
    return requests.get(base_url+endpoint, params=data)

import pprint as pp
for offset in range(0, 2000, 20):

    r = marvel_get('series', {'offset':str(offset)})

    d = json.loads(r.text)
    
    for comic_keys, comic_data in d['data'].items():
        if comic_keys == 'results':
            #pp.pprint(comic_data)
            for comic in comic_data:
                if comic['id'] != "":
                    for comic_attr_keys, comic_attr in comic.items():
                        if comic_attr_keys == 'id':
                            id_name = str(comic_attr)
                            print('ID: ' + id_name)
                        elif comic_attr_keys == 'title':
                            title = comic_attr.encode('utf-8')
                            print('Title: ' + title)
                        elif comic_attr_keys == 'thumbnail':
                            path = str(comic_attr['path'])
                            for v in path.split('/'):
                                if v == 'image_not_available':
                                    path = None

                            if path != None:
                                path = path + '.' + comic_attr['extension']
                        elif comic_attr_keys == 'description':
                            descr = comic_attr
                            if descr == None:
                                descr = "None"
                            else:
                                descr = comic_attr.encode('utf-8')
                            print('Description: ' + descr)
                        elif comic_attr_keys == 'characters':
                            char_list = []
                            items = comic_attr['items']
                            for chars in items:
                                char_list.append(chars['name'].encode('utf-8'))
                            print('Characters: ')
                            print(char_list)
                        elif comic_attr_keys == 'startYear':
                            year = str(comic_attr)
                            print("Year: " + year)
                        elif comic_attr_keys == 'creators':
                            creator_list = []
                            items = comic_attr['items']
                            for create in items:
                                creator_list.append(create['name'].encode('utf-8'))
                            print('Creators: ')
                            print(creator_list)
                        elif comic_attr_keys == 'events':
                            # Events have their own dict to go through
                            event_list = []
                            items = comic_attr['items']
                            for event in items:
                                event_list.append(event['name'].encode('utf-8'))
                            print('Events: ')
                            print(event_list)
                        print('\n')
    
