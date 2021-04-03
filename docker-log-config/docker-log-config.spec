Name: docker-log-config
Version: 1.0.2
Release: 1
BuildArch: noarch
Packager: Carlos Neto <carlos.augusto@fotosensores.com>
Summary: Rsyslog, Logrotate and Docker config files, configured to: ingest, process and persist and manage retention/rotation Containers logs.
License: GPLv2+
Source0: %{name}-%{version}.tar.gz
URL: https://github.com/augustoliks/docker-log-config
Requires: rsyslog, logrotate


%define logrotate_dir /etc/logrotate.d
%define docker_dir /etc/docker
%define rsyslog_dir /etc/rsyslog.d


%description
Rsyslog, Logrotate and Docker config files, configured to: ingest, process and persist and manage retention/rotation Containers logs.


%prep
%setup -q


%install
mkdir -p %{buildroot}/%{logrotate_dir}
mkdir -p %{buildroot}/%{rsyslog_dir}
mkdir -p %{buildroot}/%{docker_dir}

cp docker/daemon.json %{buildroot}/%{docker_dir}/
cp rsyslog/rsyslog.d/* %{buildroot}/%{rsyslog_dir}/
cp rsyslog/rsyslog.conf %{buildroot}/etc/rsyslog.dlc.conf
cp logrotate/docker-server-config %{buildroot}/%{logrotate_dir}/


%files
%attr(644, -, -)
%{logrotate_dir}/docker-server-config

%{docker_dir}/daemon.json

/etc/rsyslog.dlc.conf
%{rsyslog_dir}/20-dlc-base.conf
%{rsyslog_dir}/30-dlc-persist.conf


%post
cp /etc/rsyslog.conf /etc/rsyslog.conf.bkp
cp /etc/rsyslog.dlc.conf /etc/rsyslog.conf

mkdir -p /var/log/containers/bkp/
mkdir -p /var/log/containers/

echo "
[!] Instalation complete, execute follow commands:

    systemctl restart rsyslog
    systemctl restart logrotare
    systemctl restart docker
"

%changelog
* Fri Apr 02 2021 Carlos Neto <carlos.neto.dev@gmail.com> 1.0.2-1
- test remove clean (carlos.neto.dev@gmail.com)

* Fri Apr 02 2021 Carlos Neto <carlos.neto.dev@gmail.com> 1.0.1-1
- new package built with tito


# %clean
# rm -rf $RPM_BUILD_ROOT
