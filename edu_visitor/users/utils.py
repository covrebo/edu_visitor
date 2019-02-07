import os
import secrets
from PIL import Image
from flask import url_for
from edu_visitor import app, mail
from flask_mail import Message

# Function to save a new profile picture submission form the user - used in the update account form
def save_picture(form_picture):
    # Randomize the file name to avoid conflicts in the file system
    random_hex = secrets.token_hex(8)
    # Get the filname and file extension of the submitted file
    _, f_ext = os.path.splitext(form_picture.filename)
    # Combine the random hex string and file extension to create a new name for the submitted picture file
    picture_file_name = random_hex + f_ext
    # Create the path to the folder where the image will be stored
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_file_name)
    # Resize the picture before saving it
    output_size = (125,125)
    resized_image = Image.open(form_picture)
    resized_image.thumbnail(output_size)
    # Save the resized image to the file system
    resized_image.save(picture_path)
    # Pass the new name of the file back so it can be used to update the database entry for the user
    return picture_file_name


# A function to compose an email to send a reset password link to
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='visitors@isd508.org', recipients=[user.email])
    msg.body = f'''To reset your password visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request, ignore this email and no changes will be made.
'''
    mail.send(msg)