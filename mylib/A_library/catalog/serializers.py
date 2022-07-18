from dataclasses import fields


class Bookserilizer(serilizers.ModelSerilizer):
    class Meta:
        model= Book
        fields= '__all__'
