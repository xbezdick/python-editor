%global pypi_name python-editor

%if 0%{?fedora}
%global with_python3 1
%endif

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-editor
Version:        0.3
Release:        1%{?dist}
Summary:        Programmatically open an editor, capture the result.

License:        ASL 2.0
URL:            https://github.com/fmoo/python-editor
# We need README.md and LICENSE files in so we don't use pypi tarballs for now
Source:         https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

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
rm -rf %{pypi_name}.egg-info

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
# https://github.com/fmoo/python-editor/issues/3
#%doc README.md
#%license LICENSE
%{python2_sitelib}/editor.py*
%{python2_sitelib}/python_editor-%{version}-py?.?.egg-info

%if 0%{with_python3}
%files -n python3-editor
# https://github.com/fmoo/python-editor/issues/3
#%doc README.md
#%license LICENSE
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/editor.py*
%{python3_sitelib}/__pycache__/*
%endif


%changelog
* Tue Aug 25 2015 Lukas Bezdicka <lbezdick@redhat.com> - 0.3-1
- initial package
