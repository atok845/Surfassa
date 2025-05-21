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

# Adicione isso se quiser um ícone customizado
# icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1

# Diretório do Android SDK que instalamos manualmente no workflow
android.sdk_path = /home/runner/android-sdk

# Garante que o Buildozer não tente baixar SDK duplicado
android.accept_sdk_license = true
