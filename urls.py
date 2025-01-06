
from django.contrib import admin
from django.urls import path

from myapp import views
#admin#
urlpatterns = [
    path('login/',views.login),
    path('login_post/',views.login_post),
    path('logout/',views.logout),

    path('admin_view_pofile/', views.admin_view_pofile),
    path('add_editprfl/', views.add_editprfl),
    path('add_editprfl_POST/', views.add_editprfl_POST),
    path('add_gallery/', views.add_gallery),
    path('add_gallery_POST/', views.add_gallery_POST),
    path('admin_view_gallery/', views.admin_view_gallery),

    # path('add_bill/', views.add_bill),

    path('user_add_Uview_custstatus/',views.user_add_Uview_custstatus),
    path('user_add_Uview_custstatus_POST/',views.user_add_Uview_custstatus_POST),


    path('add_Acreateprfl/',views.add_Acreateprfl),
    path('add_Acreateprfl_POST/',views.add_Acreateprfl_POST),

    path('add_Aserviceform/',views.add_Aserviceform),
    path('add_Aserviceform_POST/',views.add_Aserviceform_POST),

    path('add_Aview_customer_rqust/',views.add_Aview_customer_rqust),
    path('add_Aview_rqst_admin_POST/',views.add_Aview_customer_rqust),

    path('add_Aview_rqst_admin/', views.add_Aview_rqst_admin),
    path('add_Aview_rqst_admin_POST/', views.add_Aview_rqst_admin_POST),

    path('add_Aviewpayment/', views.add_Aviewpayment),

    path('add_Aviewusers/', views.add_Aviewusers),
    path('add_Aviewusers_post/', views.add_Aviewusers_post),

    path('add_Aview_review/', views.add_Aview_review),
    path('HOME/',views.HOME),

    path('admin_changepass/',views.admin_changepass),
    path('admin_changepass_POST/',views.admin_changepass_POST),

    path('raz_pay/<amount>/<id>',views.raz_pay),
    path('normal_raz_pay/<amount>/<id>',views.normal_raz_pay),
    path('Admin_add_Sentamount/<id>',views.Admin_add_Sentamount),
    path('Admin_add_Sentamount_POST/',views.Admin_add_Sentamount_POST),

    path('accept/<id>',views.admin_accept),
    path('reject/<id>',views.admin_reject),

    path('accept2/<id>',views.admin_accept2),
    path('reject2/<id>',views.admin_reject2),
    path('admin_DELgal/<id>',views.admin_DELgal),

#user#

    path('user_add_Uview_custstatus/',views.user_add_Uview_custstatus),
    path('user_add_Uview_gallery/',views.user_add_Uview_gallery),
    path('user_add_Uview_gallery_POST/',views.user_add_Uview_gallery_POST),

    path('user_add_Uview_service/',views.user_add_Uview_service),
    path('user_add_Uview_service_post/',views.user_add_Uview_service_post),
    path('Aviewservices/',views.Aviewservices),
    path('edit_service/<id>',views.edit_service),
    path('delete_service/<id>',views.delete_service),
    path('edit_service_post/',views.edit_service_post),

    path('user_add_Ucustrqst/',views.user_add_Ucustrqst),
    path('user_add_Ucustrqst_POST/',views.user_add_Ucustrqst_POST),

    path('user_add_Uprofilecreation/', views.user_add_Uprofilecreation),
    path('user_add_Uprofilecreation_POST/',views.user_add_Uprofilecreation_POST),

    path('user_add_Usend_rqst/<id>', views.user_add_Usend_rqst),
    path('user_add_Usend_rqst_POST/', views.user_add_Usend_rqst_POST),

    path('user_add_Usendreview/', views.user_add_Usendreview),
    path('user_add_Usendreview_POST/',views.user_add_Usendreview_POST),

    path('user_changepass/',views.user_changepass),
    path('user_changepass_POST/',views.user_changepass_POST),

    path('uviewprofl/', views.uviewprofl),

    path('user_add_Sendpayment/', views.user_add_Sendpayment),
    path('user_add_Sendpayment_POST/', views.user_add_Sendpayment_POST),

    path('user_add_Uview_status/', views.user_add_Uview_status),

    path('HomeU/',views.HomeU),
    path('HomeU1/',views.HomeU1),

    path('user_edit_Uprofilecreation/',views.user_edit_Uprofilecreation),
    path('user_edit_Uprofilecreation_POST/',views.user_edit_Uprofilecreation_POST),

    path('add_Aview_review_POST/',views.add_Aview_review_POST),
    path('user_add_normal_Usend_rqst/<id>', views.user_add_normal_Usend_rqst),

]
