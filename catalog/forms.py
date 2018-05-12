from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Story
from PIL import Image
from django.core.files import File


class NewStoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'story', 'photo', 'photo_height', 'photo_width', 'top', 'left']#, 'orientation'] heroku test

    #this function allows us to crop the image to a desired width and Height
    #shoud change this out with use input to customize exact picture desired.
    def save( self ):
        story = super(NewStoryForm, self).save()

        backup_image = Image.open( story.photo )
        backup_image.save(  "media/image/backup_story_photo/" + story.title + ".png")

        img = Image.open( story.photo )

        # img = img.rotate(-90*float(story.orientation), expand=True) heroku test

        natural_image_width, natural_image_height = img.size
        image_height = float(story.photo_height)
        image_width = float(story.photo_width)
        image_top = float(story.top)
        image_left = float(story.left)
        ratio_height = natural_image_height/image_height
        ratio_width = natural_image_width/image_width

        view_height = 100
        view_width = 162
        container_height = 300
        container_width = 300
        top = (container_height - view_height)/2 - image_top
        left = (container_width - view_width)/2 - image_left
        bottom = top + view_height
        right = left + view_width

        top = top*ratio_height
        left= left*ratio_width
        bottom = bottom*ratio_height
        right = right*ratio_width


        print( 'height =' + story.top + 'and width =' + story.left)
        print ( 'natural width' + str(natural_image_width) + "natural height" + str(natural_image_height))

        cropped_image = img.crop((left, top, right, bottom))
        cropped_image.save( story.photo.path )

        print("test the python print funciton")

        return story
