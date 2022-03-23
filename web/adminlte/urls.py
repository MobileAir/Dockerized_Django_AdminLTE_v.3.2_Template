from django.urls import path
from .views import *

app_name = 'adminlte'

urlpatterns = [
    path('index/', MixView.as_view(template_name='adminlte/index.html'), name='index'),
    path('index2/', MixView.as_view(template_name='adminlte/index2.html'), name='index2'),
    path('index3/', MixView.as_view(template_name='adminlte/index3.html'), name='index3'),
    path('widgets/', MixView.as_view(template_name='adminlte/pages/widgets.html'), name='widgets'),
    path('calendar/', MixView.as_view(template_name='adminlte/pages/calendar.html'), name='calendar'),
    path('gallery/', MixView.as_view(template_name='adminlte/pages/gallery.html'), name='gallery'),
]

"""Layout Options part"""
urlpatterns += [
    path('layout/top-nav/', MixView.as_view(template_name='adminlte/pages/layout/top-nav.html'),
         name='layout_top-nav'),
    path('layout/top-nav-sidebar/',
         MixView.as_view(template_name='adminlte/pages/layout/top-nav-sidebar.html'), name='layout_top-nav-sidebar'),
    path('layout/boxed/',
         MixView.as_view(template_name='adminlte/pages/layout/boxed.html'), name='layout_boxed'),
    path('layout/fixed-sidebar/',
         MixView.as_view(template_name='adminlte/pages/layout/fixed-sidebar.html'), name='layout_fixed-sidebar'),
    path('layout/fixed-navbar/',
         MixView.as_view(template_name='adminlte/pages/layout/fixed-topnav.html'), name='layout_fixed-topnav'),
    path('layout/fixed-footer/',
         MixView.as_view(template_name='adminlte/pages/layout/fixed-footer.html'), name='layout_fixed-footer'),
    path('layout/collapsed-sidebar/',
         MixView.as_view(template_name='adminlte/pages/layout/collapsed-sidebar.html'), name='layout_collapsed-sidebar')
]

"""Charts part"""
urlpatterns += [
    path('charts/chartjs/', MixView.as_view(template_name='adminlte/pages/charts/chartjs.html'), name='chartjs'),
    path('charts/flot/', MixView.as_view(template_name='adminlte/pages/charts/flot.html'), name='flot'),
    path('charts/inline/', MixView.as_view(template_name='adminlte/pages/charts/inline.html'), name='inline'),
]

"""UI elements part"""
urlpatterns += [
    path('ui/general/', MixView.as_view(template_name='adminlte/pages/UI/general.html'), name='general'),
    path('ui/icons/', MixView.as_view(template_name='adminlte/pages/UI/icons.html'), name='icons'),
    path('ui/buttons/', MixView.as_view(template_name='adminlte/pages/UI/buttons.html'), name='buttons'),
    path('ui/sliders/', MixView.as_view(template_name='adminlte/pages/UI/sliders.html'), name='sliders'),
    path('ui/modals/', MixView.as_view(template_name='adminlte/pages/UI/modals.html'), name='modals'),
    path('ui/navbar/', MixView.as_view(template_name='adminlte/pages/UI/navbar.html'), name='navbar'),
    path('ui/timeline/', MixView.as_view(template_name='adminlte/pages/UI/timeline.html'), name='timeline'),
    path('ui/ribbons/', MixView.as_view(template_name='adminlte/pages/UI/ribbons.html'), name='ribbons'),
]

"""Forms part"""
urlpatterns += [
    path('forms/general/', MixView.as_view(template_name='adminlte/pages/forms/general.html'), name='general_form'),
    path('forms/advanced/', MixView.as_view(template_name='adminlte/pages/forms/advanced.html'), name='advanced_form'),
    path('forms/editors/', MixView.as_view(template_name='adminlte/pages/forms/editors.html'), name='editors_form'),
    path('forms/validation/', MixView.as_view(template_name='adminlte/pages/forms/validation.html'),
         name='validation_form'),
]

