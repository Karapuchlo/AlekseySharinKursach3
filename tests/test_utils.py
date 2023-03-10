from unittest import TestCase
from utils import print_last_five_operations, load_operations


class Test(TestCase):
    def test_print_last_five_operations(self):
        filename = 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230205T161424Z&X-Amz-Expires=86400&X-Amz-Signature=cbd89eb2b7b9dcb324ca92433979e80afc1857c68b453ff9f0d898a094e32186&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22operations.json%22&x-id=GetObject'
        operation_1 = load_operations(filename)

        print_last_five_operations(operation_1)

