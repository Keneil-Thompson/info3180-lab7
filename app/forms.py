from flask_wtf import FlaskForm
from wtforms.fields.simple import FileField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed

class UploadForm(FlaskForm):
    description = TextAreaField('Description',validators=[DataRequired()])
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
