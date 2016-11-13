# pull in quality data from Wikimedia
from paws.EpochFail import wikiquality as wq
import json
import configparser

def get_page_quality(page_id_set):
    page_by_month = {} 
    for i in wq.read_aq('en'):
        if i['page_id'] in page_id_set:
            if i['page_id'] not in page_by_month:
                page_by_month[i['page_id']] = {}
            time = i['timestamp']
            new_val = dict(i)
            del new_val['timestamp']
            del new_val['page_id']
            page_by_month[i['page_id']][time] = new_val
    return page_by_month
                
def get_page_ids(category, file_name):
    page_id_set = set()
    generator = wq.read_page_ids(category)
    for page in generator:
        page_id_set.add(page['page_id'])
    with open(file_name, 'w') as f:
        for page_id in page_id_set:
            f.write(str(page_id) + '\n')
    return page_id_set


def save_to_disk(category_quality_dict, file_name):
    with open(file_name,'w') as f:
        json.dump(category_quality_dict,f)
        

def main():
    config = configparser.ConfigParser()
    config.read('settings.cfg')
    category = config.get('default', 'category')
    filename = config.get('default', 'filename')
                     
    page_ids = wq.read_page_ids(category)
    page_quality = get_page_quality(page_ids)
    save_to_disk(page_quality, filename)
    

if __name__ == "__main__":
    main()
    