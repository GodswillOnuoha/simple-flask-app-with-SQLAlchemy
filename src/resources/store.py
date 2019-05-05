from flask_restful import Resource, reqparse
from models.store import Store as StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found.'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "Store with name '{}' already exists".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save()
        except:
            return {'message': 'An error occurred while creating store'}, 500
        
        return store.json(), 201

    def delete(self, name):
        store =  StoreModel.find_by_name(name)
        if store:
            store.delete()
        return {'message': 'store deleted'}
        
    
class StoreList(Resource):
    def get(self):
        stores = [store.json() for store in StoreModel.query.all()]
        return {'stores': stores}