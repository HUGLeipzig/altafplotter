import os

# varvis credentials

varvis_hg19_credentials = {
    "target"    : os.environ.get('VARVIS_HG19_TARGET', ''),
    "user_name" : os.environ.get('VARVIS_HG19_USER', ''),
    "password"  : os.environ.get('VARVIS_HG19_password', '')
}

varvis_hg38_credentials = {
    "target"    : os.environ.get('VARVIS_HG38_TARGET', ''),
    "user_name" : os.environ.get('VARVIS_HG38_USER', ''),
    "password"  : os.environ.get('VARVIS_HG38_password', '')
}