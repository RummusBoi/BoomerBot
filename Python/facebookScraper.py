import facebook
import scrapy

token = "EAAgBKQHwJYIBAKgBNsCdZBvjM7l2Pz5d9ypZA1gXWTT6NcWWET6JSpVnr7y0bhTiBdnqlGc46w98aNhmpy9rgCBrvjlYz6dOaQmDZCC4utfFXtLeJ4AcOPCghGRZBdddHnhPhuUwihDEiJDDv3oabsurQVgECGKzpDcOmyUuH5PC4zu4ZCfhrAZCOEs2jrvnuZAuoqBLbi2rQZDZD"

# Main function 
def main():
    graph = facebook.GraphAPI(access_token=token, version=2.12)
    
    post_ids = ['post_id_1', 'post_id_2']
    posts = graph.get_objects(ids=post_ids, fields="created_time")

    facebook.GraphAPI()

    for post in posts:
        print(post['created_time'])

# Testing feature
def test():
    graph = facebook.GraphAPI(access_token=token, version=2.12)
    fields = ["id", "name"]
    fields = ",".join(fields)
    page = graph.get_object(id="ekstrabladet", fields=fields)

    print(page)

test()