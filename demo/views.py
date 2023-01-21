from rest_framework.response import Response
from rest_framework.decorators import api_view
import json, pymongo

@api_view(["GET"])
def simpleRequest(request):
    sr = {
        "name" : "prachi"
    }
    return Response(sr)

@api_view(["POST"])
def postRequest(request):
    pr = request.data
    sr = {
        "anything" : "anystring hello {} howru".format(pr["name"])
    }
    return Response(sr)

@api_view(["POST"])
def figureOut(request):
    pr = request.data
    client = pymongo.MongoClient("mongodb+srv://buttercup:buttercup@cluster0.bdqacl5.mongodb.net/?retryWrites=true&w=majority")
    db = client.sample_mflix["comments"]
    cursor = db.find({"name" : pr["name"]})
    #for document in cursor:
    #     print(document)
    result = {"resultData":[{"name": x['name'], 'email': x['email'], 'txt': x['text']} for x in cursor]}
    return Response(result)

@api_view(["POST"])
def airplane(request):
    pr = request.data
    client = pymongo.MongoClient("mongodb+srv://buttercup:buttercup@cluster0.bdqacl5.mongodb.net/?retryWrites=true&w=majority")
    db = client.sample_training["routes"]
    cursor = db.find({"airplane" : pr["name"]})
    #for document in cursor:
    #     print(document)
    result = {"resultData":[{"name": x['airplane'], 'source': x['src_airport'], 'dest': x['dst_airport'], "airline":x['airline']['name']} for x in cursor]}
    return Response(result)
    
@api_view(["GET"])
def sourceairport(request):
    client = pymongo.MongoClient("mongodb+srv://buttercup:buttercup@cluster0.bdqacl5.mongodb.net/?retryWrites=true&w=majority")
    db = client.sample_training["routes"]
    srcValue = request.GET.get('src')
    cursor = db.find({"src_airport" : srcValue})
    result = {"resultData":[{"name": x['airplane'], 'source': x['src_airport'], 'dest': x['dst_airport'], "airline":x['airline']['name']} for x in cursor]}
    return Response(result)

