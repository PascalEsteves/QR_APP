from flask.views import MethodView
from flask_smorest import Blueprint, abort
from src.schemas.schemas import StoreSchema
from src.models.database import db
from src.models.models import StoreModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blb = Blueprint(
    "Store",
    __name__,
    description="Operation on Stores")

blb.route("/store/<int:store_id>")
class Store(MethodView):

    @blb.response(200, StoreSchema)
    def get(self, store_id):
        """
        Get information about store
        Args:
            :params store_id - Store unique id
        """
        store = StoreModel.query.get_or_404(store_id)
        return store
    def delete(self, store_id):
        """Delete a specific store"""
        store = StoreModel.query_get_or_404(store_id)
        db.session.delete(store)
        db.commit()
        return {"message":"Store successfully deleted"},200

blb.route("/store")
class StoreList(MethodView):

    @blb.response(200, StoreSchema(many=True))
    def get(self):
        """
        Get all the stores in database
        Args:
            :params None
        Return
            List of stores
        """
        return StoreModel.query.all()

    @blb.arguments(StoreSchema)
    @blb.response(201, StoreSchema)
    def post(self, store_data: dict):
        """
        Add New store to database
        Args:
            :params store data
        Return
            store
        """
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()

        except IntegrityError:
            abort(400, message="A store with that name already exists")

        except SQLAlchemyError:
            abort(500, message = "An error occurred creating the store.")

        return store
