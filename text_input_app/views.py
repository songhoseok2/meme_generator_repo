from django.shortcuts import render
from flickrapi import FlickrAPI

def ask_text(request, keyword):

    FLICKR_PUBLIC = '62fc03e54fbf6e29d42cb66de850a66b'
    FLICKR_SECRET = '5247f1bd66733dd9'

    flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
    searched_photos = flickr.photos.search(text=keyword)
    photos_container = searched_photos['photos']['photo']
    list_of_urls = []

    for photo in photos_container:
        farm_id = photo['farm']
        server_id = photo['server']
        photo_id = photo['id']
        secret = photo['secret']

        if farm_id is not 0 and server_id is not 0:
            url = 'https://farm' + str(farm_id) + '.staticflickr.com/' + str(server_id) + '/' + str(photo_id) + '_' + str(secret) + '.jpg'
            list_of_urls += [url]

    url_dict = []
    for url in list_of_urls:
        url_dict += [{'url': url}]

    context = {
        'url_dict': url_dict,
        'keyword': keyword
    }

    return render(request, 'text_input_app/text_input_page.html', context)
