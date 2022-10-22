from django.urls import path
from . import views

urlpatterns = [
    path('home',views.indexShop,name="index"),
    path('indexAgency',views.indexAgency,name="indexAgency"),
    path('indexPortfolio',views.indexPortfolio,name="indexPortfolio"),
    path('indexCorporate',views.indexCorporate,name="indexCorporate"),
    path('indexLandingPage',views.indexLandingPage,name="indexLandingPage"),
    path('indexBlog',views.indexBlog,name="indexBlog"),
    path('indexApp',views.indexApp,name="indexApp"),
    path('indexRestaurant',views.indexRestaurant,name="indexRestaurant"),
    path('indexMinimal',views.indexMinimal,name="indexMinimal"),
    path('indexComingSoon',views.indexComingSoon,name="indexComingSoon"),
    path('aboutUs',views.aboutUs,name="aboutUs"),
    path('services',views.services,name="services"),
    path('contacts1',views.contacts1,name="contacts1"),
    path('contacts2',views.contacts2,name="contacts2"),
    path('error404',views.error404,name="error404"),
    path('portfolioBoxed2Col',views.portfolioBoxed2Col,name="portfolioBoxed2Col"),
    path('singlePortfolioCarousel',views.singlePortfolioCarousel,name="singlePortfolioCarousel"),
    path('boxedMasonry4Col',views.boxedMasonry4Col,name="boxedMasonry4Col"),
    path('blogGrid2ColSidebar',views.blogGrid2ColSidebar,name="blogGrid2ColSidebar"),
    path('blogTraditional',views.blogTraditional,name="blogTraditional"),
    path('blogTraditionalSidebar',views.blogTraditionalSidebar,name="blogTraditionalSidebar"),
    path('singlePostThin',views.singlePostThin,name="singlePostThin"),
    path('indexShop',views.indexShop,name="indexShop"),
    path('<slug:productUrl>',views.singleProduct,name="singleProduct"),
]