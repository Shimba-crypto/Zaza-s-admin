[app]

# (str) Title of your application
title = Zaza Admin

# (str) Package name
package.name = zazaadmin

# (str) Package domain (needed for android packaging)
package.domain = org.shimba

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let's include everything in the repo)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# We need kivy and any other libs you use (like requests if you add API calls later)
requirements = python3,kivy,hostpython3

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application (Loading screen)
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_PY

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (list) Permissions
# Adding INTERNET so you can track Kwacha rates or connect to GitHub
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 31

# (str) Android NDK version to use
#android.ndk = 23b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android entry point, default is ok
#android.entrypoint = org.kivy.android.PythonActivity

# (list) Android architectures to build for (Default is armeabi-v7a)
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk)
android.release_artifact = apk

# (str) The format used to package the app for debug mode (apk or aab)
android.debug_artifact = apk


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1

# (str) Path to build artifacts
bin_dir = ./bin
