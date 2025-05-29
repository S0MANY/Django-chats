import os
from uuid import uuid4


def rename_uploaded_file(instance, filename):
    ext = filename.split(".")[-1]

    new_filename = f"{instance.username}_{uuid4().hex[:8]}.{ext}"
    return os.path.join("users_images", new_filename)
