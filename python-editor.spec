%global pypi_name python-editor

%if 0%{?fedora}
%global with_python3 1
%endif

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-editor
Version:        master
Release:        1%{?dist}
Summary:        Programmatically open an editor, capture the result.

License:        ASL 2.0
URL:            https://github.com/fmoo/python-editor
# We need README.md and LICENSE files in so we don't use pypi tarballs for now
# https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source:         https://github.com/fmoo/python-editor/archive/master.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
An python module which provides a convenient example.


%if 0%{with_python3}
%package -n python3-editor
Summary:        Programmatically open an editor, capture the result.
BuildRequires:  python3-devel

%{?python_provide:%python_provide python3-editor}

%description -n python3-editor
An python module which provides a convenient example.
%endif

%prep
%setup -q -n %{pypi_name}-%{upstream_version}


%build
%{__python2} setup.py build
%if 0%{with_python3}
%{__python3} setup.py build
%endif

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
%if 0%{with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
%endif

%check

%files
%doc README.md
%license LICENSE
%{python2_sitelib}/*

%if 0%{with_python3}
%files -n python3-editor
%license LICENSE
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/editor.py
%{python3_sitelib}/__pycache__/*
%endif


%changelog

