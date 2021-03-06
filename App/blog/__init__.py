from flask import Blueprint

from . import api, config, jinja
from .router import (
    ArticleListView,
    ArticleView,
    ArticleRssView,
    ArchiveView,
    TimeLineView,
)

site = Blueprint('blog', __name__, template_folder='templates')

site.add_url_rule(
    '/article',
    view_func=ArticleListView.as_view('articles'),
)
site.add_url_rule(
    '/article/<int:pk>',
    view_func=ArticleView.as_view('article'),
)
site.add_url_rule(
    '/rss',
    view_func=ArticleRssView.as_view('rss'),
)

archives = ArchiveView.as_view('archives')
site.add_url_rule(
    '/archives',
    view_func=archives,
)
site.add_url_rule(
    '/archives/<int:year>',
    view_func=archives,
)
site.add_url_rule(
    '/archives/<int:year>/<int:month>',
    view_func=archives,
)
site.add_url_rule(
    '/timeline',
    view_func=TimeLineView.as_view('timelines'),
)


def init_app(app):
    api.init_app(app)
    jinja.init_app(site)
    app.register_blueprint(site, subdomain=config.SUBDOMAIN)
