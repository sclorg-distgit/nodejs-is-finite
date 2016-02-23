%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global npm_name is-finite

Summary:       ES6 Number.isFinite ponyfill
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       1.0.1
Release:       6%{?dist}
License:       MIT
URL:           https://github.com/sindresorhus/is-finite
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
ES6 Number.isFinite() ponyfill

Ponyfill: A polyfill that doesn't overwrite the native method

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%files
%doc license readme.md
%{nodejs_sitelib}/%{npm_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-6
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-5
- Rebuilt with updated metapackage

* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-4
- Enable find provides and requires macro

* Thu Jan 07 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-3
- Enable scl macros

* Thu Sep 10 2015 Troy Dawson <tdawson@redhat.com>
- spec change: npmname -> npm_name

* Thu Sep 10 2015 Troy Dawson <tdawson@redhat.com> - 1.0.1-1
- Initial package