Summary:	An automatic disk mounting service using udisks
Summary(pl.UTF-8):	Usługa do automatycznego montowania dysków przy użyciu udisks
Name:		udiskie
Version:	0.3.5
Release:	1
License:	MIT
Group:		Applications
Source0:	http://bitbucket.org/byronclark/udiskie/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	b352003aa4a87a8fbcc8a77f1e27fc75
URL:		http://bitbucket.org/byronclark/udiskie
BuildRequires:	asciidoc
BuildRequires:	rpm-pythonprov >= 4.1-13
Requires:	udisks
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An automatic disk mounting service using udisks.

%description -l pl.UTF-8
Usługa do automatycznego montowania dysków przy użyciu udisks.

%prep
%setup -q

%build
cd doc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
python ./setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" | xargs rm

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man8
install bin/udiskie $RPM_BUILD_ROOT%{_bindir}/udiskie
install bin/udiskie-umount $RPM_BUILD_ROOT%{_bindir}/udiskie-umount
install doc/%{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/*.egg-info
%{_mandir}/man8/%{name}*
