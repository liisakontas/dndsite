from .models import WildMagicTable
from django.http import JsonResponse

def getwildmagic(request, roll):
    object = WildMagicTable.objects.get(dice_value=roll)
    data = {
        "roll": roll,
        "effect": object.effect,
        "url": object.urls,
    }
    return JsonResponse(data)