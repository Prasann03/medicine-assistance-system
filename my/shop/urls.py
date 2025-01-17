from django.contrib import admin
from django.urls import path,include


from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('add-patient-form',views.add_patient ,name='add_patient'),
    path('quick-add-patient-form',views.quick_add_patient ,name='quick_add_patient'),
    path('patients',views.all_patients ,name='all_patients'),
    path('reports',views.reports,name='reports'),
    path('collection-report', views.collection_reports,name='collection_reports'),
    path('index',views.index,name='index'),
    path('n_patients',views.n_patients,name='n_patients'),
    path('visit-form/<int:patient_id>',views.add_visit ,name='add_visit'),
    path('index_doctor',views.index_doctor,name='index_doctor'),
    path('login',views.login_user,name='login'),
    path('register',views.register,name='register'),
    path('options',views.options,name='options'),
    path('logout',views.logout,name='logout'),
    path('info',views.info,name='info'),
    path('successful_profile',views.successful_profile,name='successful_profile'),
    path('dashboard',views.patient_dashboard,name='dashboard'),
    path('profile',views.profile,name='profile'),
    path('update/<int:id>',views.update_patient ,name='update_patient'),
    path('delete/<int:id>',views.delete_patient ,name='delete_patient'),
    path('email_template',views.email_template,name='email_template'), 
    path('patient_detail',views.patient_detail,name='patient_detail'),
    path('Quick_Statistics',views.Quick_Statistics,name='Quick_Statistics'),
    path('create_reminder',views.create_reminder,name='create_reminder'),
    path('schedule',views.schedule,name='schedule'),
    path('pricing',views.pricing,name='pricing'),
    path('faq',views.faq,name='faq'),
    path('inquiry_page', views.inquiry_page, name='inquiry_page'),
    path('inquiry_success', views.inquiry_success, name='inquiry_success'),
    path('inquiry_list', views.inquiry_list, name='inquiry_list'),
    path('add-room', views.add_room, name='add_room'),
    path('edit-room', views.edit_room, name='edit_room'),
    path('add-payment', views.add_payment, name='add_payment'),
    path('about-payment', views.about_payment, name='about_payment'),
    path('patient_profile/<int:id>', views.patient_profile, name='patient_profile'),
    path('medication-details/', views.medication_details, name='medication_details'),
    

]