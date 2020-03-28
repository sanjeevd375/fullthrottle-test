# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import FTUserSerializer
from .models import FTUser, Activity
from django.shortcuts import render, redirect
# Create your views here.

class UserActivityView(viewsets.ModelViewSet):
    """
    Description : View for UserActivity
    """
    serializer_class = FTUserSerializer
    model = FTUser

    def get_queryset(self):
        """
        returns all FTUser objects as queryset
        """
        queryset = FTUser.objects.all()
        return queryset

    def list(self, request):
        """
        FTUser List view
        """
        queryset = self.get_queryset()
        serializer = FTUserSerializer(queryset, many=True, context={'request': request})

        if serializer.is_valid:
            return Response({"ok":True, "members":serializer.data})
            #return render(request, 'userActivityList.html', context={"ok":True, "members":serializer.data})
        else:
            return Response({"ok":False, "members":serializer.error})
