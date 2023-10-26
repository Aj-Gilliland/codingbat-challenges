from django.test import SimpleTestCase


class testWarmUp1(SimpleTestCase):
    def test_93(self):
        response = self.client.get("/warmup-1/93")
        self.assertContains(response, "True")

    def test_90(self):
        response = self.client.get("/warmup-1/90")
        self.assertContains(response, "True")

    def test_89(self):
        response = self.client.get("/warmup-1/89")
        self.assertContains(response, "False")


class testWarmUp2(SimpleTestCase):
    def test_Code(self):
        response = self.client.get("/warmup-2/Code")
        self.assertContains(response, "CCoCodCode")

    def test_abc(self):
        response = self.client.get("/warmup-2/abc")
        self.assertContains(response, "aababc")

    def test_ab(self):
        response = self.client.get("/warmup-2/ab")
        self.assertContains(response, "aab")


class String2(SimpleTestCase):
    def test_catdog(self):
        response = self.client.get("/string-2/catdog")
        self.assertContains(response, "True")

    def test_catcat(self):
        response = self.client.get("/string-2/catcat")
        self.assertContains(response, "False")

    def test_1cat1cadodog(self):
        response = self.client.get("/string-2/1cat1cadodog")
        self.assertContains(response, "True")


class logic2(SimpleTestCase):
    def test_123(self):
        response = self.client.get("/logic-2/1/2/3")
        self.assertContains(response, 6)

    def test_323(self):
        response = self.client.get("/logic-2/3/2/3")
        self.assertContains(response, 2)

    def test_333(self):
        response = self.client.get("/logic-2/3/3/3")
        self.assertContains(response, 0)
