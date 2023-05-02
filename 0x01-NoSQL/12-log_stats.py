#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_db = client.logs.nginx

    count_docs = len(list(nginx_db.find()))
    count_get = nginx_db.count_documents({'method': 'GET'})
    count_post = nginx_db.count_documents({'method': 'POST'})
    count_put = nginx_db.count_documents({'method': 'PUT'})
    count_patch = nginx_db.count_documents({'method': 'PATCH'})
    count_delete = nginx_db.count_documents({'method': 'DELETE'})
    count_status_path = nginx_db.count_documents({'path': '/status'})

    print('{} logs'.format(count_docs))
    print('methods:')
    print('\tmethod GET: {}'.format(count_get))
    print('\tmethod POST: {}'.format(count_post))
    print('\tmethod PUT: {}'.format(count_put))
    print('\tmethod PATCH: {}'.format(count_patch))
    print('\tmethod DELETE: {}'.format(count_delete))
    print('{} status check'.format(count_status_path))
