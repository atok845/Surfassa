[app]
title = MeuApp
package.name = meuapp
package.domain = org.exemplo
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1
android.api = 34
android.build_tools_version = 36.0.0
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.accept_sdk_license = True
