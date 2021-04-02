Name: docker-config
Version: 1.0.3
Release: 1
Summary: Testes
License: GPLv2+
Source0: %{name}-%{version}.tar.gz


%description
testes


%prep
%setup -q


%install
mkdir -p %{buildroot}/opt/
cp teste.sh %{buildroot}/opt/


%files
/opt/teste.sh


%changelog
* Fri Apr 02 2021 Carlos Neto <carlos.neto.dev@gmail.com> 1.0.3-1
- bug: inserted rpm prep (carlos.neto.dev@gmail.com)

* Fri Apr 02 2021 Carlos Neto <carlos.neto.dev@gmail.com> 1.0.2-1
- bug: inserted rpm prep (carlos.neto.dev@gmail.com)

* Fri Apr 02 2021 Carlos Neto <carlos.neto.dev@gmail.com> 1.0.1-1
- new package built with tito

* Fri Apr 02 2021 Carlos Neto <carlos.augusto@fotosensores.com> 1.0.1-1
- new package built with tito

