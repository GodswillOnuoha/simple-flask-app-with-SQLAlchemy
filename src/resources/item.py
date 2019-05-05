from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import Item as ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help='This field can not be left blank'
    )

    parser.add_argument('store_id',
        type=float,
        required=True,
        help='store_id can not be blank'
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists".format(name)}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        
        try:
            item.save()
        except:
            return {'message': 'An error occurred inserting the item'}, 500

        return item.json(), 201
    
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete()

        return {'message': 'item deleted'}
    
    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item:
            item.price = data['price']
        else:
            item =  ItemModel(name, **data)
        
        item.save()

        return item.json()


class ItemList(Resource):
    def get(self):
        items = [item.json() for item in ItemModel.query.all()]
        return {'items': items}, 200