for i in $(xfconf-query -c xfce4-desktop -p /backdrop -l|egrep -e "screen.*/monitor.*image-path$" -e "screen.*/monitor.*/last-image$"); do
    xfconf-query -c xfce4-desktop -p $i -n -t string -s $1
    xfconf-query -c xfce4-desktop -p $i -s $1
done
#thanks to https://askubuntu.com/questions/414422/command-to-change-the-wallpaper-in-xubuntu