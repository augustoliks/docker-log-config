Name: docker-config
Version: 1.0.1
Release: 1
Summary: Testes
License: GPLv2+
# URL: https://github.com/augustoliks/docker-log-config
# Source: 


%description
testes


%install
mkdir -p %{buildroot}/opt/
cp teste.sh %{buildroot}/opt/


%files
/opt/teste.sh


%changelog
* Fri Apr 02 2021 Carlos Neto <carlos.augusto@fotosensores.com> 1.0.1-1
- new package built with tito

