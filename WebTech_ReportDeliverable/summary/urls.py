from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.index_view.as_view(), name='index'),
    url(r'^summary/(?P<pk>\d+)/$', views.summary_detail, name='summary_detail'),
    url(r'^subject/(?P<pk>\d+)/$', views.subject, name='subject'),
    url(r'^book/(?P<pk>\d+)/$', views.book, name='book'),
    url(r'^university/(?P<pk>\d+)/$', views.uni, name='uni'),
    url(r'^allUnis/$', views.allUnis, name='allUnis'),
    url(r'^allSubj/$', views.allSubj, name='allSubj'),
    url(r'^allBooks/$', views.allBooks, name='allBooks'),
    url(r'^login/$', views.login_auth.as_view(), name='login'),
    url(r'^logout/$', views.logout_auth.as_view(), name='logout'),
    url(r'^delete/(?P<pk>\d+)/$', views.deleteSummary, name='deleteSummary'),
    url(r'^user/add_summary/$', views.addSummary.as_view(), name='addSummary'),
    url(r'^signup/$', views.signup.as_view(), name='signup'),
    url(r'^user/', views.userView.as_view(), name='userView'),
    url(r'^pdf/.*$', views.pdf_view, name='pdf_view'), #for showing PDF
    url(r'^upload/$', views.uploadView, name='uploadView'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
