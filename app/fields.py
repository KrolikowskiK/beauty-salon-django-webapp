from django.forms import ModelChoiceField


class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj}, {obj.service} - {obj.service.price} zł"
