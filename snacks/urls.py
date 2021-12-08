from django.urls import path

from snacks.views import SnackCreateView, SnackDeleteView, SnackDetailView, SnackListView, SnackUpdateView



urlpatterns = [
    path("", SnackListView.as_view(), name = "ListView"),
    path("<int:pk>", SnackDetailView.as_view(), name = "DetailView"),
    path("create/", SnackCreateView.as_view(), name = "CreateView"), 
    path("<int:pk>/update/", SnackUpdateView.as_view(), name = "UpdateView"),
    path("<int:pd>/delete/", SnackDeleteView.as_view(), name= "DeleteView")
]