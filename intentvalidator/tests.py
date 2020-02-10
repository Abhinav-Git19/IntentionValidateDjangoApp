from rest_framework.test import APITestCase, APIClient
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path += "/JSONfiles"


# Create your tests here.

class POSTServiceTests(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_finite_one_valid(self):
        fp_in = open(dir_path + "/" + "in1.json")
        fp_out = open(dir_path + "/" + "out1.json")

        jin = json.load(fp_in)
        jout = json.load(fp_out)

        response = self.client.post('/validateFiniteEntity', jin, format='json')
        self.assertEqual(json.loads(response.content), jout)
        fp_in.close()
        fp_out.close()

    def test_finite_invalid_only(self):
        fp_in = open(dir_path + "/" + "in2.json")
        fp_out = open(dir_path + "/" + "out2.json")

        jin = json.load(fp_in)
        jout = json.load(fp_out)

        response = self.client.post('/validateFiniteEntity', jin, format='json')
        self.assertEqual(json.loads(response.content), jout)
        fp_in.close()
        fp_out.close()

    def test_finite_empty(self):
        fp_in = open(dir_path + "/" + "in3.json")
        fp_out = open(dir_path + "/" + "out3.json")

        jin = json.load(fp_in)
        jout = json.load(fp_out)

        response = self.client.post('/validateFiniteEntity', jin, format='json')
        self.assertEqual(json.loads(response.content), jout)
        fp_in.close()
        fp_out.close()

    def test_finite_valid_invalid(self):
        fp_in = open(dir_path + "/" + "in4.json")
        fp_out = open(dir_path + "/" + "out4.json")

        jin = json.load(fp_in)
        jout = json.load(fp_out)

        response = self.client.post('/validateFiniteEntity', jin, format='json')
        self.assertEqual(json.loads(response.content), jout)
        fp_in.close()
        fp_out.close()

    def test_finite_all_valid(self):
        fp_in = open(dir_path + "/" + "in5.json")
        fp_out = open(dir_path + "/" + "out5.json")

        jin = json.load(fp_in)
        jout = json.load(fp_out)

        response = self.client.post('/validateFiniteEntity', jin, format='json')
        self.assertEqual(json.loads(response.content), jout)
        fp_in.close()
        fp_out.close()

    def test_numeric_one_valid(self):
        fp_in = open(dir_path + "/" + "in6.json")
        fp_out = open(dir_path + "/" + "out6.json")

        jin = json.load(fp_in)
        jout = json.load(fp_out)

        response = self.client.post('/validateNumEntity', jin, format='json')
        self.assertEqual(json.loads(response.content), jout)
        fp_in.close()
        fp_out.close()

    def test_numeric_invalid_only(self):
        fp_in = open(dir_path + "/" + "in7.json")
        fp_out = open(dir_path + "/" + "out7.json")

        jin = json.load(fp_in)
        jout = json.load(fp_out)

        response = self.client.post('/validateNumEntity', jin, format='json')
        self.assertEqual(json.loads(response.content), jout)
        fp_in.close()
        fp_out.close()

    def test_numeric_empty(self):
        fp_in = open(dir_path + "/" + "in8.json")
        fp_out = open(dir_path + "/" + "out8.json")

        jin = json.load(fp_in)
        jout = json.load(fp_out)

        response = self.client.post('/validateNumEntity', jin, format='json')
        self.assertEqual(json.loads(response.content), jout)
        fp_in.close()
        fp_out.close()

    def test_numeric_valid_invalid(self):
        fp_in = open(dir_path + "/" + "in9.json")
        fp_out = open(dir_path + "/" + "out9.json")

        jin = json.load(fp_in)
        jout = json.load(fp_out)

        response = self.client.post('/validateNumEntity', jin, format='json')
        self.assertEqual(json.loads(response.content), jout)
        fp_in.close()
        fp_out.close()

    def test_numeric_all_valid(self):
        fp_in = open(dir_path + "/" + "in10.json")
        fp_out = open(dir_path + "/" + "out10.json")

        jin = json.load(fp_in)
        jout = json.load(fp_out)

        response = self.client.post('/validateNumEntity', jin, format='json')
        self.assertEqual(json.loads(response.content), jout)
        fp_in.close()
        fp_out.close()
