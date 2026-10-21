import pas2_ini_overlay as api

print(api.overlay("[app]\nmode=dev", "[app]\nmode=prod"))
