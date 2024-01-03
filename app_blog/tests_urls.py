from django.test import TestCase
from django.urls import reverse, resolve
from django.utils import timezone

from .models import Article

from .views import HomePageView

class HomeTests(TestCase):
    def test_home_view_status_code(self):
         url = reverse('main')
         response = self.client.get(url)
         self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, HomePageView)

    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args = ('name',))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_article_detail_status_code(self):
        self.article = Article.objects.create(
            title='Example Article',
            description='This is an example article.',
            pub_date=timezone.datetime(2004, 3, 15),
            slug='example-article'
            # Add other necessary fields
        )

        url = reverse('news-detail', args=(
            self.article.pub_date.strftime("%Y"),
            self.article.pub_date.strftime("%m"),
            self.article.pub_date.strftime("%d"),
            self.article.slug,
        ))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)