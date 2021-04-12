from flask_wtf import FlaskForm
from wtforms.fields.simple import FileField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed

class UploadForm(FlaskForm):
    description = TextAreaField('Description',validators=[InputRequired()])
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
