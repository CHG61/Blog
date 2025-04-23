#!/usr/bin/env bash

# Gereken Python kütüphanelerini yükler
pip install -r requirements.txt

# Statik dosyaları toplar (CSS, JS, görseller vs.)
python manage.py collectstatic --no-input
