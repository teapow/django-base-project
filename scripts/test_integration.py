"""Simple script to confirm that the system is up and running."""

from simple_pages.models import Page
import requests


def run():
    """Run the integration test."""
    try:
        page = Page.objects.get(access_url="/")
        created = False
    except Page.DoesNotExist:
        page = Page.objects.create(title="Home", access_url="/")
        created = True

    response = requests.get("http://nginx/")

    if created:
        page.delete()

    assert response.status_code == 200
