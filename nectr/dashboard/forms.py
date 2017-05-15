from django import forms


class CoursesForm(forms.Form):
    #  <input name="subject" type="text" id="subject" placeholder="Subject">
    #                 <input name="course" type="text" id="course" placeholder="Courses">
    subject = forms.CharField()
    course = forms.CharField()

class EditProfileForm(forms.Form):
    pass
