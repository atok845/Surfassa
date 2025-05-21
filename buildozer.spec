[app]
title = NomeDoSeuApp
package.name = nome_do_pacote
package.domain = org.exemplo

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy

orientation = portrait

osx.kivy_version = 2.3.0

fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

# Diretório onde o SDK será copiado no GitHub Actions
android.sdk_path = ~/.buildozer/android/platform/android-sdk

# Usa a API 34, compatível com Build Tools 36.0.0
android.api = 34
android.build_tools_version = 36.0.0

# Arquitetura padrão para compatibilidade ampla
android.archs = armeabi-v7a

# Otimiza build para debug (você pode mudar para release depois)
android.minapi = 21

# Desativa build remoto (usamos local via GitHub Actions)
android.accept_sdk_license = True
android.ndk = 25b
android.ndk_path = 

[android]
# Caso seu app use permissões (como internet), descomente abaixo
# android.permissions = INTERNET
