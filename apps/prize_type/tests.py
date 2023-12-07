# from rest_framework.test import APITestCase
# from rest_framework import status


# class CreateTestPeriod(APITestCase):

#     def setUp(self):
#         self.test_test_url = 'api/v1/prize_types'
#         self.payload_valid = {
#             'prize_type': 'ລາງວັນໃຫຍ່', 'is_active': 'true'}

#     def test_create(self):
#         data = {'prize_type': 'ລາງວັນໃຫຍ່', 'is_active': 'true'}
#         response = self.client.post(
#             self.test_test_url, data)
#         print(response.json())
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
