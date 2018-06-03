from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile

import io
from PIL import Image

from croppie.widgets import CroppieImageRatioWidget


class CroppieField(forms.MultiValueField):

    def __init__(self, options={}, widget=None, *args, **kwargs):
        fields = (
            forms.ImageField(),
            forms.CharField(),
            forms.CharField(),
            forms.CharField(),
            forms.CharField(),
            forms.CharField(),  #test code for rotation
        )
        if widget is None:
            widget = CroppieImageRatioWidget(options=options)

        super(CroppieField, self).__init__(
            fields=fields, widget=widget, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            data_image = data_list[0]
            ratio = data_list[1:5]
            ratio = [int(i) for i in ratio]
            rotation = data_list[5]
            print(data_list[5])
            return self.crop_image(data_image, ratio, rotation)

    def crop_image(self, data_image, ratio, rotation ):
        image = Image.open(data_image)
        print(rotation)
        print(ratio)
        pic = image.rotate(90*int(rotation), expand=True)
        cropped_image = pic.crop(ratio)
        print("In crop image")

        # saving image to memory
        thumb_io = io.BytesIO()
        cropped_image.save(
            thumb_io,
            data_image.content_type.split('/')[-1].upper()
        )

        # creating new InMemoryUploadedFile() based on the modified file
        file = InMemoryUploadedFile(
            thumb_io,
            'photo',
            data_image._get_name(),
            data_image.content_type,
            None, None,
        )
        return file
