# Created by pyp2rpm-3.3.2
%global pypi_name hvac

Name:           python-%{pypi_name}
Version:        0.7.2
Release:        1%{?dist}
Summary:        HashiCorp Vault API client

License:        None
URL:            https://github.com/hvac/hvac
Source0:        https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 ![Header image]( [Vault]() API client for Python 2.7/3.x[![Travis CI](
[![codecov]( [![Documentation Status]( [![PyPI version]( [![Twitter -
@python_hvac](

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(pyhcl) >= 0.3.10
Requires:       python3dist(requests) >= 2.21.0
%description -n python3-%{pypi_name}
 ![Header image]( [Vault]() API client for Python 2.7/3.x[![Travis CI](
[![codecov]( [![Documentation Status]( [![PyPI version]( [![Twitter -
@python_hvac](


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/%{pypi_name}
# Make sure this stays commented out or deleted to build successfully.
# MANIFEST.in prunes it, # but pyp2rpm lists it anyway.
#%%{python3_sitelib}/tests
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Mar 21 2019 Mike DePaulo <mikedep333@redhat.com> - 0.7.2-1
- Initial package.
