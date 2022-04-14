import re
from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']

        if not request.user.id:
            messages.error(
                request, 'Before adding a listing to favorites you must login')
            return redirect('/listings/' + listing_id)

        name = request.POST['name']
        email = request.POST['email']
        # phone = request.POST['phone']
        phone = '0000000000'
        # message = request.POST['message']
        user_id = request.POST['user_id']
        # realtor_email = request.POST['realtor_email']

        # Check if user already made an inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already added this listing to favorites')
                return redirect('/listings/' + listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                          phone=phone, message='', user_id=user_id)

        contact.save()

        # Send Email
        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
        #     'subleet.info@gmail.com',
        #     [realtor_email, 'roy.druker95@gmail.com'],
        #     fail_silently=False
        # )

        # messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/' + listing_id)
