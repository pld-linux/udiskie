Summary:	An automatic disk mounting service using udisks
Summary(pl.UTF-8):	Usługa do automatycznego montowania dysków przy użyciu udisks
Name:		udiskie
Version:	0.3.3
Release:	1
License:	MIT
Group:		Applications
Source0:	http://bitbucket.org/byronclark/udiskie/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	af594ae204565e5a29b05f91319b51d6
URL:		http://bitbucket.org/byronclark/udiskie
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An automatic disk mounting service using udisks.

%description -l pl.UTF-8
Usługa do automatycznego montowania dysków przy użyciu udisks.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
python ./setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" | xargs rm

install -d $RPM_BUILD_ROOT%{_bindir}
install bin/udiskie $RPM_BUILD_ROOT%{_bindir}/udiskie
install bin/udiskie-umount $RPM_BUILD_ROOT%{_bindir}/udiskie-umount

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/*.egg-info
