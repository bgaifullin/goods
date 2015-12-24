%global package_name packetary
%global with_python3 1

%{!?version: %define version 0.1.0}
%{!?release: %define release 1}

Name: python-%{package_name}
Version: %{version}
Release: %{release}%{?dist}
Summary: Package allows to build and clone deb and rpm repositories

License: GPLv2
Source0: %{package_name}-%{version}.tar.gz
URL:     https://github.com/openstack/packetary
Group:   Development/Libraries

BuildRequires:  git
BuildRequires: python-devel
BuildRequires: python-setuptools
BuildRequires: python-pbr
BuildArch: noarch

%if %{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
%endif # if with_python3

Requires:    createrepo
Requires:    python
Requires:    python-babel >= 1.3
Requires:    python-bintrees >= 2.0.2
Requires:    python-chardet >= 2.0.1
Requires:    python-cliff >= 1.7.0
Requires:    python-debian >= 0.1.21
Requires:    python-eventlet >= 0.15
Requires:    python-lxml >= 1.1.23
Requires:    python-pbr >= 0.8
Requires:    python-six >= 1.5.2
Requires:    python-stevedore >= 1.1.0
# Workaroud for babel bug
Requires:    pytz

%description
This Python package provides object model and API for dealing with deb
and rpm repositories. One can use this framework to
implement operations like building repository
from a set of packages, clone repository, find package
dependencies, mix repositories, pull out a subset of
packages into a separate repository, etc.


%if 0%{?with_python3}
%package -n     python3-%{package_name}
Summary:        Package allows to build and clone deb and rpm repositories

%description -n python3-%{package_name}
This Python 3 package provides object model and API for dealing with deb
and rpm repositories. One can use this framework to
implement operations like building repository
from a set of packages, clone repository, find package
dependencies, mix repositories, pull out a subset of
packages into a separate repository, etc.

%endif # with_python3

%prep
%setup -q -n %{package_name}-%{version}

%build
%{__python2} setup.py build

%if 0%{?with_python3}
%{__python3} setup.py build
%endif # with_python3

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if 0%{?with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
# rename the entry-point to avoid conflict
mv %{buildroot}/%{_bindir}/%{package_name} %{buildroot}/%{_bindir}/%{package_name}3
%endif # with_python3

%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst LICENSE
%{python2_sitelib}/%{package_name}
%{python2_sitelib}/%{package_name}-%{version}-py?.?.egg-info
%{_bindir}/%{package_name}

%if 0%{?with_python3}
%files -n python3-%{package_name}
%doc README.rst LICENSE
%{python3_sitelib}/%{package_name}
%{python3_sitelib}/%{package_name}-%{version}-py?.?.egg-info
%{_bindir}/%{package_name}3
%endif # with_python3


%changelog
* Tue Dec 22 2015 Bulat Gaifullin <bgaifullin@mirantis.com> - 0.1.0-1
- Initial package.
