
from sqlalchemy import func
from maple.extension import db
from .db import Category, Article, Tag


class Archives:
    def categories():
        ins = db.session.query(Category, func.count(Article.id)).outerjoin(
            Category.articles).group_by(Category.id)
        return ins

    def tags():
        ins = db.session.query(Tag, func.count(Article.id)).outerjoin(
            Tag.articles).group_by(Tag.id)
        return ins


def init_app(app):
    # site.add_app_template_filter()
    app.add_app_template_global(Archives)
