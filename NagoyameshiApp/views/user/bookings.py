from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from NagoyameshiApp.models.booking import Booking
from datetime import date

# 予約一覧（有料会員のみ）
class BookingsView(LoginRequiredMixin, TemplateView):
    template_name = "NagoyameshiApp/user/bookings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        bookings = Booking.get_sorted_bookings(user=user)
        context['bookings'] = bookings
        context['today'] = date.today()
        return context
    
