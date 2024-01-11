%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

%global modname scour
%global sum     An SVG scrubber

Name:               python-scour
Version:            0.35
Release:            10%{?dist}
Summary:            %{sum}

License:            ASL 2.0
URL:                https://github.com/scour-project/scour
Source0:            %{url}/archive/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz

%if %{with python2}
BuildRequires:      python2-devel
BuildRequires:      python2-setuptools
%endif # with python2

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools

BuildArch:          noarch

%description
%{sum}.

%if %{with python2}
%package -n python2-%{modname}
Summary:            %{sum}
%{?python_provide:%python_provide python2-%{modname}}


%description -n python2-%{modname}
%{sum}.
%endif # with python2


%package -n python3-%{modname}
Summary:            %{sum}
%{?python_provide:%python_provide python3-%{modname}}


%description -n python3-%{modname}
%{sum}.


%prep
%autosetup -n %{modname}-%{version}

# Better safe than sorry
find . -type f -name '*.py' -exec sed -i /env\ python/d {} ';'
find . -type f -name '*.py' -exec sed -i /env\ python/d {} ';'

%build
%if %{with python2}
%py2_build
%endif # with python2
%py3_build

%install
%if %{with python2}
%py2_install
%endif # with python2
%py3_install


#%%check
%if %{with python2}
#%%{__python2} setup.py test
%endif # with python2
#%%{__python3} setup.py test

%{!?_licensedir: %global license %doc}

%if %{with python2}
%files -n python2-%{modname}
%doc README.md
%license LICENSE
%{python2_sitelib}/%{modname}/
%{python2_sitelib}/%{modname}-%{version}*
%endif # with python2

%files -n python3-%{modname}
%doc README.md
%license LICENSE
%{_bindir}/%{modname}
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*


%changelog
* Wed Oct 19 2022 Lukas Zachar <lzachar@redhat.com> - 0.35.10
- Add gating test
- Related: rhbz#1891732

* Tue Oct 18 2022 Tomas Popela <tpopela@redhat.com> - 0.35.9
- Bump the release so we can resurrect the python3 subpackages that we need for
  newer Inkscape
- Related: rhbz#1891732

* Sun Jul 22 2018 Charalampos Stratakis <cstratak@redhat.com> - 0.35-8
- Conditionalize the python2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.35-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.35-3
- Rebuild for Python 3.6

* Fri Oct 28 2016 Jon Ciesla <limburgher@gmail.com> - 0.35-2
- Fix Source0.

* Fri Oct 28 2016 Jon Ciesla <limburgher@gmail.com> - 0.35-1
- Initial package.