"""Tables part"""
urlpatterns += [
    path('tables/data/', MixView.as_view(template_name='adminlte/pages/tables/data.html'), name='data_table'),
    path('tables/jsgrid/', MixView.as_view(template_name='adminlte/pages/tables/jsgrid.html'), name='jsgrid_table'),
    path('tables/simple/', MixView.as_view(template_name='adminlte/pages/tables/simple.html'), name='simple_table'),
]

"""Mailbox part"""
urlpatterns += [
    path('mailbox/compose/', MixView.as_view(template_name='adminlte/pages/mailbox/compose.html'),
         name='compose_mailbox'),
    path('mailbox/mailbox/', MixView.as_view(template_name='adminlte/pages/mailbox/mailbox.html'),
         name='mailbox_mailbox'),
    path('mailbox/read-mail/', MixView.as_view(template_name='adminlte/pages/mailbox/read-mail.html'),
         name='read-mail_mailbox'),
]

"""Pages part"""
urlpatterns += [
    path('pages/invoice/', MixView.as_view(template_name='adminlte/pages/examples/invoice.html'),
         name='pages_invoice'),
    path('pages/invoice/print/', MixView.as_view(template_name='adminlte/pages/examples/invoice-print.html'),
         name='pages_invoice-print'),
    path('pages/profile/', MixView.as_view(template_name='adminlte/pages/examples/profile.html'),
         name='pages_profile'),
    path('pages/e-commerce/', MixView.as_view(template_name='adminlte/pages/examples/e-commerce.html'),
         name='pages_e-commerce'),
    path('pages/projects/', MixView.as_view(template_name='adminlte/pages/examples/projects.html'),
         name='pages_projects'),
    path('pages/project-add/', MixView.as_view(template_name='adminlte/pages/examples/project-add.html'),
         name='pages_project-add'),
    path('pages/project-edit/', MixView.as_view(template_name='adminlte/pages/examples/project-edit.html'),
         name='pages_project-edit'),
    path('pages/project-detail/', MixView.as_view(template_name='adminlte/pages/examples/project-detail.html'),
         name='pages_project-detail'),
    path('pages/contacts/', MixView.as_view(template_name='adminlte/pages/examples/contacts.html'),
         name='pages_contacts'),
]

"""Extra part"""
urlpatterns += [
    path('extra/login/', MixView.as_view(template_name='adminlte/pages/examples/login.html'),
         name='extra_login'),
    path('extra/register/', MixView.as_view(template_name='adminlte/pages/examples/register.html'),
         name='extra_register'),
    path('extra/forgot/', MixView.as_view(template_name='adminlte/pages/examples/forgot-password.html'),
         name='extra_forgot'),
    path('extra/recover/', MixView.as_view(template_name='adminlte/pages/examples/recover-password.html'),
         name='extra_recover'),
    path('extra/lockscreen/', MixView.as_view(template_name='adminlte/pages/examples/lockscreen.html'),
         name='extra_lockscreen'),
    path('extra/leg-user-menu/', MixView.as_view(template_name='adminlte/pages/examples/legacy-user-menu.html'),
         name='extra_leg-user-menu'),
    path('extra/lang-menu/', MixView.as_view(template_name='adminlte/pages/examples/language-menu.html'),
         name='extra_lang'),
    path('extra/error404/', MixView.as_view(template_name='adminlte/pages/examples/404.html'),
         name='extra_404'),
    path('extra/error500/', MixView.as_view(template_name='adminlte/pages/examples/500.html'),
         name='extra_500'),
    path('extra/pace/', MixView.as_view(template_name='adminlte/pages/examples/pace.html'),
         name='extra_pace'),
    path('extra/blank/', MixView.as_view(template_name='adminlte/pages/examples/blank.html'),
         name='extra_blank'),
    path('extra/starter/', MixView.as_view(template_name='adminlte/pages/examples/starter.html'),
         name='extra_starter'),
]
