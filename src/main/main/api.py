from ninja import NinjaAPI, Schema
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController 
from ninja_jwt.authentication import JWTAuth 

import helpers

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router("/waitlist/", "waitlist.api.router")


class UserSchema(Schema):
    username : str 
    is_authenticated : bool
    # is not request.user.is_Authenticated
    email : str = None


@api.get("/hello")
def hello(request):
    print(request)
    return {"message": "Hello World"}

@api.get("/me", response=UserSchema, auth=helpers.api_auth_user_required)
def me(request):
    print(request)
    return request.user