from django.test import TestCase
from nexaas_id_client.oauth_token import OAuthToken, TokenSerializer
from ._vcr import vcr


class IDProfileTestCase(TestCase):

    token = OAuthToken(
        access_token='9fab3314d70124e792323196c9c89adb'
                     '704cc07768fac48f4157fd89c41671f1',
    )

    def signin(self):
        client = self.client
        session = client.session
        session['oauth_token'] = TokenSerializer.serialize(self.token)
        session.save()

    def test_redirect_to_sign_in(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, '/oauth/signin/')

    def test_authorized_access(self):
        self.signin()

        with vcr.use_cassette('authorized.yaml'):
            res = self.client.get('/')

        self.assertContains(res, 'Hi Rodrigo Cacilhas!')
        self.assertContains(
            res,
            '<script src="http://localhost:3000/api/v1/widgets/user.js'
            '?access_token={}'
            '&callback=initWidget"></script>'
            .format(self.token.access_token),
        )
        self.assertContains(
            res,
            '<img src="http://localhost:3000/images/avatar/'
            '51dfb322-2c58-457a-b4e8-6de9d82c1316?size=140" '
            'alt="rodrigo.cacilhas@nexaas.com" />',
        )
