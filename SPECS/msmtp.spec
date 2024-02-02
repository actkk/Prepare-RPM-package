%global debug_package %{nil}

Name:           msmtp
Version:        1.8.25
Release:        1%{?dist}
Summary:        Lightweight SMTP client

License:        GPL-3.0
URL:            https://marlam.de/msmtp/
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  make
Requires:       bash

%description
msmtp is a lightweight SMTP client.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make
make install
mkdir -p %{buildroot}/usr/local/bin
cp ~/rpmbuild/BUILD/msmtp-1.8.25/src/msmtp %{buildroot}/usr/local/bin

%files
/usr/local/bin/msmtp

%changelog
* Mon Jan 29 2024 Deneme deneme@deneme.com - %{version}-%{release}
- Initial package

