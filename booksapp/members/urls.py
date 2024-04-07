from django.urls import path

from .views import CheckoutView, ReturnView, FulfillView

urlpatterns = [
    path('checkout/', CheckoutView.as_view()),
    path('return/', ReturnView.as_view()),
    path('fulfill/', FulfillView.as_view())
    # path('stock_price/<str:ticker>/<str:pattern_name>/', StockPriceView.as_view()),
    # path('stock_price/<str:ticker>/', StockPriceView.as_view()),
    # path('tabular_pattern_gain', TabularPatternGainView.as_view()),
    # path('company_detail', CompanyDetailView.as_view())
]
