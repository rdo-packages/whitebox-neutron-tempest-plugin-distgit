%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2ef3fe0ec2b075ab7458b5f8b702b20b13df2318
%global plugin whitebox-neutron-tempest-plugin
%global module whitebox_neutron_tempest_plugin
%global with_doc 0


%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
This package contains whitebox Tempest tests to cover the Neutron project. \
Additionally it provides a plugin to automatically load these tests into Tempest.

Name:       python-whitebox-neutron-tests-tempest
Version:    0.1.0
Release:    1%{?dist}
Summary:    Whitebox Tempest tests related to the Neutron Project
License:    ASL 2.0
URL:        https://opendev.org/x/%{plugin}/

Source0:    http://tarballs.opendev.org/x/%{plugin}/%{plugin}-%{upstream_version}.tar.gz
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

Requires:   python3-coverage > 4.4
Requires:   python3-oslotest >= 3.2.0
Requires:   python3-stestr >= 1.0.0
Requires:   python3-subunit >= 1.0.0
Requires:   python3-testtools >= 2.2.0
Requires:   python3-scapy
Requires:   python3-netaddr
Requires:   python3-netifaces
Requires:   python3-pyroute2 >= 0.6.6
Requires:   python3-neutron-tests-tempest

%description -n python3-whitebox-neutron-tests-tempest
%{common_desc}

%if 0%{?with_doc}
%package -n python-whitebox-neutron-tests-tempest-doc
Summary:        Documentation for python-whitebox-neutron-tests-tempest

BuildRequires:  python3-sphinx > 2.1.0
BuildRequires:  python3-openstackdocstheme >= 1.20.0
BuildRequires:  python3-reno >= 1.20.0

%description -n python-whitebox-neutron-tests-tempest-doc
It contains the documentation for the Whitebox Neutron Tempest plugin.
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{module}-%{upstream_version} -S git

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
* Tue Mar 26 2024 RDO <dev@lists.rdoproject.org> 0.1.0-1
- Update to 0.1.0

