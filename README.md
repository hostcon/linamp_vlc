# linamp_vlc
Linamp com moto VLC

# Player com VLC (robusto)

# Aqui você usa o motor do próprio VLC — muito mais estável.

# Instalação
pip install python-vlc

# E precisa ter o VLC instalado no sistema

VLC media player
Código (VLC + Tkinter)

Diferença REAL (importante pra você explicar em aula)

# pygame
  Simples
  Didático
  Mais controle manual
  Menos recursos

# VLC
  Já é um player completo por dentro
  Suporta mais formatos
  Melhor controle de tempo
  Mais estável

  ==================================================


  Esse erro aqui:

NameError: no function 'libvlc_new'

não é bug no seu código — é problema de instalação/ligação da biblioteca nativa do VLC.

👉 O pacote Python (:contentReference[oaicite:0]{index=0}) é só um wrapper.
Ele depende do VLC instalado no sistema (biblioteca C libvlc).

🧠 O que está acontecendo

O Python tentou chamar:

libvlc_new()

Mas não encontrou a biblioteca nativa do VLC media player no sistema.

✅ SOLUÇÃO (Linux / Pop!_OS / Ubuntu)
1️⃣ Instalar o VLC completo
sudo apt update
sudo apt install vlc
2️⃣ (IMPORTANTE) Instalar a libvlc separadamente
sudo apt install libvlc-dev

👉 Isso garante que o Python consiga acessar a lib

3️⃣ Teste rápido no terminal
vlc --version

Se aparecer versão → OK

4️⃣ Teste no Python
import vlc
print(vlc.Instance())

Se não der erro → resolveu ✔️

⚠️ Problema comum (PyCharm / venv)

Você está usando:

.venv/lib/python3.12/

👉 Isso NÃO é o problema — o python-vlc funciona no venv
👉 MAS o sistema precisa enxergar a libvlc global

🔧 Se ainda der erro

Força o caminho da lib manualmente:

import os
os.environ["VLC_PLUGIN_PATH"] = "/usr/lib/x86_64-linux-gnu/vlc/plugins"

import vlc

Ou:

vlc.Instance("--no-xlib")
🔍 Verifique se a lib existe
ls /usr/lib/x86_64-linux-gnu/libvlc.so*

Se aparecer algo → está instalado

💡 Dica de professor (isso evita dor de cabeça na aula)

Se for usar VLC com alunos:

👉 Linux → precisa instalar:

vlc
libvlc-dev

👉 Windows → instalar VLC resolve tudo

🎯 Resumo direto
Problema	Solução
libvlc_new não encontrado	Instalar VLC
Ainda não funciona	Instalar libvlc-dev
venv	Não interfere
