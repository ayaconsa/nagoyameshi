from django.views.generic import TemplateView



# ================== 管理者（サイト運営側）画面 ==================


# 管理者（サイト運営者）トップページ
class AdminRestaurantRegistrationView(TemplateView):
    template_name = "NagoyameshiApp/admin2/admin_restaurant_registration.html"