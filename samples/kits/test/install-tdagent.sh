{{ if target.distro == "debian" }}
echo "soc un debian"
{{ elsif target.distro == "redhat" }}
echo "soc un redhat"
{{ endif }}
