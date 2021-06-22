import json
from django import views
from django.http import JsonResponse
from django.views import View
from .models import Owner, Dog

class OwnerView(View) :
    def post(self, request) :
        data = json.loads(request.body)

        if(Owner.objects.filter(name=data['owner']).exists()) :
            owner = Owner.objects.get(name=data['owner'])
            dog = Dog.objects.create(
            name=data['dog_name'],
            age=data['dog_age'],
            owner = owner
        )
        else :
            owner = Owner.objects.create(
                name = data['owner'],
                email = data["email"],
                age = data['age']
                )
            dog = Dog.objects.create(
                name=data['dog_name'],
                age=data['dog_age'],
                owner = owner
            )

        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

    def get(self, request) :
        dogs = Dog.objects.all()
        results = []
        for d in dogs :
            results.append(
                {
                    "onwer" : d.owner.name,
                    "name" : d.name,
                    "age" : d.age
                }
            )

        return JsonResponse({"results" : results}, status = 200)        