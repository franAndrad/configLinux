from os import system

#Actualizar archlinux
system("pacman -Syu")

#Elimina versiones anteriores de programas que ya no tengamos instaladaos
system("pacman -Sc")

#Elimanmos todos los paquetes antiguos
system("pacman -Scc")

#Verificar paquetes huerfanos y descartados
system("pacman -Qtd && pacman -Qm")
