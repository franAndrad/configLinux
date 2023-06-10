# Mis configuraciones
<p align="center"> <img src="./archlinux-logo-dark-1200dpi.b42bd35d5916.png" alt="logo-burgerhouse" height="200"/> </p>

## 💿 Dependencias

### 📂 Gestor de paquete [yay](https://github.com/Jguer/yay)

`$ pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si`

### 📘 Inicio de sesion [ly](https://github.com/fairyglade/ly) 

`$ yay -S ly `

### 📘 Gestor de ventanas [i3wm](https://wiki.archlinux.org/title/i3)

`$ sudo pacman -Syu i3-wm`

### 📘 Compositor para Xorg [picom](https://wiki.archlinux.org/title/picom)(transparencia)

`$ sudo pacman -Syu picom`

### 📙 Wallpaper [feh](https://wiki.archlinux.org/title/Feh_(Espa%C3%B1ol))

`$ sudo pacman -Syu feh`

## 📥 Instalacion

Para poder utilizar estos packetes debemos reemplazar los archivos dentro de su directorio home:

  `$ cd /home/$USER/`
  
  `$ git clone https://github.com/franAndrad/configLinux.git`
  
  `$ cp -r configLinux/* /home/$USER/`
  
  `$ sudo cp -r configLinux/etc/* /etc/`
  
  `$ rm -r configLinux/etc`

## 🔧 Otras Configuraciones

### 📶 Wifi
  
  Instalamos networkmanager
  
  `$ sudo pacman -Syu networkmanager`
  
  Mostrar lista de puntos de acceso
  
  `$ nmcli device wifi list`
  
  Si no muestra su SSID
  
  `$ nmcli device wifi rescan`
  
  Para conectarnos a la red wifi utilizamos 
  
  `nmcli device wifi connect *access_point_name* password *your_password*`
  
  Para verificar su conexion
  
  `nmcli connection show`
