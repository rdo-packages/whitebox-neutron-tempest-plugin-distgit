%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg 0
%global sources_gpg_sign 0xa7475c5f2122fec3f90343223fe3bf5aad1080e4
%global plugin whitebox-neutron-tempest-plugin
%global module whitebox_neutron_tempest_plugin
%global with_doc 0

%{!?upstream_version: %global upstream_version %{commit}}
%global commit 73402012d40a549561eeb8f57917b089315bba9f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

%{?dlrn: %global tarsources %{module}-%{upstream_version}}
%{!?dlrn: %global tarsources %{plugin}}


%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
This package contains whitebox Tempest tests to cover the Neutron project. \
Additionally it provides a plugin to automatically load these tests into Tempest.

Name:       python-whitebox-neutron-tests-tempest
Version:    0.0.1
Release:    1.1%{?alphatag}%{?dist}
Summary:    Whitebox Tempest tests related to the Neutron Project
License:    ASL 2.0
URL:        https://opendev.org/x/%{plugin}/

Source0:    http://opendev.org/x/%{plugin}/archive/%{upstream_version}.tar.gz#/%{module}-%{shortcommit}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        http://tarballs.opendev.org/x/%{plugin}/%{plugin}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.opendev.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python3-whitebox-neutron-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python3-whitebox-neutron-tests-tempest}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Requires:   python3-subunit >= 0.0.18
Requires:   python3-testtools >= 0.9.30
Requires:   python3-cryptography >= 2.5
Requires:   python3-netaddr
Requires:   python3-netifaces

%description -n python3-whitebox-neutron-tests-tempest
%{common_desc}

%if 0%{?with_doc}
%package -n python-whitebox-neutron-tests-tempest-doc
Summary:        Documentation for python-whitebox-neutron-tests-tempest

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-whitebox-neutron-tests-tempest-doc
It contains the documentation for the Whitebox Neutron Tempest plugin.
%endif

%prep
%autosetup -n %{tarsources} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%{py3_build}

# Generate Docs
%if 0%{?with_doc}
sphinx-build -W -b html doc/source doc/build/html
# remove the sphinx build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%files -n python3-whitebox-neutron-tests-tempest
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/*.egg-info

%if 0%{?with_doc}
%files -n python-whitebox-neutron-tests-tempest-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
* Mon Mar 20 2023 RDO <dev@lists.rdoproject.org> 0.0.1-1.1.7340201git
- Update to post 0.0.1

