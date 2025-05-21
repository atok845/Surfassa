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

# Ícone customizado (opcional)
# icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1

# SDK instalado via workflow
android.sdk_path = /home/runner/android-sdk

# NDK será baixado automaticamente
android.accept_sdk_license = true

# Versões fixas e compatíveis
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2
