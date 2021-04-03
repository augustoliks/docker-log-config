.. image:: https://copr.fedorainfracloud.org/coprs/augustoliks/docker-log-config/package/docker-log-config/status_image/last_build.png
    :target: https://copr.fedorainfracloud.org/coprs/augustoliks/docker-log-config/builds/

docker-server-config
====================

Rsyslog, Logrotate and Docker config files, configured to: ingest, process and persist and manage retention/rotation Containers logs.

Dependencies
------------

=========   ==========================  ===============
Package     Version                     Description
=========   ==========================  ===============
docker      19.03.8                     Container Runtime
rsyslog     8.2008.0.master-1597014157  Enhanced system logging and kernel message trapping daemon
logrotate   logrotate-3.15.1-1          Rotates, compresses, removes and mails system log files
=========   ==========================  ===============

Install
-------

This project was publish in RPM package format, available in **Copr Repositories**.

To install ``docker-log-config`` package, first, enable this follow Copr:

.. code:: shell

    dnf copr enable augustoliks/docker-log-config

After enable ``augustoliks/docker-log-config``, this ``docker-log-config`` already avaible to install.

.. code:: shell

    dnf install docker-log-config

How it Works
------------

Containers logs will be persist in disk. Each day (midnight specifically), log files are rotated and compressed. The last 30 log files per Container will be preserved.

.. code:: shell

    /var/log/containers/<CONTAINER-NAME>.log
    /var/log/containers/bkp/<CONTAINER-NAME>.{1..30}.log.gz

Developer Notes
---------------

- Create new Release:

.. code:: shell
    
    tito tag

- Test RPM build:

.. code:: shell
    
    tito rpm
