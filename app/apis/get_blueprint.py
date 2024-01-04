from sanic import Blueprint, Request
from sanic.response import json
from sanic_ext import openapi, validate
from sanic import Blueprint
from sanic.response import json

from databases.sparql import Sparql
sparql = Sparql()

bp = Blueprint('get_blueprint', url_prefix='/get')


@bp.get('/courses')
@openapi.tag("Get list")
@openapi.summary("Get all Courses")
async def get_courses(request):
    courses = sparql.get_courses()
    return json(courses)


@bp.get('/classes')
@openapi.tag("Get list")
@openapi.summary("Get all Classes")
async def get_classes(request):
    courses = sparql.get_courses()
    return json(courses)
