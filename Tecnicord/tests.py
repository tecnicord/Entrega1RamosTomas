from django.test import TestCase
from Tecnicord.models import Tractores
from django.urls import reverse

class TractoresTestCase(TestCase):
    def setUp(self):
        Tractores.objects.create(nombre="6180", potencia=180)
        Tractores.objects.create(nombre="6110", potencia=110)

    def test_animals_can_speak(self):
        p1 = Tractores.objects.get(potencia=180)
        p2 = Tractores.objects.get(potencia=110)
        self.assertEqual(p1.nombre, '6180')
        self.assertEqual(p2.nombre, '6110')


class ViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('TecnicordInicio'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hay nada para mostrar")

    def test_past_question(self):
        tractor = Tractores.objects.create(nombre="6180", potencia=180)
        response = self.client.get(reverse('Tecnicord'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            f"el tractor es: { tractor.nombre } potencia { tractor.potencia }"
        )

