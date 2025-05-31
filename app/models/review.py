from app.utils import extract
class Review:

    review_schema = {
        "review_id": (None, 'data-entry-id'),
        "author": ("span.user-post__author-name",),
        "recomendation": ("span.user-post__author-recomendation > em",),
        "stars": ("span.user-post__score-count",),
        "content": ("div.user-post__text",),
        "pros": ("div.review-feature__item--positive", None, True),
        "cons": ("div.review-feature__item--negative", None, True),
        "likes": ("button.vote-yes > span",),
        "dislikes": ("button.vote-no > span",),
        "publish_date": ("span.user-post__published > time:nth-child(1)",'datetime'),
        "purchase_date": ("span.user-post__published > time:nth-child(2)",'datetime'),
    }

    def __init__(self, review_id="", author="", recomendation="", stars=0.0, content="", pros=[], cons=[], likes=0, dislikes=0, publish_date="", purchase_date=""):
        self.review_id = review_id
        self.author = author
        self.recomendation = recomendation
        self.stars = stars
        self.content = content
        self.pros = pros
        self.cons = cons
        self.likes = likes
        self.dislikes = dislikes
        self.publish_date = publish_date
        self.purchase_date = purchase_date
    
    def __str__(self):
        return "\n".join([f"{feature}: {getattr(self,feature)}"  for feature in self.review_schema.keys()])
    
    def to_dict(self):
        return {feature: getattr(self,feature)  for feature in self.review_schema.keys()}
    
    def extract_features(self, review):
        for key, value in self.review_schema.items():
              setattr(self, key, extract(review, *value))
        return self
    
    def transform(self):
        self.stars = float(self.stars.split("/")[0].replace(",", "."))
        self.likes = int(self.likes)
        self.dislikes = int(self.dislikes)
        return self