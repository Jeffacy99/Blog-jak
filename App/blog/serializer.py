from flask_maple.serializer import Serializer


class ArticleSerializer(Serializer):
    class Meta:
        exclude = ["user", "user_id"]
        extra = ["htmlcontent"]
