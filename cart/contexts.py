from django.shortcuts import get_object_or_404
from arts.models import Art


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    art_count = 0
    
    for id, quantity in cart.items():
        art = get_object_or_404(art, pk=id)
        total += quantity * Art.price
        art_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'art': art})
    
    return {'cart_items': cart_items, 'total': total, 'art_count': art_count}