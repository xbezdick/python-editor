%global pypi_name python-editor

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:		python-editor
Version:	0.3
Release:	1%{?dist}
Summary:	Programmatically open an editor, capture the result.

License:	ASL 2.0
URL:		https://github.com/fmoo/python-editor
Source0:	https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch	

BuildRequires:  python2-devel python3-devel
BuildRequires:  python-setuptools

%description
An python module which provides a convenient example.

%package -n python2-editor
Summary:	Programmatically open an editor, capture the result.
%{?python_provide:%python_provide python2-editor}

%description -n python2-editor
An python module which provides a convenient example.

%package -n python3-editor
Summary:	Programmatically open an editor, capture the result.
%{?python_provide:%python_provide python3-editor}

%description -n python3-editor
An python module which provides a convenient example.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}


%build
%{__python2} setup.py build
%{__python3} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
%{__python3} setup.py install --skip-build --root %{buildroot}

%check

%files -n python2-editor
%{python2_sitelib}/*

%files -n python3-editor
%{python3_sitelib}/*



%changelog

