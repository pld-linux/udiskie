Summary:	An automatic disk mounting service using udisks
Summary(pl.UTF-8):	Usługa do automatycznego montowania dysków przy użyciu udisks
Name:		udiskie
Version:	0.3.7
Release:	3
License:	MIT
Group:		Applications
Source0:	http://bitbucket.org/byronclark/udiskie/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	9f2320d5ee4b8ed8903aec55f12c4d40
URL:		http://bitbucket.org/byronclark/udiskie
BuildRequires:	asciidoc
BuildRequires:	rpm-pythonprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	udisks
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An automatic disk mounting service using udisks.

%description -l pl.UTF-8
Usługa do automatycznego montowania dysków przy użyciu udisks.

%prep
%setup -q

# to autogenerate python interpreter dep
%{__sed} -i -e '1s,^#!.*python,#!%{__python},' bin/*

%build
%{__python} setup.py build

%{__make} -C doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

install -p bin/udiskie $RPM_BUILD_ROOT%{_bindir}/udiskie
install -p bin/udiskie-umount $RPM_BUILD_ROOT%{_bindir}/udiskie-umount
cp -a doc/%{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/udiskie
%attr(755,root,root) %{_bindir}/udiskie-umount
%{py_sitescriptdir}/%{name}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/udiskie-*.egg-info
%endif
%{_mandir}/man8/udiskie.8*
