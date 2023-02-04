from utils import load_operations, print_last_five_operations

if __name__ == '__main__':
    filename = 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230204T084306Z&X-Amz-Expires=86400&X-Amz-Signature=4c1cec7738bac444776218386bd74d1a35fb49600606621536dd82c436d2a701&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22operations.json%22&x-id=GetObject'
    operation = load_operations(filename)
    name = input("Ваше имя: ")

print_last_five_operations(operation)
