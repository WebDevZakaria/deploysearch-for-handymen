from django import forms
from django.forms import ModelForm
from .models import Createservice
from .models import Category, ReviewRating, baladiya


class Serviceform(ModelForm):

    class Meta:

        model = Createservice

        fields = ['Service_name',

                  'description', 'your_sertificate', 'images', 'baladiya', 'category']

    def __init__(self, *args, **kwargs):

        self.user = kwargs.pop('user')

        super(Serviceform, self).__init__(*args, **kwargs)

        print(self.user)

        if self.user is not None:

            self.fields['baladiya'].queryset = baladiya.objects.filter(

                wilaya=self.user.wilaya)

            self.fields['category'].queryset = Category.objects.filter(

                wilaya=self.user.wilaya)

            #self.fields['category'].queryset = Category.objects.none()

            if 'baladiya' in self.data:

                try:

                    baladiya_id = int(self.data.get('baladiya'))
                    self.fields['category'].queryset = Category.objects.filter(
                        baladiya_id=baladiya_id).order_by('Category_name')

                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset


class reviews(ModelForm):
    class Meta:
        model = ReviewRating

        fields = ['subject', 'review', 'rating']
