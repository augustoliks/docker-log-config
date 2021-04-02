Name: teste
Version: 1.0.1
Release: 1
Summary: Testes
License: Free
# URL: https://github.com/augustoliks/docker-log-config
# Source: 


%description
testes


%install
mkdir -p %{buildroot}/opt/
cp teste.sh %{buildroot}/opt/


%files
/opt/teste.sh
