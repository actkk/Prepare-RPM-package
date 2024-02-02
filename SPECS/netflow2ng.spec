Name:		netflow2ng
Version:	0.0.5
Release:	2%{?dist}
Summary:	dsasdad

License:        MIT
URL:            https://github.com/synfinatic/netflow2ng
Source0:        %{name}-%{version}.tar.gz

BuildRequires:	epel-release
BuildRequires:	bash
BuildRequires:  make
BuildRequires:	golang
BuildRequires:	zeromq-devel
Requires:       golang
Requires:	zeromq-devel

%global debug_package %{nil}

%description
NetFlow v9 collector for ntopng

%prep
%setup -q -n netflow2ng


%build
make


%install
make
mkdir -p %{buildroot}/usr/local/bin
cp dist/netflow2ng-0.0.5 %{buildroot}/usr/local/bin

%files
/usr/local/bin/netflow2ng-0.0.5


%changelog
* Mon Jan 29 2024 Deneme deneme@deneme.com - %{version}-%{release}
- Initial package for netflow2ng.


