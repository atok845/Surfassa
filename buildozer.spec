[app]
title = Calculadora Surfacagem
package.name = calculadorasurfacagem
package.domain = org.kivy
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.kivy_version = 2.1.0

[buildozer]
log_level = 2
warn_on_root = 1

# Caminho do SDK manual
android.sdk_path = /home/runner/android-sdk

# Versões fixas para evitar erro de AIDL
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2

# Aceitar automaticamente as licenças
android.accept_sdk_license = true
