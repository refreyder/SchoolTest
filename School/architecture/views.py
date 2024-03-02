from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Groups, ListStudents
from django.utils import timezone



@api_view(['POST'])
def grant_access_to_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:
        user_id = request.user.id
        groups = Groups.objects.filter(product=product).order_by('min_users', 'max_users')
        for group in groups:
            if group.min_users <= group.groupmembership_set.count() < group.max_users + 1:
                if product.cost_paid_by_user(user_id) and product.start_datetime <= timezone.now():
                    ListStudents.objects.create(user_id=user_id, group=group)
                    return Response({'message': 'Access granted'})

    # Product has not started or no suitable group found, or payment is not done
    return Response({'message': 'Access denied'})

