from wtforms import Form, StringField, SubmitField, validators

class ProductForm(Form):
    product_id = StringField("Kod produktu", 
                            name='product_id', 
                            id='product_id',
                            validators=[
                                 validators.DataRequired(message="Kod produktu jest wymagany."),
                                 validators.Regexp("^[0-9]*$", message= "Kod produktu może zawierać jedynie cyfry."),
                                 validators.Length(min=5, max=10, message="Kod produktu musi mieć od 1 do 10 znaków."),
                             ])
    submit = SubmitField("Pobierz opinie")