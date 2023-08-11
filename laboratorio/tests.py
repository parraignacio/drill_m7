from django.test import TestCase
from django.urls import reverse

from .models import Laboratorio


class LaboratorioTests(TestCase):
    tags = ['laboratorio']
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(nombre='Laboratorio X', ciudad='Ciudad X', pais='Pais X')
 
    def test_model_content(self):
        self.assertEqual(self.laboratorio.nombre, "Laboratorio X")
        self.assertEqual(self.laboratorio.ciudad, "Ciudad X")
        self.assertEqual(self.laboratorio.pais, 'Pais X')
 
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
 
    def test_homepage(self):
        response = self.client.get(reverse("mostrar-lab"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mostrar.html")
        self.assertContains(response, "Información de Laboratorios")
        self.assertContains(response, "Usted ha visitado esta página")