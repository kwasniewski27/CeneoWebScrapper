from wtforms import Form, StringField, SubmitField, validators

class ProductForm(Form):
    def __init__(self):
        product_id = StringField("Identyfikator produktu", 
                                 name='product_id', 
                                 id='product_id',
                                 validators=[
                                     validators.DataRequired()
                                 ])
        submit = SubmitField("Pobierz opinie")